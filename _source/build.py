"""Régénère le kit : PDF au gabarit La Rochelle Université et archives ZIP.

Usage : python build.py   (dépendance : reportlab)
"""
import re
import zipfile
from pathlib import Path

from reportlab import rl_config
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, ListFlowable, ListItem,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

from atelier_ia import ATELIER, fichiers_correction, fichiers_depart
from corrections import archives
from figures import BLEU, FIGURES, FILET, GRIS, SCHEMAS_DOCS, TEXTE
from sujets import DEROULE, FICHE_DOC, FICHE_MD, GUIDE_WP, LISEZ_MOI, SUJETS

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
ASSETS = ICI / "assets"

# Charte graphique 2024 : A4, logo de 3 cm en haut à gauche, marges de 1,5 cm.
# Police : Texte LRU, dérivée de Raleway, la police du document de la charte (voir polices.py).
LOGO_LARGEUR = 3 * cm
MARGE = 1.5 * cm
LARGEUR, HAUTEUR = A4

# Tailles et couleurs relevées dans le document de la charte :
# texte Regular 10 pt noir ; titres ExtraBold bleu 25, 14 et 10 pt ; repères ExtraBold noir 10 pt.
for nom, fichier in [("TL", "Regular"), ("TL-B", "Bold"), ("TL-SB", "SemiBold"), ("TL-XB", "ExtraBold")]:
    pdfmetrics.registerFont(TTFont(nom, str(ASSETS / f"TexteLRU-{fichier}.ttf")))
pdfmetrics.registerFontFamily("TL", normal="TL", bold="TL-B", italic="TL", boldItalic="TL-B")
rl_config.canvas_basefontname = "TL"

CORPS = ParagraphStyle("corps", fontName="TL", fontSize=10, leading=13.6, textColor=TEXTE,
                       alignment=TA_LEFT, spaceAfter=3)
SECTION = ParagraphStyle("section", fontName="TL-XB", fontSize=14, leading=17, textColor=BLEU,
                         spaceBefore=10, spaceAfter=3, keepWithNext=1)
CELLULE = ParagraphStyle("cellule", parent=CORPS, fontSize=9, leading=11.5, spaceAfter=0)
ENTETE_CELLULE = ParagraphStyle("entete", parent=CELLULE, fontName="TL-XB", textColor=white)
BOITE_TITRE = ParagraphStyle("boite", parent=CORPS, fontName="TL-XB", fontSize=14, leading=17,
                             textColor=BLEU, spaceAfter=4)
KICKER = ParagraphStyle("kicker", fontName="TL-XB", fontSize=10, leading=13, textColor=TEXTE)
TITRE = ParagraphStyle("titre", fontName="TL-XB", fontSize=25, leading=27, textColor=BLEU)
META = ParagraphStyle("meta", fontName="TL", fontSize=10, leading=13, textColor=TEXTE)
LEGENDE = ParagraphStyle("legende", parent=CORPS, fontSize=8, leading=10.5, textColor=GRIS,
                         alignment=TA_CENTER, spaceBefore=3, spaceAfter=6)


def en_ligne(texte):
    """Convertit `code` et **gras** en balises reportlab, en échappant le reste."""
    morceaux = re.split(r"(`[^`]*`)", texte)
    sortie = []
    for morceau in morceaux:
        code = morceau.startswith("`") and morceau.endswith("`") and len(morceau) > 1
        contenu = morceau[1:-1] if code else morceau
        contenu = contenu.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        if code:
            sortie.append(f'<font name="TL-SB" color="#256CB4">{contenu}</font>')
        else:
            sortie.append(re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", contenu))
    return "".join(sortie)


def para(texte, style=CORPS):
    return Paragraph(en_ligne(texte), style)


def liste(items, numerotee=False):
    options = dict(bulletType="1", bulletFontName="TL-XB", bulletColor=BLEU, leftIndent=15,
                   bulletFontSize=10) if numerotee else dict(
        bulletType="bullet", start="–", bulletColor=TEXTE, bulletFontName="TL", leftIndent=12, bulletFontSize=10)
    return ListFlowable([ListItem(para(i), spaceAfter=0) for i in items], **options)


def boite(titre, items):
    """Encadré bleu, repris du style des encadrés de la charte."""
    contenu = [para(titre, BOITE_TITRE), liste(items)]
    table = Table([[contenu]], colWidths=[LARGEUR - 2 * MARGE])
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "TL"),
        ("BOX", (0, 0), (-1, -1), 3, BLEU),
        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether([Spacer(1, 5), table, Spacer(1, 3)])


def tableau(lignes, largeurs):
    avec_entete = len(lignes) > 1 and len(lignes[0]) > 2 or lignes[0][0] == "TP"
    donnees = []
    for i, ligne in enumerate(lignes):
        style = ENTETE_CELLULE if avec_entete and i == 0 else CELLULE
        donnees.append([para(c, style) for c in ligne])
    hauteur = None if lignes[0][0] == "TP" else [None if avec_entete and i == 0 else 0.75 * cm
                                                 for i in range(len(lignes))]
    table = Table(donnees, colWidths=[l * cm for l in largeurs], rowHeights=hauteur, repeatRows=1 if avec_entete else 0)
    style = [("FONTNAME", (0, 0), (-1, -1), "TL"), ("GRID", (0, 0), (-1, -1), 0.5, FILET), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    if avec_entete:
        style.append(("BACKGROUND", (0, 0), (-1, 0), BLEU))
    table.setStyle(TableStyle(style))
    return table


def lignes_vides(n):
    table = Table([[""] for _ in range(n)], colWidths=[LARGEUR - 2 * MARGE], rowHeights=[0.75 * cm] * n)
    table.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), "TL"), ("LINEBELOW", (0, 0), (-1, -1), 0.5, FILET)]))
    return table


def creer_pdf(chemin, kicker, titre, meta, histoire, pied):
    def premiere(c, doc):
        c.saveState()
        # Logo : 3 cm, à 1,5 cm du haut et de la gauche ; rien n'y est rattaché.
        c.drawImage(str(ASSETS / "logo-la-rochelle-universite.png"), MARGE, HAUTEUR - MARGE - LOGO_LARGEUR,
                    LOGO_LARGEUR, LOGO_LARGEUR, mask="auto")
        # Filet noir comme dans la charte, à distance du logo (zone de protection).
        filet = MARGE + LOGO_LARGEUR + 0.8 * cm
        c.setStrokeColor(TEXTE)
        c.setLineWidth(0.8)
        c.line(filet, HAUTEUR - MARGE, filet, HAUTEUR - MARGE - LOGO_LARGEUR)
        x = filet + 0.6 * cm
        largeur = LARGEUR - x - MARGE
        y = HAUTEUR - MARGE
        for texte, style in [(kicker.upper(), KICKER), (titre, TITRE), (meta, META)]:
            p = Paragraph(en_ligne(texte), style)
            _, h = p.wrap(largeur, 10 * cm)
            y -= h
            p.drawOn(c, x, y)
            y -= 4
        c.restoreState()
        pied_page(c, doc)

    def pied_page(c, doc):
        c.saveState()
        c.setStrokeColor(FILET)
        c.setLineWidth(0.5)
        c.line(MARGE, 1.35 * cm, LARGEUR - MARGE, 1.35 * cm)
        c.setFont("TL", 8)
        c.setFillColor(GRIS)
        c.drawString(MARGE, 0.95 * cm, pied)
        c.drawRightString(LARGEUR - MARGE, 0.95 * cm, f"Page {doc.page}")
        c.restoreState()

    bas = 1.6 * cm
    haut_premier = HAUTEUR - MARGE - LOGO_LARGEUR - 0.45 * cm
    doc = BaseDocTemplate(str(chemin), pagesize=A4, title=f"{titre}", author="La Rochelle Université",
                          subject=kicker, lang="fr-FR")
    cadre = dict(leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="premiere", frames=[Frame(MARGE, bas, LARGEUR - 2 * MARGE, haut_premier - bas, **cadre)],
                     onPage=premiere, autoNextPageTemplate="suite"),
        PageTemplate(id="suite", frames=[Frame(MARGE, bas, LARGEUR - 2 * MARGE, HAUTEUR - MARGE - bas, **cadre)],
                     onPage=pied_page),
    ])
    doc.build(histoire)


def figure(element, legende, numero):
    element.hAlign = "CENTER"
    return KeepTogether([Spacer(1, 4), element, para(f"**Figure {numero}.** {legende}", LEGENDE)])


def section(titre, *contenu):
    """Garde le titre avec le début de son contenu."""
    return [KeepTogether([para(titre, SECTION), contenu[0]]), *contenu[1:]]


def histoire_sujet(s):
    h = []
    figures = FIGURES.get(s["num"], {})
    avant, apres = figures.get("avant", []), figures.get("apres", [])
    h += section("Objectifs pédagogiques", liste(s["objectifs"]))
    h += section("Notions étudiées", para(s["notions"]))
    h += section("Mise en situation", para(s["situation"]))
    h += section("Préparation et matériel", para(s["prep"]))
    numero = 0
    if avant:
        h.append(para("Repères", SECTION))
    for element, legende in avant:
        numero += 1
        h.append(figure(element, legende, numero))
    h += section("Travail demandé", liste(s["travail"], numerotee=True))
    if s.get("cahier"):
        h.append(boite(*s["cahier"]))
    for element, legende in apres:
        numero += 1
        h.append(figure(element, legende, numero))
    h += section("Contraintes", para(s["contraintes"]))
    h += section("Critères de réussite", para(s["criteres"]))
    rendu = [para(s["rendre"]), para(f"Nom de rendu : `TP{s['num']}_NOM_Prenom.zip`")]
    h += section("À rendre", *rendu)
    if s.get("plus"):
        h += section("Pour aller plus loin (facultatif)", para(s["plus"]))
    return h


def histoire_doc(d):
    h = []
    titre = None
    for bloc in d["blocs"]:
        genre = bloc[0]
        if genre == "h":
            titre = para(bloc[1], SECTION)
            continue
        if genre == "schema":
            # La figure est déjà insécable : le style du titre suffit à les garder ensemble.
            if titre:
                h.append(titre)
                titre = None
            h.append(figure(*SCHEMAS_DOCS[bloc[1]], bloc[2]))
            continue
        if genre == "p":
            element = para(bloc[1])
        elif genre == "ul":
            element = liste(bloc[1])
        elif genre == "table":
            element = tableau(bloc[1], bloc[2])
        elif genre == "box":
            element = boite(bloc[1], bloc[2])
        else:
            element = lignes_vides(bloc[1])
        # Un titre reste sur la même page que le bloc qui le suit.
        h.append(KeepTogether([titre, element]) if titre else element)
        titre = None
    return h


def construire():
    pied_tp = "La Rochelle Université · Développement web"
    for s in SUJETS:
        dossier = RACINE / f"TP{s['num']}"
        dossier.mkdir(exist_ok=True)
        kicker = f"Développement web · TP {s['num']}" + (" · Évaluation" if s.get("evaluation") else "")
        meta = f"Durée : 1h30 · Niveau : débutant · Projet : {s['projet']}"
        creer_pdf(dossier / f"TP{s['num']}_Sujet.pdf", kicker, s["titre"], meta, histoire_sujet(s),
                  f"{pied_tp} · TP {s['num']}")

    dossier = RACINE / "Atelier_IA"
    dossier.mkdir(exist_ok=True)
    creer_pdf(dossier / "Atelier_IA_Sujet.pdf", ATELIER["kicker"], ATELIER["titre"],
              f"Durée : 1h30 · Niveau : débutant · Projet : {ATELIER['projet']}", histoire_sujet(ATELIER),
              f"{pied_tp} · Atelier IA")

    for d in (DEROULE, GUIDE_WP, FICHE_DOC):
        creer_pdf(RACINE / d["fichier"], d["kicker"], d["titre"], d["meta"], histoire_doc(d), pied_tp)

    (RACINE / "Fiche_realisation_WordPress.md").write_text(FICHE_MD, encoding="utf-8")
    (RACINE / "LISEZ_MOI.txt").write_text(LISEZ_MOI, encoding="utf-8")

    lots = {**archives(), "Atelier_IA/Atelier_IA_Fichiers_depart.zip": fichiers_depart(),
            "Atelier_IA/Atelier_IA_Correction.zip": fichiers_correction()}
    for nom, fichiers in lots.items():
        chemin = RACINE / nom
        chemin.parent.mkdir(exist_ok=True)
        with zipfile.ZipFile(chemin, "w", zipfile.ZIP_DEFLATED) as z:
            for interne, contenu in sorted(fichiers.items()):
                z.writestr(interne, contenu)


if __name__ == "__main__":
    construire()
