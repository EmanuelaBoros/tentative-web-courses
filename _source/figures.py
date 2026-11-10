"""Figures des sujets : schémas vectoriels et captures des corrections.

Les évaluations (TP5, TP10) n'utilisent que des schémas : une capture de la
correction donnerait la réponse.
"""
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Flowable, Image

ASSETS = Path(__file__).resolve().parent / "assets"
CAPTURES = ASSETS / "captures"

BLEU = HexColor("#256CB4")  # bleu de la charte
MARINE = HexColor("#00346B")
TEXTE = HexColor("#000000")
GRIS = HexColor("#555555")
FILET = HexColor("#BFC7CF")
PALE = HexColor("#ECEFF2")
ALERTE = HexColor("#A4161A")

L = 510  # largeur utile en points (18 cm)


class Schema(Flowable):
    def __init__(self, hauteur, dessin, largeur=L):
        super().__init__()
        self.width, self.height, self.dessin = largeur, hauteur, dessin

    def wrap(self, *_):
        return self.width, self.height

    def draw(self):
        self.canv.saveState()
        self.dessin(self.canv)
        self.canv.restoreState()


def texte(c, x, y, t, taille=9, gras=False, couleur=TEXTE, align="c", mono=False):
    # Raleway est large : on réduit légèrement le texte des schémas.
    c.setFont("TL-SB" if mono else ("TL-B" if gras else "TL"), taille * 0.9)
    c.setFillColor(couleur)
    {"c": c.drawCentredString, "g": c.drawString, "d": c.drawRightString}[align](x, y, t)


def boite(c, x, y, w, h, t="", fond=white, trait=BLEU, couleur=TEXTE, taille=9, gras=False, r=0, tirets=False):
    c.setFillColor(fond)
    c.setStrokeColor(trait)
    c.setLineWidth(1)
    c.setDash(3, 2) if tirets else c.setDash()
    c.roundRect(x, y, w, h, r, stroke=1, fill=1)
    c.setDash()
    lignes = t.split("\n") if t else []
    pas = taille + 2
    depart = y + h / 2 + (len(lignes) - 1) * pas / 2 - taille * 0.34
    for i, ligne in enumerate(lignes):
        texte(c, x + w / 2, depart - i * pas, ligne, taille, gras, couleur)


def bloc(c, x, y, w, h, t="", taille=8, fond=PALE, couleur=TEXTE, gras=False):
    boite(c, x, y, w, h, t, fond=fond, trait=FILET, taille=taille, couleur=couleur, gras=gras)


def fleche(c, x1, y1, x2, y2, couleur=MARINE, largeur=1.2):
    from math import atan2, cos, sin
    c.setStrokeColor(couleur)
    c.setFillColor(couleur)
    c.setLineWidth(largeur)
    a = atan2(y2 - y1, x2 - x1)
    bx, by = x2 - 6 * cos(a), y2 - 6 * sin(a)
    c.line(x1, y1, bx, by)
    p = c.beginPath()
    p.moveTo(x2, y2)
    p.lineTo(bx - 3 * sin(a), by + 3 * cos(a))
    p.lineTo(bx + 3 * sin(a), by - 3 * cos(a))
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def anatomie(c, x, y, code, reperes, taille=11):
    """Code avec des accolades étiquetées dessous (0) ou dessus (1)."""
    largeur = lambda t: stringWidth(t, "TL-SB", taille * 0.9)
    texte(c, x, y, code, taille, couleur=MARINE, align="g", mono=True)
    for debut, fin, etiquette, dessus in reperes:
        i = code.index(debut)
        j = code.index(fin, i) + len(fin)
        x1, x2 = x + largeur(code[:i]), x + largeur(code[:j])
        ligne = y + taille + 2 if dessus else y - 4
        pointe = ligne + 3 if dessus else ligne - 3
        c.setStrokeColor(BLEU)
        c.setLineWidth(1)
        c.line(x1, ligne, x1, pointe)
        c.line(x1, pointe, x2, pointe)
        c.line(x2, pointe, x2, ligne)
        texte(c, (x1 + x2) / 2, pointe + 3 if dessus else pointe - 10, etiquette, 8.5, True, BLEU)


# ---------------------------------------------------------------- TP1
def client_serveur(c):
    boite(c, 10, 34, 120, 60, "Navigateur\n(client)", fond=PALE, gras=True, taille=10)
    boite(c, 380, 34, 120, 60, "Serveur", fond=PALE, gras=True, taille=10)
    fleche(c, 134, 76, 376, 76)
    texte(c, 255, 81, "1. Requête HTTP(S) : « donne-moi cette page »")
    fleche(c, 376, 50, 134, 50)
    texte(c, 255, 37, "2. Réponse : fichiers HTML, CSS, JavaScript, images")
    for i, (a, b) in enumerate([("HTML", "structure"), ("CSS", "présentation"), ("JavaScript", "comportement")]):
        x = 70 + i * 130
        bloc(c, x, 2, 120, 22, f"{a} : {b}", 8.5)


def anatomie_url(c):
    anatomie(c, 30, 88, "https://www.larochelle.fr/culture/agenda.html", [
        ("https", "https", "protocole", 0), ("www", ".fr", "nom de domaine", 0), ("/culture", ".html", "chemin", 0)])
    anatomie(c, 30, 26, '<a href="https://www.larochelle.fr/">Ville de La Rochelle</a>', [
        ("<a", '/">', "balise ouvrante", 1), ("href", "href", "attribut", 0),
        ('"https', '/"', "valeur", 0), ("Ville", "Rochelle", "contenu", 1), ("</a>", "</a>", "fermante", 1)], 10.5)


# ---------------------------------------------------------------- TP2
def arborescence_squelette(c):
    texte(c, 10, 128, "Organisation des fichiers", 9.5, True, BLEU, "g")
    for i, (ligne, dec) in enumerate([("oceanfest/", 0), ("index.html", 1), ("apropos.html", 1), ("contact.html", 1),
                                      ("images/", 1), ("ocean.svg", 2)]):
        texte(c, 14 + dec * 16, 110 - i * 17, ligne, 9.5, couleur=MARINE, align="g", mono=True)
    texte(c, 205, 128, "Structure de chaque page", 9.5, True, BLEU, "g")
    boite(c, 205, 8, 135, 112, trait=FILET)
    bloc(c, 212, 92, 121, 22, "header + nav")
    bloc(c, 212, 34, 121, 54, "main\n(section, article...)", fond=white)
    bloc(c, 212, 13, 121, 17, "footer")
    texte(c, 375, 128, "Menu : liens relatifs", 9.5, True, BLEU, "g")
    pages = [(375, 88, "index.html"), (375, 18, "apropos.html"), (440, 53, "contact.html")]
    for x, y, t in pages:
        boite(c, x, y, 68, 24, t, taille=8, fond=PALE)
    fleche(c, 400, 86, 400, 44)
    fleche(c, 400, 44, 400, 86)
    fleche(c, 444, 88, 470, 79)
    fleche(c, 444, 34, 470, 51)


def lien_label(c):
    anatomie(c, 22, 30, '<label for="nom">Nom</label>', [('for="nom"', 'for="nom"', "for", 1)], 10.5)
    anatomie(c, 288, 30, '<input id="nom" name="nom">', [('id="nom"', 'id="nom"', "id", 1)], 10.5)
    texte(c, 255, 8, "Même valeur pour for et id : un clic sur le libellé active le champ, et les lecteurs d’écran l’annoncent.", 9)


# ---------------------------------------------------------------- TP3
def modele_boite(c):
    x, y = 8, 6
    boite(c, x, y, 290, 150, fond=white, trait=GRIS, tirets=True)
    texte(c, x + 8, y + 137, "margin : espace extérieur", 9, True, GRIS, "g")
    boite(c, x + 25, y + 18, 240, 110, fond=MARINE, trait=MARINE)
    texte(c, x + 33, y + 115, "border : contour", 9, True, white, "g")
    boite(c, x + 33, y + 26, 224, 84, fond=PALE, trait=PALE)
    texte(c, x + 41, y + 96, "padding : espace intérieur", 9, True, MARINE, "g")
    boite(c, x + 62, y + 38, 166, 50, "contenu\n(titre et texte de la carte)", trait=BLEU)
    texte(c, 325, 146, "Quelle règle s’applique ?", 9.5, True, BLEU, "g")
    for i, (sel, spec, w) in enumerate([("p  (élément)", "0,0,1", 70), (".card  (classe)", "0,1,0", 115), ("#carte-phare  (id)", "1,0,0", 170)]):
        y2 = 118 - i * 29
        texte(c, 325, y2 + 15, sel, 9, align="g")
        c.setFillColor(BLEU)
        c.rect(325, y2, w, 12, stroke=0, fill=1)
        texte(c, 330, y2 + 3, spec, 8.5, True, white, "g")
    for i, ligne in enumerate(["La spécificité la plus forte l’emporte.", "À égalité, la dernière règle écrite gagne.",
                               "box-sizing: border-box : la largeur déclarée", "inclut padding et border."]):
        texte(c, 325, 44 - i * 12, ligne, 9, align="g")


# ---------------------------------------------------------------- Maquettes
def _cadre(c, x, y, w, h, titre):
    texte(c, x + w / 2, y + h + 5, titre, 9.5, True, BLEU)
    boite(c, x, y, w, h, trait=GRIS)


def responsive_ocean(c):
    x, y, w, h = 8, 6, 318, 172
    _cadre(c, x, y, w, h, "Grand écran (1280 px)")
    bloc(c, x + 5, y + h - 30, w - 10, 25, "")
    texte(c, x + 12, y + h - 21, "Ocean Fest", 8.5, True, align="g")
    for i, m in enumerate(["Accueil", "À propos", "Contact"]):
        bloc(c, x + 170 + i * 46, y + h - 25, 43, 15, m, 7.5, fond=white)
    texte(c, x + w / 2, y + h - 42, "Flexbox : marque à gauche, menu à droite", 8, couleur=GRIS)
    boite(c, x + 25, y + 26, w - 50, 96, trait=BLEU, tirets=True)
    texte(c, x + w / 2, y + 110, "Zone centrale limitée par max-width", 8, True, BLEU)
    for i in range(3):
        bloc(c, x + 33 + i * 87, y + 50, 80, 52, f"Carte {i + 1}", fond=white)
    texte(c, x + w / 2, y + 33, "Grid : 3 colonnes de même largeur", 8, couleur=GRIS)
    bloc(c, x + 5, y + 5, w - 10, 16, "footer")
    fleche(c, 332, 90, 388, 90)
    texte(c, 360, 96, "≤ 700 px", 8.5, True)
    x, w = 396, 104
    _cadre(c, x, y, w, h, "Mobile (375 px)")
    bloc(c, x + 5, y + h - 53, w - 10, 48, "Ocean Fest\nAccueil\nÀ propos\nContact", 7.5)
    for i in range(3):
        bloc(c, x + 12, y + 77 - i * 29, w - 24, 26, f"Carte {i + 1}", fond=white)
    bloc(c, x + 5, y + 5, w - 10, 14, "footer", 7.5)


def maquette_forum(c):
    x, y, w, h = 8, 6, 330, 205
    _cadre(c, x, y, w, h, "À partir de 700 px")
    bloc(c, x + 5, y + h - 32, w - 10, 27, "En-tête centré : nom du forum et navigation", fond=white)
    bloc(c, x + 5, y + h - 72, w - 10, 37, "Introduction : bandeau coloré sur toute la largeur", 8.5, gras=True)
    for i, m in enumerate(["Développeur web", "UX Designer", "Administrateur\nde systèmes"]):
        bloc(c, x + 12 + i * 104, y + 66, 98, 58, m, fond=white)
    bloc(c, x + 5, y + 27, w - 10, 34, "Bloc contact, visuellement distinct des cartes")
    bloc(c, x + 5, y + 5, w - 10, 18, "Pied de page", fond=white)
    x, w = 392, 110
    _cadre(c, x, y, w, h, "Sous 700 px")
    bloc(c, x + 5, y + h - 27, w - 10, 22, "En-tête centré", 7.5, fond=white)
    bloc(c, x + 5, y + h - 57, w - 10, 27, "Introduction", 8, gras=True)
    for i, m in enumerate(["Développeur web", "UX Designer", "Administrateur"]):
        bloc(c, x + 12, y + 96 - i * 29, w - 24, 26, m, 7.5, fond=white)
    bloc(c, x + 5, y + 21, w - 10, 16, "Contact", 7.5)
    bloc(c, x + 5, y + 5, w - 10, 13, "Pied de page", 7, fond=white)
    fleche(c, 344, 110, 386, 110)


# ---------------------------------------------------------------- TP6
def etats_js(c):
    texte(c, 10, 104, "Thème : alterner une classe sur body", 9.5, True, BLEU, "g")
    boite(c, 10, 32, 90, 50, "Mode jour\nbody", fond=white, gras=True)
    boite(c, 170, 32, 90, 50, "Mode nuit\nbody.nuit", fond=MARINE, couleur=white, trait=MARINE, gras=True)
    fleche(c, 102, 68, 168, 68)
    fleche(c, 168, 46, 102, 46)
    texte(c, 135, 73, "clic", 8.5)
    texte(c, 135, 33, "clic", 8.5)
    texte(c, 10, 12, "Un booléen retient l’état ; une condition choisit le texte du bouton.", 8.5, couleur=GRIS, align="g")
    texte(c, 300, 104, "Artistes : avancer, puis recommencer", 9.5, True, BLEU, "g")
    for i, a in enumerate(["Artiste 1", "Artiste 2", "Artiste 3"]):
        boite(c, 300 + i * 72, 50, 56, 32, f"{a}\nindice {i}", taille=7.5, fond=PALE)
        if i < 2:
            fleche(c, 357 + i * 72, 66, 371 + i * 72, 66)
    c.setStrokeColor(MARINE)
    c.setLineWidth(1.2)
    c.line(472, 50, 472, 34)
    c.line(472, 34, 328, 34)
    fleche(c, 328, 34, 328, 48)
    texte(c, 400, 38, "clic : retour au début", 8.5)
    texte(c, 300, 12, "Chaque clic affiche un nom et avance l’indice.", 8.5, couleur=GRIS, align="g")


# ---------------------------------------------------------------- TP7
def logique_formulaire(c):
    y = 62
    etapes = ["Événement\nsubmit", "Empêcher le\nrechargement", "Lire et nettoyer\nla saisie"]
    for i, e in enumerate(etapes):
        boite(c, 4 + i * 92, y, 80, 36, e, taille=8, fond=PALE)
        fleche(c, 85 + i * 92, y + 18, 95 + i * 92, y + 18)
    cx, cy = 318, y + 18
    p = c.beginPath()
    for k, (dx, dy) in enumerate([(-42, 0), (0, 26), (42, 0), (0, -26)]):
        (p.moveTo if k == 0 else p.lineTo)(cx + dx, cy + dy)
    p.close()
    c.setFillColor(white)
    c.setStrokeColor(BLEU)
    c.drawPath(p, stroke=1, fill=1)
    texte(c, cx, cy - 3, "Champ vide ?", 8, True)
    fleche(c, 361, cy, 388, cy)
    texte(c, 374, cy + 5, "non", 8, True)
    boite(c, 390, y - 2, 56, 40, "Créer le li\net l’ajouter", taille=7.5, fond=PALE)
    fleche(c, 447, cy, 456, cy)
    boite(c, 457, y - 2, 50, 40, "Mettre à\njour le\ncompteur", taille=7.5, fond=PALE)
    fleche(c, cx, cy - 27, cx, 34)
    texte(c, cx + 14, 42, "oui", 8, True)
    boite(c, cx - 66, 4, 132, 29, "Afficher l’erreur (role=\"alert\")\net replacer le focus", taille=8, trait=ALERTE)


def arbre_dom(c):
    noeuds = {"ul": (120, 70, "ul#liste"), "li": (120, 38, "li"), "span": (60, 6, "span : texte"), "bt": (180, 6, "button : Supprimer")}
    for a, b in [("ul", "li"), ("li", "span"), ("li", "bt")]:
        c.setStrokeColor(BLEU)
        c.line(noeuds[a][0], noeuds[a][1], noeuds[b][0], noeuds[b][1] + 20)
    for x, y, t in noeuds.values():
        boite(c, x - 54, y, 108, 20, t, taille=8.5, fond=PALE)
    texte(c, 268, 66, "Chaque tâche est un petit arbre créé en JavaScript :", 9, align="g")
    texte(c, 268, 50, "1. créer les éléments (createElement) ;", 9, align="g")
    texte(c, 268, 36, "2. les assembler (append), du plus petit au plus grand ;", 9, align="g")
    texte(c, 268, 22, "3. ajouter le li dans la liste : il apparaît à l’écran ;", 9, align="g")
    texte(c, 268, 8, "4. li.remove() le retire ; le compteur est recalculé.", 9, align="g")


# ---------------------------------------------------------------- TP8
def architecture_wp(c):
    boite(c, 6, 50, 92, 50, "Navigateur\ndu visiteur", fond=PALE, gras=True)
    boite(c, 170, 34, 170, 82, trait=BLEU)
    texte(c, 255, 103, "Serveur web", 9.5, True, BLEU)
    boite(c, 182, 44, 146, 50, "PHP\nWordPress assemble la page", taille=8.5, fond=PALE)
    boite(c, 410, 50, 94, 50, "Base de données\nMySQL / MariaDB", taille=8.5, fond=PALE, gras=True)
    fleche(c, 100, 84, 168, 84)
    texte(c, 134, 89, "requête", 8.5)
    fleche(c, 168, 62, 100, 62)
    texte(c, 134, 49, "page HTML", 8.5)
    fleche(c, 342, 84, 408, 84)
    fleche(c, 408, 62, 342, 62)
    texte(c, 375, 89, "lit, écrit", 8.5)
    texte(c, 375, 49, "contenus", 8.5)
    bloc(c, 170, 6, 82, 22, "Thème : apparence", 8)
    bloc(c, 258, 6, 82, 22, "Extension : fonction", 8)
    bloc(c, 410, 6, 94, 22, "Pages, articles, réglages", 7.5)


def structure_wp(c):
    texte(c, 10, 142, "Menu", 9.5, True, BLEU, "g")
    pages = ["Accueil", "Programme", "Contact", "Actualités"]
    for i, p in enumerate(pages):
        x = 10 + i * 78
        boite(c, x, 106, 70, 24, p, taille=8.5, fond=PALE, gras=True)
        fleche(c, x + 35, 140, x + 35, 132, largeur=0.8)
    c.setStrokeColor(MARINE)
    c.setLineWidth(0.8)
    c.line(45, 140, 279, 140)
    texte(c, 10, 86, "Réglages > Lecture :", 8.5, True, GRIS, "g")
    texte(c, 10, 73, "Accueil = page d’accueil statique", 8.5, couleur=GRIS, align="g")
    texte(c, 10, 60, "Actualités = page des articles", 8.5, couleur=GRIS, align="g")
    for i, a in enumerate(["Article 1", "Article 2"]):
        x = 196 + i * 90
        boite(c, x, 34, 78, 24, a, taille=8.5)
        fleche(c, 279, 104, x + 39, 60, BLEU, 0.8)
    for i, a in enumerate(["Catégorie A", "Catégorie B"]):
        x = 196 + i * 90
        boite(c, x, 0, 78, 20, a, taille=8, fond=PALE)
        fleche(c, x + 39, 33, x + 39, 21, BLEU, 0.8)
    texte(c, 390, 118, "Page : contenu stable, hors du fil", 8.5, align="g")
    texte(c, 390, 105, "d’actualités (Contact, Programme).", 8.5, align="g")
    texte(c, 390, 44, "Article : contenu daté, classé", 8.5, align="g")
    texte(c, 390, 31, "dans une catégorie.", 8.5, align="g")


# ---------------------------------------------------------------- TP9
def administration_wp(c):
    texte(c, 8, 136, "Éditeur de site : zones", 9.5, True, BLEU, "g")
    boite(c, 8, 8, 130, 118, trait=GRIS)
    bloc(c, 13, 96, 120, 25, "En-tête\n(site, navigation)", 7.5)
    bloc(c, 13, 38, 120, 54, "Contenu de la page\n(blocs)", fond=white)
    bloc(c, 13, 13, 120, 21, "Pied de page", 7.5)
    texte(c, 165, 136, "Rôles : du moins au plus de droits", 9.5, True, BLEU, "g")
    roles = [("Abonné", 50), ("Contributeur", 80), ("Auteur", 110), ("Éditeur", 140), ("Administrateur", 170)]
    for i, (r, w) in enumerate(roles):
        y = 106 - i * 23
        c.setFillColor(BLEU if r != "Éditeur" else MARINE)
        c.rect(165, y, w, 18, stroke=0, fill=1)
        texte(c, 170, y + 5.5, r, 8.5, True, white, "g")
    texte(c, 360, 136, "Cycle de maintenance", 9.5, True, BLEU, "g")
    etapes = ["Sauvegarder", "Mettre à jour", "Tester", "Documenter"]
    for i, e in enumerate(etapes):
        y = 102 - i * 31
        boite(c, 372, y, 110, 22, e, taille=8.5, fond=PALE)
        if i < 3:
            fleche(c, 427, y - 1, 427, y - 8)
    c.setStrokeColor(MARINE)
    c.setLineWidth(1)
    c.line(483, 20, 498, 20)
    c.line(498, 20, 498, 113)
    fleche(c, 498, 113, 484, 113, largeur=1)


def choix_formulaire(c):
    cx, cy = 92, 44
    p = c.beginPath()
    for k, (dx, dy) in enumerate([(-84, 0), (0, 36), (84, 0), (0, -36)]):
        (p.moveTo if k == 0 else p.lineTo)(cx + dx, cy + dy)
    p.close()
    c.setFillColor(white)
    c.setStrokeColor(BLEU)
    c.drawPath(p, stroke=1, fill=1)
    texte(c, cx, cy + 2, "Extension", 8.5, True)
    texte(c, cx, cy - 9, "autorisée ?", 8.5, True)
    fleche(c, 177, 58, 222, 66)
    texte(c, 196, 69, "oui", 8.5, True)
    fleche(c, 177, 30, 222, 22)
    texte(c, 196, 12, "non", 8.5, True)
    boite(c, 224, 52, 128, 32, "Installer l’extension\net créer le formulaire", taille=8.5, fond=PALE)
    boite(c, 224, 6, 128, 32, "Formulaire de démonstration,\nindiqué comme non connecté", taille=8, fond=PALE)
    fleche(c, 353, 68, 385, 50)
    fleche(c, 353, 22, 385, 40)
    boite(c, 387, 26, 118, 38, "Tester avec des données\nfictives, documenter\ndans la fiche", taille=8, fond=PALE)


# ---------------------------------------------------------------- TP10
def comportement_filtre(c):
    activites = [("Concert 1", "concert"), ("Atelier 1", "atelier"), ("Rencontre 1", "rencontre"),
                 ("Concert 2", "concert"), ("Atelier 2", "atelier"), ("Rencontre 2", "rencontre")]
    for x, choix, n in [(8, "Toutes", 6), (278, "Concert", 2)]:
        w = 224
        texte(c, x + w / 2, 168, f"Choix : {choix}", 9.5, True, BLEU)
        boite(c, x, 4, w, 158, trait=GRIS)
        boite(c, x + 8, 136, 110, 20, f"{choix}  v", taille=8.5)
        texte(c, x + 124, 142, "select", 8, couleur=GRIS, align="g")
        texte(c, x + 8, 120, f"{n} activités visibles", 9, True, align="g")
        ligne = 0
        for t, k in activites:
            if choix == "Toutes" or k == choix.lower():
                bloc(c, x + 8, 96 - ligne * 18, w - 16, 15, t, fond=PALE)
                ligne += 1
    fleche(c, 236, 84, 274, 84)


def relations_wp(c):
    boite(c, 8, 30, 130, 30, "Page\nInformations pratiques", taille=8.5, fond=PALE)
    fleche(c, 140, 45, 178, 45)
    texte(c, 159, 50, "ajouter", 8)
    boite(c, 180, 30, 80, 30, "Menu", fond=PALE, gras=True)
    boite(c, 290, 30, 90, 30, "Catégorie\nActualités", taille=8.5, fond=PALE)
    fleche(c, 416, 45, 382, 45)
    texte(c, 399, 50, "affecter", 8)
    boite(c, 418, 30, 86, 30, "Article\nfourni", taille=8.5)
    texte(c, 255, 8, "Vérifier ensuite le résultat en navigation privée.", 9, couleur=GRIS)


# ---------------------------------------------------------------- Atelier IA
def cycle_ia(c):
    etapes = [("Demander", "avec un contexte\net des contraintes"), ("Lire", "comprendre chaque\nligne reçue"),
              ("Tester", "tests T1 à T6,\nclavier, 375 px"), ("Corriger", "à la main, ou par\nune demande ciblée")]
    for i, (titre, detail) in enumerate(etapes):
        x = 6 + i * 128
        boite(c, x, 30, 106, 54, fond=PALE)
        texte(c, x + 53, 68, titre, 10, True, BLEU)
        for k, ligne in enumerate(detail.split("\n")):
            texte(c, x + 53, 54 - k * 11, ligne, 8.5)
        if i < 3:
            fleche(c, x + 108, 57, x + 126, 57)
    c.setStrokeColor(MARINE)
    c.setLineWidth(1.2)
    c.line(443, 30, 443, 14)
    c.line(443, 14, 59, 14)
    fleche(c, 59, 14, 59, 28)
    texte(c, 251, 2, "Recommencer jusqu’à ce que tous les tests passent, puis noter ce qui a été fait dans le journal.", 8.5, couleur=GRIS)


# ---------------------------------------------------------------- Documents enseignant
def frise(c):
    for i in range(10):
        ev = i in (4, 9)
        x = 2 + i * 51
        fond = MARINE if ev else PALE
        boite(c, x, 18, 47, 26, f"TP{i + 1}", fond=fond, trait=MARINE if ev else BLEU, couleur=white if ev else TEXTE, gras=True)
    for x1, x2, t in [(2, 200, "HTML et CSS"), (257, 353, "JavaScript"), (359, 508, "WordPress")]:
        c.setStrokeColor(BLEU)
        c.line(x1, 12, x2, 12)
        texte(c, (x1 + x2) / 2, 1, t, 8.5, True, BLEU)
    texte(c, 255, 50, "En foncé : les évaluations (TP5 et TP10)", 8.5, couleur=GRIS)


def instances_wp(c):
    boite(c, 10, 12, 92, 34, "TP8", fond=PALE, gras=True)
    fleche(c, 104, 29, 146, 29)
    texte(c, 125, 34, "conserver", 8)
    boite(c, 148, 12, 92, 34, "TP9", fond=PALE, gras=True)
    texte(c, 125, 52, "Instance de TP (une par personne)", 8.5, True, BLEU)
    boite(c, 320, 12, 110, 34, "TP10", fond=MARINE, trait=MARINE, couleur=white, gras=True)
    texte(c, 375, 52, "Nouvelle instance d’évaluation", 8.5, True, BLEU)


def capture(nom, largeur_cm):
    chemin = CAPTURES / nom
    w, h = PILImage.open(chemin).size
    l = largeur_cm * cm
    return Image(str(chemin), width=l, height=l * h / w)


EXEMPLE = "Exemple de résultat, une solution parmi d’autres."

# Par sujet : schémas placés avant le travail demandé, puis exemples placés après.
FIGURES = {
    "01": dict(avant=[(Schema(98, client_serveur), "Le navigateur demande une page, le serveur répond."),
                      (Schema(118, anatomie_url), "Anatomie d’une URL et d’un élément HTML.")],
               apres=[(capture("tp01.png", 8), EXEMPLE)]),
    "02": dict(avant=[(Schema(142, arborescence_squelette), "Fichiers, structure commune et navigation entre les pages."),
                      (Schema(58, lien_label), "Relier un label à son champ.")],
               apres=[(capture("tp02.png", 9), f"{EXEMPLE} Sans CSS, le rendu reste volontairement simple.")]),
    "03": dict(avant=[(Schema(162, modele_boite), "Le modèle de boîte et la spécificité des sélecteurs.")],
               apres=[(capture("tp03.png", 15), EXEMPLE)]),
    "04": dict(avant=[(Schema(196, responsive_ocean), "Disposition attendue sur grand écran et sur mobile.")],
               apres=[(capture("tp04.png", 16), f"{EXEMPLE} Rendu sur grand écran.")]),
    "05": dict(apres=[(Schema(226, maquette_forum), "Maquette de principe : l’organisation est imposée, le style est libre.")]),
    "06": dict(avant=[(Schema(116, etats_js), "Les deux comportements à programmer.")],
               apres=[(capture("tp06.png", 15), f"{EXEMPLE} Extrait en mode nuit.")]),
    "07": dict(avant=[(Schema(104, logique_formulaire), "Ce qui se passe à l’envoi du formulaire."),
                      (Schema(92, arbre_dom), "Structure DOM d’une tâche.")],
               apres=[(capture("tp07.png", 13), f"{EXEMPLE} Deux tâches et l’erreur de saisie vide.")]),
    "08": dict(avant=[(Schema(122, architecture_wp), "Comment WordPress produit une page."),
                      (Schema(154, structure_wp), "Le site à construire : menu, pages, articles et catégories.")]),
    "09": dict(avant=[(Schema(150, administration_wp), "Zones de l’éditeur de site, rôles et maintenance.")],
               apres=[(Schema(90, choix_formulaire), "Démarche pour le formulaire de l’étape 3.")]),
    "IA": dict(apres=[(Schema(90, cycle_ia), "La méthode : ne jamais s’arrêter à la première réponse.")]),
    "10": dict(apres=[(Schema(182, comportement_filtre), "Partie A : comportement attendu, style libre."),
                      (Schema(66, relations_wp), "Partie B : les liens à établir.")]),
}

SCHEMAS_DOCS = {"frise": (Schema(62, frise), "Progression des 10 séances."),
                "instances": (Schema(66, instances_wp), "Quelle instance pour quelle séance.")}
