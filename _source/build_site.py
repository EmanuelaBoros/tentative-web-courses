"""Génère le site public du cours dans ../site à partir de sujets.py.

Usage : python build_site.py   après build.py (le site copie les PDF et les ZIP).

Le site est destiné à être public : par défaut, il ne contient ni correction, ni
sujet d'évaluation, ni fichier de départ du TP10. Modifier les réglages ci-dessous
pour les libérer au fil du semestre, puis relancer ce script.
"""
import html
import re
import shutil
from pathlib import Path

from atelier_ia import ATELIER
from sujets import DEROULE, REGLE_EVAL, REPARTITION, SUJETS

# ------------------------------------------------------------- À ajuster
SUJETS_EVALUATION_PUBLIES = set()  # par exemple {"05"}, après l'épreuve
CORRECTIONS_PUBLIEES = set()       # par exemple {"01", "02"}, après chaque remise
DEPART_TP10_PUBLIE = False         # True le jour de l'épreuve
DATES = {}                         # par exemple {"01": "12 janvier 2027"}
ATELIER_IA_PUBLIE = True           # séance d'essai : sujet et fichiers de départ, jamais la correction
DATE_ATELIER_IA = ""               # par exemple "9 mars 2027"
MODE_PROPOSITION = True            # version de relecture : détail complet des séances et des évaluations (jamais les corrections)
# -------------------------------------------------------------------------

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
SITE = RACINE / "site"

MODULES = [
    ("html-css", "HTML et CSS", "Structurer une page, la mettre en forme et la rendre responsive.", ["01", "02", "03", "04", "05"]),
    ("javascript", "JavaScript", "Réagir aux actions de l’utilisateur et modifier la page.", ["06", "07"]),
    ("wordpress", "WordPress", "Publier du contenu et administrer un site, puis tout évaluer.", ["08", "09", "10"]),
]
PAR_NUM = {s["num"]: s for s in SUJETS}


def en_html(texte):
    """Échappe le texte et convertit `code` en balises code."""
    morceaux = re.split(r"`([^`]*)`", texte)
    sortie = "".join(f"<code>{html.escape(m)}</code>" if i % 2 else html.escape(m, quote=False)
                     for i, m in enumerate(morceaux))
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", sortie)


def titre_court(s):
    return re.sub(r"^ÉVALUATION \d+ - ", "", s["titre"])


def liens(s):
    num = s["num"]
    evaluation = s.get("evaluation")
    sortie = []
    if not evaluation or num in SUJETS_EVALUATION_PUBLIES:
        sortie.append(f'<a class="bouton" href="tp/TP{num}_Sujet.pdf">Sujet (PDF)</a>')
    else:
        sortie.append('<span class="attente">Sujet remis le jour de l’épreuve</span>')
    if num == "10" and DEPART_TP10_PUBLIE:
        sortie.append('<a class="bouton secondaire" href="tp/TP10_Fichiers_depart.zip">Fichiers de départ (ZIP)</a>')
    if num in CORRECTIONS_PUBLIEES:
        sortie.append(f'<a class="bouton secondaire" href="tp/TP{num}_Correction.zip">Correction (ZIP)</a>')
    if num in ("08", "09", "10"):
        sortie.append('<a class="bouton secondaire" href="tp/Fiche_realisation_WordPress.pdf">Fiche de réalisation</a>')
    return "\n          ".join(sortie)


def liste(elements, ordonnee=False):
    balise = "ol" if ordonnee else "ul"
    return f"<{balise}>" + "".join(f"<li>{en_html(e)}</li>" for e in elements) + f"</{balise}>"


def details(s):
    blocs = [f"<h4>Objectifs</h4>{liste(s['objectifs'])}", f"<h4>Notions</h4><p>{en_html(s['notions'])}</p>"]
    if MODE_PROPOSITION:
        blocs.insert(0, f"<h4>Situation</h4><p>{en_html(s['situation'])}</p>")
        blocs.append(f"<h4>À préparer</h4><p>{en_html(s['prep'])}</p>")
        blocs.append(f"<h4>{'Déroulé de l’épreuve' if s.get('evaluation') else 'Travail demandé'}</h4>{liste(s['travail'], True)}")
        if s.get("cahier"):
            titre, lignes = s["cahier"]
            blocs.append(f"<h4>{en_html(titre)}</h4>{liste(lignes)}")
        blocs += [f"<h4>Contraintes</h4><p>{en_html(s['contraintes'])}</p>",
                  f"<h4>Critères d’évaluation</h4><p>{en_html(s['criteres'])}</p>",
                  f"<h4>À rendre</h4><p>{en_html(s['rendre'])}</p>"]
        if s.get("plus"):
            blocs.append(f"<h4>Pour aller plus loin</h4><p>{en_html(s['plus'])}</p>")
        return "".join(blocs)
    # Les évaluations non libérées ne donnent ni prérequis détaillés ni consigne de rendu.
    if not s.get("evaluation") or s["num"] in SUJETS_EVALUATION_PUBLIES:
        blocs += [f"<h4>À préparer</h4><p>{en_html(s['prep'])}</p>", f"<h4>À rendre</h4><p>{en_html(s['rendre'])}</p>"]
    return "".join(blocs)


def resume_carte(s):
    """Phrase visible sans déplier : le premier objectif."""
    return f'<p class="objectif">{en_html(s["objectifs"][0])}</p>' if MODE_PROPOSITION else ""


def tableau():
    lignes = REPARTITION[1:]
    corps = "".join(
        f'<tr><th scope="row"><a href="#tp{n}">{int(n)}</a></th><td>{en_html(t.replace("**", ""))}</td><td>{en_html(no)}</td></tr>'
        for n, t, no in lignes)
    return ('<div class="defilement"><table><thead><tr><th scope="col">TP</th><th scope="col">Séance</th>'
            f'<th scope="col">Notions principales</th></tr></thead><tbody>{corps}</tbody></table></div>')


def section_proposition():
    if not MODE_PROPOSITION:
        return ""
    comp = [b for b in DEROULE["blocs"] if b[0] == "ul"][2][1]
    return f"""    <section id="proposition">
      <h2>Proposition pédagogique</h2>
      <div class="deux">
        <div>
          <h3>Cadre</h3>
          <ul>
            <li><strong>Public :</strong> débutants découvrant le développement web.</li>
            <li><strong>Volume :</strong> 10 séances de 1h30, soit 15 h, dont deux évaluations (TP 5 et TP 10).</li>
            <li><strong>Fil rouge :</strong> Ocean Fest, un festival fictif à La Rochelle. Le TP 5 porte sur un autre sujet, pour évaluer sans que la correction donne la réponse.</li>
            <li><strong>Matériel :</strong> navigateur récent, VS Code, une instance WordPress par personne.</li>
          </ul>
        </div>
        <div>
          <h3>Déroulé type d’une séance</h3>
          <ol>
            <li>15 min de démonstration</li>
            <li>20 min d’exercice guidé</li>
            <li>45 min de travail autonome</li>
            <li>10 min de bilan</li>
          </ol>
          <p>Chaque séance repart du rendu précédent ou de sa correction, diffusée après la remise.</p>
        </div>
      </div>
      <h3>Compétences visées</h3>
      {liste(comp)}
      <h3>Répartition des séances</h3>
      {tableau()}
    </section>
"""


def section_diffusion():
    if not MODE_PROPOSITION:
        return ""
    return """    <section id="diffusion">
      <h2>Ressources et diffusion</h2>
      <div class="deux">
        <div>
          <h3>Pour chaque TP</h3>
          <ul>
            <li>Un <strong>sujet PDF</strong> remis aux étudiants, avec objectifs, travail pas à pas, critères et consignes de rendu.</li>
            <li>Un <strong>ZIP de correction</strong> réservé à l’enseignant, diffusé après la remise (guide, barème, grille de validation selon le TP).</li>
            <li>Pour les TP 8 à 10 : une <strong>fiche de réalisation WordPress</strong> à compléter, avec captures.</li>
          </ul>
        </div>
        <div>
          <h3>Côté enseignant</h3>
          <ul>
            <li>Un <strong>déroulé des 10 TP</strong> et un <strong>guide de préparation des instances WordPress</strong> (instance de TP, instance d’évaluation, contrôles avant séance).</li>
            <li>Les corrections des TP 5 et 10 ne sont diffusées qu’après toutes les sessions d’épreuve.</li>
            <li>Les fichiers de départ du TP 10 sont remis le jour de l’épreuve.</li>
          </ul>
        </div>
      </div>
    </section>
"""


def carte(s):
    num = s["num"]
    evaluation = s.get("evaluation")
    date = f'<span class="date">{html.escape(DATES[num])}</span>' if num in DATES else ""
    badge = '<span class="badge">Évaluation</span>' if evaluation else ""
    return f"""      <article class="carte{' evaluation' if evaluation else ''}" id="tp{num}">
        <p class="surtitre">TP {int(num)} · 1h30 · {html.escape(s["projet"])}{badge}{date}</p>
        <h3>{html.escape(titre_court(s))}</h3>
        {resume_carte(s)}
        <div class="liens">
          {liens(s)}
        </div>
        <details>
          <summary>{"Voir le détail de la séance" if MODE_PROPOSITION else "Objectifs et notions"}</summary>
          {details(s)}
        </details>
      </article>"""


def frise():
    cases = []
    for ancre, nom, _, nums in MODULES:
        for num in nums:
            ev = " evaluation" if PAR_NUM[num].get("evaluation") else ""
            titre = html.escape(titre_court(PAR_NUM[num]), quote=True)
            cases.append(f'<li class="{ancre}{ev}"><a href="#tp{num}" title="{titre}">{int(num)}</a></li>')
    return "\n        ".join(cases)


def section_atelier():
    date = f'<span class="date">{html.escape(DATE_ATELIER_IA)}</span>' if DATE_ATELIER_IA else ""
    return f"""    <section class="module" id="atelier-ia">
      <h2>Atelier IA</h2>
      <p class="resume">Une séance d’essai après le TP 7 : utiliser une IA pour créer une page, puis vérifier ce qu’elle produit.</p>
      <div class="grille">
      <article class="carte">
        <p class="surtitre">Atelier · 1h30<span class="badge">Essai, non noté</span>{date}</p>
        <h3>{html.escape(ATELIER["titre"].replace("Atelier IA : g", "G"))}</h3>
        <div class="liens">
          <a class="bouton" href="tp/Atelier_IA_Sujet.pdf">Sujet (PDF)</a>
          <a class="bouton secondaire" href="tp/Atelier_IA_Fichiers_depart.zip">Fichiers de départ (ZIP)</a>
        </div>
        <details>
          <summary>Objectifs et notions</summary>
          {details(ATELIER)}
        </details>
      </article>
      </div>
    </section>"""


def modules():
    sorties = []
    for ancre, nom, resume, nums in MODULES:
        cartes = "\n".join(carte(PAR_NUM[n]) for n in nums)
        large = " large" if MODE_PROPOSITION else ""
        sorties.append(f"""    <section class="module" id="{ancre}">
      <h2>{nom}</h2>
      <p class="resume">{resume}</p>
      <div class="grille{large}">
{cartes}
      </div>
    </section>""")
        # L'atelier se place après le TP 7, donc entre JavaScript et WordPress.
        if ancre == "javascript" and ATELIER_IA_PUBLIE:
            sorties.append(section_atelier())
    return "\n\n".join(sorties)


BANDEAU = ""

PAGE = """<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Développement web - La Rochelle Université</title>
  <meta name="description" content="Organisation du cours de développement web : 10 TP de HTML, CSS, JavaScript et WordPress.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="evitement" href="#contenu">Aller au contenu</a>
  <header class="entete">
    <div class="enveloppe">
      <a href="#haut" class="logo"><img src="assets/logo-la-rochelle-universite.png" width="96" height="96" alt="La Rochelle Université"></a>
      <nav aria-label="Navigation principale">
        <ul>
{lien_proposition}          <li><a href="#progression">Progression</a></li>
          <li><a href="#html-css">Séances</a></li>{lien_atelier}
          <li><a href="#evaluations">Évaluations</a></li>
{lien_diffusion}          <li><a href="#pratique">Infos pratiques</a></li>
        </ul>
      </nav>
    </div>
  </header>

{bandeau}
  <main id="contenu">
    <section class="ouverture" id="haut">
      <p class="surtitre">Cours et travaux pratiques</p>
      <h1>Développement web</h1>
      <p class="chapeau">De la première page HTML à l’administration d’un site WordPress, autour d’un projet fil rouge : Ocean Fest, un festival fictif à La Rochelle.</p>
      <dl class="chiffres">
        <div><dt>Séances</dt><dd>10</dd></div>
        <div><dt>Heures</dt><dd>15</dd></div>
        <div><dt>Évaluations</dt><dd>2</dd></div>
      </dl>
    </section>

{proposition}
    <section id="progression">
      <h2>Progression</h2>
      <ol class="frise">
        {frise}
      </ol>
      <ul class="legende">
        <li><span class="pastille html-css"></span>HTML et CSS</li>
        <li><span class="pastille javascript"></span>JavaScript</li>
        <li><span class="pastille wordpress"></span>WordPress</li>
        <li><span class="pastille evaluation"></span>Évaluation</li>
      </ul>
    </section>

{modules}

    <section id="evaluations">
      <h2>Évaluations</h2>
      <div class="deux">
        <div class="encadre">
          <h3>Évaluation 1 : HTML et CSS</h3>
          <p><strong>TP 5 · 40 % de la note.</strong> Créer une page responsive à partir d’un cahier des charges, sur un nouveau sujet.</p>
        </div>
        <div class="encadre">
          <h3>Évaluation 2 : JavaScript et WordPress</h3>
          <p><strong>TP 10 · 60 % de la note.</strong> 60 min de JavaScript, 25 min de WordPress et 5 min de remise.</p>
        </div>
      </div>
      <p>{regle}</p>
    </section>

{diffusion}
    <section id="pratique">
      <h2>Infos pratiques</h2>
      <div class="deux">
        <div>
          <h3>Matériel</h3>
          <ul>
            <li>Un navigateur récent et un éditeur de code (VS Code conseillé).</li>
            <li>Pour les TP 8 à 10 : une instance WordPress individuelle et ses identifiants, fournis pour le cours.</li>
          </ul>
        </div>
        <div>
          <h3>Rendus</h3>
          <ul>
            <li>Une archive nommée <code>TP05_NOM_Prenom.zip</code>, avec le numéro du TP.</li>
            <li>Pour WordPress, la <a href="tp/Fiche_realisation_WordPress.pdf">fiche de réalisation</a> (<a href="tp/Fiche_realisation_WordPress.md">version modifiable</a>).</li>
            <li>Jamais d’identifiant ni de mot de passe dans les captures.</li>
          </ul>
        </div>
      </div>
    </section>
  </main>

  <footer class="pied">
    <div class="enveloppe">
      <p>Assist. Prof. Emanuela Boros · <a href="mailto:emanuela.boros@univ-lr.fr">emanuela.boros@univ-lr.fr</a></p>
      <p><a href="https://emanuelaboros.github.io/courses/">Tous les cours</a> · La Rochelle Université</p>
    </div>
  </footer>
</body>
</html>
"""

CSS = """/* « Texte LRU » est dérivée de Raleway, avec des chiffres alignés (licence SIL OFL). */
@font-face {
  font-family: "Texte LRU";
  src: url("assets/TexteLRU-Regular.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}

@font-face {
  font-family: "Texte LRU";
  src: url("assets/TexteLRU-Bold.woff2") format("woff2");
  font-weight: 700;
  font-display: swap;
}

:root {
  --bleu: #0f6eb1;
  --marine: #00346b;
  --texte: #1f2933;
  --gris: #5f6b76;
  --filet: #c9d6e3;
  --pale: #eaf2f9;
  --js: #b45309;
  --wp: #2f6f4f;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 1rem;
}

body {
  margin: 0;
  font-family: "Texte LRU", Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--texte);
  background: #fff;
}

a {
  color: var(--bleu);
}

a:focus-visible,
summary:focus-visible {
  outline: 3px solid var(--marine);
  outline-offset: 2px;
}

code {
  font-size: 0.9em;
  color: var(--marine);
  overflow-wrap: anywhere;
}

h1,
h2,
h3,
h4 {
  line-height: 1.2;
  color: var(--marine);
}

h2 {
  margin: 0 0 0.5rem;
  font-size: 1.75rem;
}

h3 {
  margin: 0 0 0.75rem;
  font-size: 1.15rem;
}

h4 {
  margin: 0.9rem 0 0.2rem;
  font-size: 1rem;
  color: var(--bleu);
}

.evitement {
  position: absolute;
  left: -999rem;
}

.evitement:focus {
  left: 1rem;
  top: 1rem;
  padding: 0.5rem 1rem;
  background: #fff;
}

.enveloppe,
main > section {
  width: 100%;
  max-width: 68rem;
  margin-inline: auto;
  padding-inline: 1.5rem;
}

/* Le logo reste en haut à gauche, avec une marge en tête égale à la moitié de sa taille. */
.entete .enveloppe {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem 2rem;
  padding-block: 3rem 1rem;
}

.logo {
  display: block;
  line-height: 0;
}

.entete ul {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem 1.25rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.entete nav a {
  display: block;
  padding: 0.5rem 0;
  font-weight: 700;
  color: var(--marine);
  text-decoration: none;
}

.entete nav a:hover {
  text-decoration: underline;
}

main > section {
  padding-block: 2rem;
}

main > section.ouverture {
  padding-block: 1.5rem 2rem;
}

.surtitre {
  margin: 0 0 0.4rem;
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--bleu);
}

h1 {
  margin: 0 0 0.75rem;
  font-size: clamp(2.25rem, 6.5vw, 3.5rem);
}

.chapeau {
  max-width: 44rem;
  margin: 0 0 1.5rem;
  font-size: 1.2rem;
}

.chiffres {
  display: flex;
  flex-wrap: wrap;
  gap: 2.5rem;
  margin: 0;
}

.chiffres div {
  display: flex;
  flex-direction: column-reverse;
}

.chiffres dt {
  color: var(--gris);
}

.chiffres dd {
  margin: 0;
  font-size: 2.25rem;
  font-weight: 700;
  line-height: 1.1;
  color: var(--marine);
}

/* Frise des 10 séances */
.frise {
  display: grid;
  grid-template-columns: repeat(10, minmax(0, 1fr));
  gap: 0.375rem;
  margin: 1rem 0;
  padding: 0;
  list-style: none;
}

.frise a {
  display: block;
  padding: 0.75rem 0;
  border-top: 6px solid var(--couleur);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--marine);
  text-align: center;
  text-decoration: none;
  background: var(--pale);
}

.frise a:hover {
  text-decoration: underline;
}

.frise .evaluation a {
  color: #fff;
  background: var(--marine);
}

.html-css {
  --couleur: var(--bleu);
}

.javascript {
  --couleur: var(--js);
}

.wordpress {
  --couleur: var(--wp);
}

.legende {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem 1.25rem;
  margin: 0;
  padding: 0;
  font-size: 0.95rem;
  color: var(--gris);
  list-style: none;
}

.pastille {
  display: inline-block;
  width: 0.8rem;
  height: 0.8rem;
  margin-right: 0.4rem;
  background: var(--couleur);
}

.pastille.evaluation {
  background: var(--marine);
}

/* Séances */
.module h2 {
  padding-top: 1.25rem;
  border-top: 2px solid var(--filet);
}

.resume {
  margin: 0 0 1.25rem;
  color: var(--gris);
}

.grille {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 19rem), 1fr));
  gap: 1rem;
  align-items: start;
}

.carte {
  padding: 1.1rem;
  border: 1px solid var(--filet);
  border-radius: 0.5rem;
  scroll-margin-top: 1rem;
}

.carte.evaluation {
  border: 2px solid var(--marine);
}

.badge {
  margin-left: 0.5rem;
  padding: 0.05rem 0.45rem;
  border-radius: 0.25rem;
  font-size: 0.8rem;
  color: #fff;
  background: var(--marine);
}

.date {
  display: block;
  font-weight: 400;
  color: var(--gris);
}

.liens {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.bouton {
  display: inline-block;
  padding: 0.45rem 0.8rem;
  border: 2px solid var(--bleu);
  border-radius: 0.3rem;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
  background: var(--bleu);
}

.bouton:hover {
  border-color: var(--marine);
  background: var(--marine);
}

.bouton.secondaire {
  color: var(--bleu);
  background: #fff;
}

.bouton.secondaire:hover {
  color: var(--marine);
  border-color: var(--marine);
}

.attente {
  padding: 0.45rem 0;
  color: var(--gris);
}

summary {
  font-weight: 700;
  color: var(--marine);
  cursor: pointer;
}

details ul {
  margin: 0;
  padding-left: 1.2rem;
}

details p {
  margin: 0;
}

/* Évaluations et infos pratiques */
.deux {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 19rem), 1fr));
  gap: 1rem 2rem;
  margin-top: 1rem;
}

.encadre {
  padding: 1.1rem;
  border: 3px solid var(--bleu);
}

.encadre p {
  margin: 0;
}

.deux ul,
.deux ol,
#proposition > ul {
  margin: 0;
  padding-left: 1.2rem;
}

.pied {
  margin-top: 2rem;
  color: #fff;
  background: var(--marine);
}

.pied .enveloppe {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.25rem 2rem;
  padding-block: 1.25rem;
}

.pied p {
  margin: 0;
}

.pied a {
  color: #fff;
}

.pied a:focus-visible {
  outline-color: #fff;
}

/* Version de relecture */
.bandeau {
  margin: 0;
  padding: 0.6rem 1.5rem;
  font-size: 0.95rem;
  font-weight: 700;
  color: #fff;
  text-align: center;
  background: var(--js);
}

.grille.large {
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 32rem), 1fr));
}

.objectif {
  margin: 0 0 0.75rem;
}

details[open] summary {
  margin-bottom: 0.25rem;
}

details ol {
  margin: 0;
  padding-left: 1.4rem;
}

details li + li {
  margin-top: 0.25rem;
}

.defilement {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid var(--filet);
  text-align: left;
  vertical-align: top;
}

thead th {
  color: #fff;
  background: var(--marine);
}

tbody th a {
  font-weight: 700;
}

/* Sous cette largeur, la frise passe sur deux lignes de 5 pour rester lisible. */
@media (max-width: 34rem) {
  .frise {
    grid-template-columns: repeat(5, minmax(0, 1fr));
  }

  .enveloppe,
  main > section {
    padding-inline: 1rem;
  }
}
"""


def construire():
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)
    (SITE / "tp").mkdir()

    regle = html.escape(REGLE_EVAL.replace(" À adapter au règlement de l’établissement.", ""), quote=False)
    lien_atelier = '\n          <li><a href="#atelier-ia">Atelier IA</a></li>' if ATELIER_IA_PUBLIE else ""
    (SITE / "index.html").write_text(
        PAGE.format(
            frise=frise(), modules=modules(), regle=regle, lien_atelier=lien_atelier, proposition=section_proposition(),
            diffusion=section_diffusion(), bandeau=BANDEAU if MODE_PROPOSITION else "",
            lien_proposition='          <li><a href="#proposition">Proposition</a></li>\n' if MODE_PROPOSITION else "",
            lien_diffusion='          <li><a href="#diffusion">Ressources</a></li>\n' if MODE_PROPOSITION else ""), encoding="utf-8")
    (SITE / "styles.css").write_text(CSS, encoding="utf-8")

    assets = ICI / "assets"
    shutil.copy(assets / "logo-la-rochelle-universite.png", SITE / "assets")
    shutil.copy(assets / "LICENCE-police.txt", SITE / "assets")
    for graisse in ("Regular", "Bold"):
        shutil.copy(assets / "web" / f"TexteLRU-{graisse}.woff2", SITE / "assets")

    for s in SUJETS:
        num = s["num"]
        if not s.get("evaluation") or num in SUJETS_EVALUATION_PUBLIES:
            shutil.copy(RACINE / f"TP{num}" / f"TP{num}_Sujet.pdf", SITE / "tp")
    for num in CORRECTIONS_PUBLIEES:
        shutil.copy(RACINE / f"TP{num}" / f"TP{num}_Correction.zip", SITE / "tp")
    if DEPART_TP10_PUBLIE:
        shutil.copy(RACINE / "TP10" / "TP10_Fichiers_depart.zip", SITE / "tp")
    if ATELIER_IA_PUBLIE:
        shutil.copy(RACINE / "Atelier_IA" / "Atelier_IA_Sujet.pdf", SITE / "tp")
        shutil.copy(RACINE / "Atelier_IA" / "Atelier_IA_Fichiers_depart.zip", SITE / "tp")
    shutil.copy(RACINE / "Fiche_realisation_WordPress.pdf", SITE / "tp")
    shutil.copy(RACINE / "Fiche_realisation_WordPress.md", SITE / "tp")


if __name__ == "__main__":
    construire()
