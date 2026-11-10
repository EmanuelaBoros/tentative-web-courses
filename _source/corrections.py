"""Contenu des archives de correction (et des fichiers de départ du TP10)."""

SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="180" viewBox="0 0 400 180">\n'
    '  <rect width="400" height="180" fill="#d9f2ff"/>\n'
    '  <path d="M0 100 Q50 40 100 100 T200 100 T300 100 T400 100 V180 H0Z" fill="#2474a7"/>\n'
    '</svg>\n'
)

PAGES = [("index.html", "Accueil"), ("apropos.html", "À propos"), ("contact.html", "Contact")]


def nav(actif):
    """Menu commun : le lien de la page courante porte aria-current et un texte en gras."""
    lignes = ['      <nav aria-label="Navigation principale">', "        <ul>"]
    for fichier, libelle in PAGES:
        if fichier == actif:
            lignes.append(
                f'          <li><a href="{fichier}" aria-current="page"><strong>{libelle}</strong></a></li>'
            )
        else:
            lignes.append(f'          <li><a href="{fichier}">{libelle}</a></li>')
    lignes += ["        </ul>", "      </nav>"]
    return "\n".join(lignes)


def page(titre, corps, actif=None, css=False, script=False, marque="Ocean Fest",
         pied="Ocean Fest - Site pédagogique fictif"):
    lien = '  <link rel="stylesheet" href="styles.css">\n' if css else ""
    js = '  <script src="script.js" defer></script>\n' if script else ""
    menu = nav(actif) + "\n" if actif else ""
    return (
        "<!doctype html>\n"
        '<html lang="fr">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{titre}</title>\n"
        f"{lien}{js}"
        "</head>\n"
        "<body>\n"
        "  <header>\n"
        '    <div class="container">\n'
        f'      <p class="marque"><strong>{marque}</strong></p>\n'
        f"{menu}"
        "    </div>\n"
        "  </header>\n"
        "  <main>\n"
        f"{corps.rstrip()}\n"
        "  </main>\n"
        f"  <footer>{pied}</footer>\n"
        "</body>\n"
        "</html>\n"
    )


HTML_TP01 = """<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ocean Fest - Festival culturel à La Rochelle</title>
</head>
<body>
  <h1>Ocean Fest</h1>
  <p>Le festival culturel de l’océan à La Rochelle.</p>

  <h2>Programme</h2>
  <ul>
    <li>Concerts</li>
    <li>Ateliers</li>
    <li>Rencontres</li>
  </ul>

  <h2>Notre lieu</h2>
  <p>Au bord de l’océan Atlantique.</p>
  <img src="images/ocean.svg" width="360" height="162" alt="Vagues stylisées représentant l’océan">
  <p><a href="https://www.larochelle.fr/">Ville de La Rochelle</a></p>
</body>
</html>
"""

def corps_accueil(id_carte=False, interactions=False):
    attr = ' id="carte-phare"' if id_carte else ""
    bloc = ""
    if interactions:
        bloc = """
    <section>
      <h2>Interactions</h2>
      <button type="button" id="theme">Mode nuit</button>
      <button type="button" id="artiste">Voir le prochain artiste</button>
      <p id="sortie" aria-live="polite">Prêt !</p>
    </section>"""
    return f"""    <h1>Ocean Fest</h1>
    <p>Un festival culturel dédié à l’océan, à la musique et à la rencontre.</p>

    <section>
      <h2>Prochains événements</h2>
      <ul>
        <li>Concert d’ouverture sur le port</li>
        <li>Atelier de création en matériaux recyclés</li>
        <li>Rencontre avec des scientifiques de l’océan</li>
      </ul>
    </section>

    <section>
      <h2>Au programme</h2>
      <div class="cards">
        <article class="card"{attr}>
          <h3>Concerts</h3>
          <p>Des artistes au bord de l’Atlantique.</p>
        </article>
        <article class="card">
          <h3>Ateliers</h3>
          <p>Créer et apprendre ensemble.</p>
        </article>
        <article class="card">
          <h3>Rencontres</h3>
          <p>Échanger autour de l’océan.</p>
        </article>
      </div>
    </section>

    <section>
      <h2>Horaires</h2>
      <table>
        <thead>
          <tr><th scope="col">Activité</th><th scope="col">Heure</th></tr>
        </thead>
        <tbody>
          <tr><td>Atelier</td><td>14h</td></tr>
          <tr><td>Concert</td><td>18h</td></tr>
        </tbody>
      </table>
    </section>

    <section>
      <h2>Notre lieu</h2>
      <p>Au bord de l’océan Atlantique.</p>
      <img src="images/ocean.svg" width="360" height="162" alt="Vagues stylisées représentant l’océan">
      <p><a href="https://www.larochelle.fr/">Découvrir La Rochelle</a></p>
    </section>{bloc}
"""


CORPS_APROPOS = """    <h1>À propos</h1>
    <p>Ocean Fest est un événement fictif conçu pour apprendre le développement web.</p>
    <h2>Nos valeurs</h2>
    <ul>
      <li>Créativité</li>
      <li>Accessibilité</li>
      <li>Partage</li>
    </ul>
"""

CORPS_CONTACT = """    <h1>Contact</h1>
    <p>Ce formulaire est une démonstration : aucun message n’est envoyé ni enregistré.</p>
    <form action="#" method="get">
      <p>
        <label for="nom">Nom</label>
        <input id="nom" name="nom" type="text" autocomplete="name" required>
      </p>
      <p>
        <label for="email">Courriel</label>
        <input id="email" name="email" type="email" autocomplete="email" required>
      </p>
      <p>
        <label for="sujet">Sujet</label>
        <select id="sujet" name="sujet">
          <option>Programme</option>
          <option>Accès</option>
        </select>
      </p>
      <p>
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="4" required></textarea>
      </p>
      <button type="submit">Tester le formulaire (démonstration)</button>
    </form>
"""


def site(css=False, id_carte=False, interactions=False):
    return {
        "index.html": page("Ocean Fest - Accueil", corps_accueil(id_carte, interactions),
                           "index.html", css, interactions),
        "apropos.html": page("Ocean Fest - À propos", CORPS_APROPOS, "apropos.html", css),
        "contact.html": page("Ocean Fest - Contact", CORPS_CONTACT, "contact.html", css),
        "images/ocean.svg": SVG,
    }


CSS_TP03 = """/* TP3 - Mise en forme : couleurs, typographie et modèle de boîte.
   La disposition en colonnes et l'adaptation mobile arrivent au TP4. */

/* La largeur déclarée inclut padding et border. */
* {
  box-sizing: border-box;
}

/* Héritage : les éléments reçoivent la police et la couleur du body. */
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.6;
  color: #18304c;
  background: #f5f8fc;
}

a {
  color: #12639b;
}

h1,
h2,
h3 {
  line-height: 1.25;
}

/* En-tête et menu */
header {
  padding: 20px;
  color: #fff;
  background: #16365a;
}

header a {
  color: #fff;
}

.marque {
  margin: 0 0 8px;
}

nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

nav li {
  display: inline-block;
  margin-right: 16px;
}

nav a[aria-current="page"] {
  text-decoration-thickness: 3px;
}

main {
  padding: 24px;
}

/* Modèle de boîte : border = le trait, padding = l'espace intérieur,
   margin = l'espace extérieur qui sépare les cartes. */
.card {
  margin: 0 0 16px;
  padding: 18px;
  border: 1px solid #d7e1ed;
  border-radius: 10px;
  background: #fff;
}

/* Sélecteurs concurrents : les deux règles visent la première carte.
   L'id (1,0,0) l'emporte sur la classe (0,1,0), quel que soit leur ordre. */
.card {
  border-left: 6px solid #d7e1ed;
}

#carte-phare {
  border-left: 6px solid #12639b;
}

table {
  border-collapse: collapse;
  background: #fff;
}

th,
td {
  padding: 8px 12px;
  border: 1px solid #d7e1ed;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 4px;
}

input,
select,
textarea {
  display: block;
  width: 100%;
  padding: 10px;
}

button {
  padding: 11px 16px;
  border: 0;
  border-radius: 6px;
  color: #fff;
  background: #12639b;
  cursor: pointer;
}

button:hover {
  background: #164a71;
}

footer {
  padding: 16px;
  color: #fff;
  background: #16365a;
  text-align: center;
}
"""

CSS_TP04 = """/* TP4 - Interface responsive : la feuille du TP3 passe en rem
   et reçoit Flexbox, Grid, une largeur maximale et une media query. */

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.6;
  color: #18304c;
  background: #f5f8fc;
}

a {
  color: #12639b;
}

h1,
h2,
h3 {
  line-height: 1.25;
}

/* L'image ne dépasse jamais de son conteneur. */
img {
  max-width: 100%;
  height: auto;
}

/* Le focus reste visible pour tous les éléments interactifs. */
a:focus-visible,
button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: 3px solid #b45309;
  outline-offset: 2px;
}

header {
  padding: 1.25rem;
  color: #fff;
  background: #16365a;
}

header a {
  color: #fff;
}

header a:focus-visible {
  outline-color: #f3a923;
}

/* Zone centrale commune à l'en-tête et au contenu */
.container,
main {
  width: 100%;
  max-width: 67.5rem;
  margin-inline: auto;
}

/* Flexbox : la marque à gauche, le menu à droite. */
.container {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem 1.5rem;
}

.marque {
  margin: 0;
}

nav ul {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

/* Une cible d'au moins 2.75rem (44 px) reste facile à toucher. */
nav a {
  display: block;
  min-height: 2.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 0.25rem;
}

nav a[aria-current="page"] {
  text-decoration-thickness: 3px;
}

main {
  padding: 1.5rem;
}

/* Grid : trois colonnes de même largeur. */
.cards {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

.card {
  padding: 1.125rem;
  border: 1px solid #d7e1ed;
  border-left: 6px solid #d7e1ed;
  border-radius: 0.625rem;
  background: #fff;
}

#carte-phare {
  border-left: 6px solid #12639b;
}

table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
}

th,
td {
  padding: 0.5rem 0.75rem;
  border: 1px solid #d7e1ed;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 0.25rem;
}

input,
select,
textarea {
  display: block;
  width: 100%;
  padding: 0.625rem;
  font: inherit;
}

button {
  min-height: 2.75rem;
  margin: 0.25rem 0.25rem 0.25rem 0;
  padding: 0.625rem 1rem;
  border: 0;
  border-radius: 0.375rem;
  font: inherit;
  color: #fff;
  background: #12639b;
  cursor: pointer;
}

button:hover {
  background: #164a71;
}

footer {
  padding: 1rem;
  color: #fff;
  background: #16365a;
  text-align: center;
}

/* Jusqu'à 700 px : une colonne et un menu empilé. */
@media (max-width: 700px) {
  .cards {
    grid-template-columns: 1fr;
  }

  nav ul {
    flex-direction: column;
    gap: 0.25rem;
  }

  main {
    padding: 0.875rem;
  }
}
"""

CSS_NUIT = """
/* TP6 - Thème nuit, activé par la classe posée sur body. */
body.nuit {
  color: #ecf1f9;
  background: #0b1729;
}

body.nuit main a {
  color: #9fd3ff;
}

body.nuit .card {
  color: #fff;
  background: #152843;
}

body.nuit table {
  background: #152843;
}

body.nuit :focus-visible {
  outline-color: #f3a923;
}
"""

CSS_TP07 = """
/* TP7 - Message d'erreur et liste de tâches */
input {
  margin-bottom: 0.5rem;
}

#erreur {
  margin: 0.25rem 0;
  font-weight: bold;
  color: #a4161a;
}

#liste li {
  margin-bottom: 0.5rem;
}
"""

JS_TP06 = """"use strict";

const artistes = ["Ariane", "Bastien", "Camille"];
let indice = 0;
let nuit = false;

const boutonTheme = document.querySelector("#theme");
const boutonArtiste = document.querySelector("#artiste");
const sortie = document.querySelector("#sortie");

function basculerTheme() {
  nuit = !nuit;
  document.body.classList.toggle("nuit", nuit);
  if (nuit) {
    boutonTheme.textContent = "Mode jour";
  } else {
    boutonTheme.textContent = "Mode nuit";
  }
}

function afficherArtiste() {
  sortie.textContent = `Prochain artiste : ${artistes[indice]}`;
  indice = indice + 1;
  if (indice === artistes.length) {
    indice = 0;
  }
}

boutonTheme.addEventListener("click", basculerTheme);
boutonArtiste.addEventListener("click", afficherArtiste);

console.log(`Script chargé : ${artistes.length} artistes`);
"""

CORPS_TP07 = """    <h1>Préparer le festival</h1>
    <form id="formulaire" novalidate>
      <label for="tache">Nouvelle tâche</label>
      <input id="tache" name="tache" type="text" aria-describedby="erreur">
      <button type="submit">Ajouter</button>
      <p id="erreur" role="alert"></p>
    </form>
    <p id="compteur" aria-live="polite">0 tâche</p>
    <ul id="liste"></ul>
"""

JS_TP07 = """"use strict";

const form = document.querySelector("#formulaire");
const champ = document.querySelector("#tache");
const liste = document.querySelector("#liste");
const erreur = document.querySelector("#erreur");
const compteur = document.querySelector("#compteur");

function actualiserCompteur() {
  const n = liste.children.length;
  compteur.textContent = `${n} tâche${n > 1 ? "s" : ""}`;
}

function supprimerTache(li) {
  li.remove();
  actualiserCompteur();
  // Le bouton cliqué a disparu : on replace le focus pour l'usage au clavier.
  champ.focus();
}

function ajouterTache(nom) {
  const li = document.createElement("li");
  const texte = document.createElement("span");
  texte.textContent = `${nom} `;

  const bouton = document.createElement("button");
  bouton.type = "button";
  bouton.textContent = "Supprimer";
  bouton.setAttribute("aria-label", `Supprimer la tâche : ${nom}`);
  bouton.addEventListener("click", () => supprimerTache(li));

  li.append(texte, bouton);
  liste.append(li);
}

form.addEventListener("submit", (evt) => {
  evt.preventDefault();
  const nom = champ.value.trim();

  if (nom === "") {
    erreur.textContent = "Saisissez une tâche.";
    champ.setAttribute("aria-invalid", "true");
    champ.focus();
    return;
  }

  erreur.textContent = "";
  champ.removeAttribute("aria-invalid");
  ajouterTache(nom);
  actualiserCompteur();
  champ.value = "";
  champ.focus();
});
"""

ACTIVITES = """    <ul id="activites">
      <li data-type="concert">Concert acoustique</li>
      <li data-type="atelier">Atelier recyclage</li>
      <li data-type="rencontre">Conférence océan</li>
      <li data-type="concert">Jazz sur le port</li>
      <li data-type="atelier">Atelier dessin</li>
      <li data-type="rencontre">Table ronde</li>
    </ul>
"""

CORPS_TP10_DEPART = "    <h1>Programme du festival</h1>\n" + ACTIVITES

CORPS_TP10 = """    <h1>Programme du festival</h1>
    <label for="filtre">Type d’activité</label>
    <select id="filtre">
      <option value="tous">Toutes</option>
      <option value="concert">Concert</option>
      <option value="atelier">Atelier</option>
      <option value="rencontre">Rencontre</option>
    </select>
    <p id="compteur" aria-live="polite"></p>
""" + ACTIVITES

JS_TP10 = """"use strict";

const filtre = document.querySelector("#filtre");
const activites = Array.from(document.querySelectorAll("#activites [data-type]"));
const compteur = document.querySelector("#compteur");

function actualiser() {
  const type = filtre.value;
  let nombre = 0;

  activites.forEach((activite) => {
    const visible = type === "tous" || activite.dataset.type === type;
    activite.hidden = !visible;
    if (visible) {
      nombre = nombre + 1;
    }
  });

  const pluriel = nombre > 1 ? "s" : "";
  compteur.textContent = `${nombre} activité${pluriel} affichée${pluriel}`;
}

filtre.addEventListener("change", actualiser);
actualiser();
"""

CORPS_TP05 = """    <section class="intro">
      <h1>Forum des métiers du numérique</h1>
      <p>Découvrez trois métiers qui construisent les usages numériques.</p>
    </section>

    <section id="metiers" aria-labelledby="titre-metiers">
      <h2 id="titre-metiers">Les métiers présentés</h2>
      <div class="cartes">
        <article class="carte">
          <h3>Développeur web</h3>
          <p>Crée des applications et des interfaces. Teste leurs fonctionnalités.</p>
        </article>
        <article class="carte">
          <h3>UX Designer</h3>
          <p>Étudie les besoins des usagers. Améliore leur expérience.</p>
        </article>
        <article class="carte">
          <h3>Administrateur de systèmes</h3>
          <p>Maintient les équipements. Sécurise les services.</p>
        </article>
      </div>
    </section>

    <section id="contact" class="contact" aria-labelledby="titre-contact">
      <h2 id="titre-contact">Contact</h2>
      <p>Écrivez à <a href="mailto:contact@example.org">contact@example.org</a>.</p>
    </section>
"""

HTML_TP05 = (
    "<!doctype html>\n"
    '<html lang="fr">\n'
    "<head>\n"
    '  <meta charset="utf-8">\n'
    '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
    "  <title>Forum des métiers du numérique</title>\n"
    '  <link rel="stylesheet" href="styles.css">\n'
    "</head>\n"
    "<body>\n"
    "  <header>\n"
    "    <p><strong>Forum des métiers</strong></p>\n"
    '    <nav aria-label="Navigation principale">\n'
    '      <a href="#metiers">Métiers</a>\n'
    '      <a href="#contact">Contact</a>\n'
    "    </nav>\n"
    "  </header>\n"
    "  <main>\n"
    f"{CORPS_TP05.rstrip()}\n"
    "  </main>\n"
    "  <footer>Forum des métiers du numérique - Site pédagogique fictif</footer>\n"
    "</body>\n"
    "</html>\n"
)

# Feuille écrite pour l'épreuve : elle ne reprend pas celle du fil rouge.
CSS_TP05 = """/* Approche « mobile d'abord » : une colonne par défaut,
   trois colonnes à partir de 700 px. */

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.6;
  color: #2b2233;
  background: #fff;
}

a {
  color: #5b2a86;
}

a:focus-visible {
  outline: 3px solid #b45309;
  outline-offset: 2px;
}

/* En-tête centré */
header {
  padding: 1rem;
  border-bottom: 4px solid #5b2a86;
  text-align: center;
}

header p {
  margin: 0 0 0.5rem;
  font-size: 1.25rem;
}

nav a {
  display: inline-block;
  min-height: 2.75rem;
  padding: 0.5rem 1rem;
}

/* Bandeau d'introduction sur toute la largeur */
.intro {
  padding: 2rem 1rem;
  color: #fff;
  background: #5b2a86;
  text-align: center;
}

.intro h1 {
  margin: 0 0 0.5rem;
  line-height: 1.2;
}

#metiers {
  max-width: 70rem;
  margin: 0 auto;
  padding: 1.5rem 1rem;
}

.cartes {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

.carte {
  padding: 1rem;
  border-top: 6px solid #5b2a86;
  background: #f4eff8;
}

.carte h3 {
  margin-top: 0;
}

/* Bloc contact distinct des cartes */
.contact {
  padding: 1.5rem 1rem;
  background: #f4eff8;
  text-align: center;
}

footer {
  padding: 1rem;
  color: #fff;
  background: #2b2233;
  text-align: center;
}

@media (min-width: 700px) {
  .cartes {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
"""

ENTETE_README = """# Correction {tp} — {titre}

Réservée aux enseignants jusqu’à la remise. Cette solution de référence n’est pas la seule possible.

"""


def readme(tp, titre, ouvrir, points):
    texte = ENTETE_README.format(tp=tp, titre=titre)
    if ouvrir:
        texte += f"Ouvrir `{ouvrir}` dans un navigateur récent ; aucune installation n’est nécessaire.\n\n"
    texte += "## À retenir\n" + "".join(f"- {p}\n" for p in points)
    return texte


REPONSES_TP01 = """# Réponses attendues aux questions du TP1

- **Navigateur (client) :** demande les ressources et affiche la page.
- **Serveur :** reçoit la requête HTTP(S) et renvoie les ressources demandées.
- **HTML / CSS / JavaScript :** structure et contenu / présentation / comportement.
- **HTTP et HTTPS :** même protocole d’échange, mais HTTPS chiffre la communication et authentifie le serveur.
- **Exemple d’URL `https://www.larochelle.fr/` :** le protocole est `https`, le nom de domaine `www.larochelle.fr` et le chemin `/`.

En ouvrant `index.html` directement, le navigateur lit un fichier local (`file://`) : aucun serveur n’intervient.
"""

GUIDE_TP08 = """# Guide de correction WordPress — TP8

État attendu sur l’instance individuelle de l’étudiant ou de l’étudiante. Les libellés peuvent varier selon la version et le thème.

## Étapes
1. Réglages > Général : saisir « Ocean Fest » comme titre du site.
2. Pages : créer et publier Accueil, Programme, Contact et Actualités.
3. Articles > Catégories : créer « Actualités » et « Programme ».
4. Articles : publier « Ouverture des inscriptions » (Actualités) et « Programme dévoilé » (Programme).
5. Réglages > Lecture : choisir une page d’accueil statique, Accueil, et Actualités comme page des articles.
6. Réglages > Permaliens : vérifier que le format « Titre de la publication » est sélectionné.
7. Apparence > Éditeur (thème de blocs) ou Apparence > Menus (thème classique) : placer les quatre pages dans la navigation.
8. Tester en navigation privée : les pages et les deux articles s’affichent.

Une page et une catégorie peuvent porter le même nom « Actualités » : leurs adresses restent distinctes.

## Contenus à copier
- Accueil : « Bienvenue à Ocean Fest, festival culturel fictif à La Rochelle. »
- Programme : « Concerts, ateliers et rencontres autour de l’océan. »
- Contact : « Contact de démonstration : aucun formulaire de cette formation n’envoie de données réelles. »
- Actualités : laisser le contenu vide, WordPress y affiche les articles.

## Réponses attendues dans la fiche
- **PHP :** génère les pages côté serveur à chaque requête.
- **MySQL/MariaDB :** stocke contenus, comptes et réglages.
- **Thème :** définit l’apparence du site.
- **Extension :** ajoute des fonctionnalités.
- **Contenu et administration :** le contenu est ce que voit le public ; l’administration (`/wp-admin`) sert à le gérer.
"""

GUIDE_TP09 = """# Guide de correction WordPress — TP9

Ce TP part de l’état final du TP8, sur la même instance individuelle.

## État attendu
1. Thème : un thème de blocs actif et une palette cohérente, avec un contraste lisible.
2. Apparence > Éditeur : en-tête avec le nom du site et la navigation ; pied de page personnalisé.
3. Formulaire : extension autorisée, testée avec des données fictives. Sinon, formulaire de démonstration indiqué comme non connecté, et choix documenté dans la fiche.
4. Vérifications : un seul titre de niveau 1 par page, hiérarchie logique, textes alternatifs renseignés, permaliens lisibles, version mobile utilisable.
5. Compte : un compte Éditeur fictif, seulement si autorisé. Justification attendue : ce rôle gère les contenus sans administrer le site (moindre privilège).
6. Fiche de maintenance : voir `FICHE_MAINTENANCE_MODELE.md`.

## SEO de base
Un titre de site explicite, des titres de page clairs, des permaliens lisibles et des textes alternatifs suffisent à ce niveau.

## Points de vigilance
- Aucun mot de passe visible dans les captures.
- Aucune donnée personnelle réelle dans les tests du formulaire.
- Une modification des permaliens doit être suivie d’un nouveau test des liens du menu.
"""

FICHE_MAINT = """# Fiche de maintenance modèle
- **Mises à jour :** vérifier régulièrement cœur, thème et extensions, après test sur une copie du site.
- **Sauvegarde :** fichiers et base de données, avec un essai de restauration.
- **Comptes :** droits minimaux, mots de passe robustes, suppression des comptes inutiles.
- **Extensions :** limiter les installations ; vérifier leur source et leur maintenance.
- **Accessibilité :** titres logiques, navigation au clavier, textes alternatifs.
"""

GRILLE_TP08 = """Critère;Attendu
Titre du site;Ocean Fest
Pages;4 pages publiées : Accueil, Programme, Contact, Actualités
Articles;2 articles publiés
Catégories;2 catégories utilisées : Actualités, Programme
Lecture;Accueil en page statique, Actualités en page des articles
Navigation;4 pages accessibles depuis le menu en mode visiteur
Fiche;Fiche de réalisation complète, sans identifiant visible
"""

GRILLE_TP09 = """Critère;Attendu
Identité;Thème de blocs actif, palette cohérente et lisible
En-tête et pied de page;Personnalisés, navigation présente
Formulaire;Extension testée avec des données fictives, ou démonstration documentée
Accessibilité;Titres hiérarchisés, textes alternatifs, version mobile utilisable
Permaliens;Lisibles, liens du menu fonctionnels après vérification
Compte;Compte Éditeur fictif justifié, si autorisé
Maintenance;Fiche complète : mises à jour, sauvegarde, comptes, extensions
Captures;Aucun identifiant ni mot de passe visible
"""

GUIDE_TP10 = """# Correction de la partie WordPress (enseignant)

Prérequis : instance préparée selon `00_Guide_enseignant_WordPress.pdf`.

1. Pages : créer et publier « Informations pratiques » avec un titre et un texte (accès fictif par exemple).
2. Articles > Catégories : créer « Actualités ».
3. Articles : affecter « Actualités » à l’article « Bilan de la dernière édition ».
4. Ajouter « Informations pratiques » au menu de navigation.
5. Vérifier en mode visiteur et joindre les captures, sans identifiant visible.

Adapter le barème si une limite de l’instance a empêché une action.
"""

BAREME_TP05 = """Barème détaillé - Évaluation 1 (100 points)

HTML et sémantique - 30 points
  12  En-tête, navigation, main, section d'introduction, trois article, bloc contact, pied de page
   6  Un seul h1 et une hiérarchie de titres logique
   6  Navigation fonctionnelle vers les sections
   6  Doctype, lang, charset, viewport, title explicite

Styles et maquette - 30 points
   6  Feuille externe styles.css, sans style inline
   8  Palette et typographie cohérentes
   8  Cartes : padding, border, espacement maîtrisés
   8  Introduction et contact visuellement distincts des cartes

Responsive - 20 points
   8  Trois colonnes à partir de 700 px
   8  Une colonne sous 700 px
   4  Aucun défilement horizontal à 375 px et 1280 px

Qualité et accessibilité - 20 points
   6  Focus visible et navigation au clavier
   5  Contrastes lisibles
   5  Code valide et indenté
   4  Contenus originaux (deux phrases par métier), rendu ZIP conforme

Tests : vérifier à 375, 699, 700 et 1280 px.
"""

BAREME_TP10 = """Barème détaillé - Évaluation 2 (100 points)

Partie A - JavaScript et DOM - 60 points
  30  Filtre : select avec label, 4 options, écoute de change, seules les bonnes activités restent visibles
  20  Compteur : exact au chargement et à chaque changement (6, puis 2 pour chaque type)
  10  Qualité : script.js externe, code lisible, data-type non modifiés, console sans erreur

Partie B - WordPress - 30 points
  10  Page « Informations pratiques » publiée
  10  Catégorie « Actualités » créée et affectée à l'article fourni
  10  Page présente dans le menu, en mode visiteur

Livrables et tests - 10 points
   5  index.html, script.js et fiche déposés sous le nom demandé
   5  Captures du menu et de la catégorie, sans identifiant visible
"""


def _site_tp04():
    fichiers = site(css=True, id_carte=True)
    fichiers["styles.css"] = CSS_TP04
    return fichiers


def archives():
    """Renvoie {nom de zip relatif à la racine du kit: {chemin: contenu}}."""
    tp02 = site()
    tp03 = site(css=True, id_carte=True)
    tp06 = site(css=True, id_carte=True, interactions=True)

    return {
        "TP01/TP01_Correction.zip": {
            "index.html": HTML_TP01,
            "images/ocean.svg": SVG,
            "REPONSES_QUESTIONS.md": REPONSES_TP01,
            "README_CORRECTION.md": readme("TP1", "Comprendre le Web et créer une page HTML", "index.html", [
                "Le `alt` décrit ce que l’image apporte à la page.",
                "Un seul `h1`, puis des `h2` : les titres décrivent la structure, pas la taille du texte.",
                "Les réponses aux questions de cours sont dans `REPONSES_QUESTIONS.md`.",
            ]),
        },
        "TP02/TP02_Correction.zip": {
            **tp02,
            "README_CORRECTION.md": readme("TP2", "Structurer un site multipage en HTML", "index.html", [
                "Le lien actif combine `aria-current=\"page\"` (lecteurs d’écran) et `strong` (visible sans CSS).",
                "Le bouton de type `submit` déclenche la vérification des champs `required`.",
                "`method=\"get\"` place les valeurs dans l’URL : c’est visible après un test, donc utile pour observer. Un vrai formulaire de contact utiliserait POST et un traitement serveur.",
                "`action=\"#\"` reste sur la page : rien n’est envoyé, et le texte de la page le dit.",
                "Les classes `cards` et `card` servent de points d’accroche au TP3.",
            ]),
        },
        "TP03/TP03_Correction.zip": {
            **tp03,
            "styles.css": CSS_TP03,
            "README_CORRECTION.md": readme("TP3", "Mettre en forme un site avec CSS", "index.html", [
                "Volontairement sans Flexbox, Grid ni media query : ces notions sont le travail du TP4.",
                "Carte `.card` : `border` dessine le contour, `padding` éloigne le texte du contour, `margin` éloigne les cartes.",
                "Sélecteurs concurrents : `.card` et `#carte-phare` visent la première carte. L’id a la spécificité (1,0,0), la classe (0,1,0) : la bordure bleue s’applique, même si l’ordre des règles est inversé. À spécificité égale, la dernière règle gagne.",
                "Héritage : `color` et `font-family` posés sur `body` se transmettent ; `border` et `padding` ne se transmettent pas.",
                "Seul ajout HTML autorisé : l’attribut `id=\"carte-phare\"`.",
            ]),
        },
        "TP04/TP04_Correction.zip": {
            **_site_tp04(),
            "README_CORRECTION.md": readme("TP4", "Créer une interface responsive", "index.html", [
                "Flexbox gère une ligne (en-tête, menu) ; Grid gère une grille (les cartes).",
                "`rem` suit la taille de police choisie par l’utilisateur ; 1 rem vaut 16 px par défaut.",
                "`max-width` limite la zone centrale sur grand écran sans provoquer de débordement sur petit écran.",
                "`max-width: 700px` inclut 700 px : la page passe à une colonne jusqu’à cette largeur incluse.",
                "`img { max-width: 100%; }` évite le débordement de l’image à 375 px.",
                "Tester à 375 et 1280 px, puis parcourir la page avec Tab.",
            ]),
        },
        "TP05/TP05_Correction.zip": {
            "index.html": HTML_TP05,
            "styles.css": CSS_TP05,
            "BAREME.txt": BAREME_TP05,
            "README_CORRECTION.md": readme("évaluation 1", "HTML et CSS", "index.html", [
                "Ne pas distribuer avant l’épreuve.",
                "La mise en page et la feuille de style diffèrent volontairement du fil rouge Ocean Fest.",
                "`min-width: 700px` applique exactement la consigne : trois colonnes dès 700 px, une colonne à 699 px.",
                "Une `max-width: 699px` équivalente est correcte ; `max-width: 700px` donne un écart mineur à 700 px exactement, à ne pas pénaliser lourdement.",
            ]),
        },
        "TP06/TP06_Correction.zip": {
            **tp06,
            "styles.css": CSS_TP04 + CSS_NUIT,
            "script.js": JS_TP06,
            "README_CORRECTION.md": readme("TP6", "Découvrir JavaScript et les événements", "index.html", [
                "`defer` lance le script une fois le HTML analysé : `querySelector` trouve donc les éléments.",
                "`type=\"button\"` garantit qu’un bouton ne soumet jamais de formulaire.",
                "Le booléen `nuit` et les deux conditions couvrent les notions du sujet. Une variante avec `classList.toggle` seul et `%` est aussi correcte.",
                "Erreur volontaire : avec `#themes`, `querySelector` renvoie `null`, et la console affiche `Cannot read properties of null (reading 'addEventListener')`. Lire le numéro de ligne, puis corriger le sélecteur.",
                "Le thème nuit redéfinit la couleur des liens : le bleu d’origine serait illisible sur fond sombre.",
            ]),
        },
        "TP07/TP07_Correction.zip": {
            "index.html": page("Ocean Fest - Tâches", CORPS_TP07, css=True, script=True),
            "styles.css": CSS_TP04 + CSS_TP07,
            "script.js": JS_TP07,
            "README_CORRECTION.md": readme("TP7", "Manipuler le DOM et valider un formulaire", "index.html", [
                "`trim()` refuse une saisie composée uniquement d’espaces.",
                "`textContent` affiche la saisie comme du texte, sans l’interpréter comme du HTML.",
                "L’erreur est annoncée par `role=\"alert\"`, reliée au champ par `aria-describedby` et signalée par `aria-invalid`.",
                "Supprimer un élément qui a le focus renvoie le focus au début de la page : on le replace donc sur le champ.",
                "`liste.children.length` donne un compteur toujours exact, sans variable à synchroniser.",
            ]),
        },
        "TP08/TP08_Correction.zip": {
            "GUIDE_CORRECTION_WORDPRESS.md": GUIDE_TP08,
            "GRILLE_VALIDATION.csv": GRILLE_TP08,
            "README_CORRECTION.md": readme("TP8", "Découvrir WordPress et publier du contenu", None, [
                "Cette correction décrit un état attendu : elle ne contient pas d’installation WordPress.",
                "Commencer par `GUIDE_CORRECTION_WORDPRESS.md`, puis contrôler avec `GRILLE_VALIDATION.csv`.",
                "Préparation des instances : voir `00_Guide_enseignant_WordPress.pdf`.",
            ]),
        },
        "TP09/TP09_Correction.zip": {
            "GUIDE_CORRECTION_WORDPRESS.md": GUIDE_TP09,
            "GRILLE_VALIDATION.csv": GRILLE_TP09,
            "FICHE_MAINTENANCE_MODELE.md": FICHE_MAINT,
            "README_CORRECTION.md": readme("TP9", "Personnaliser et administrer WordPress", None, [
                "Cette correction décrit un état attendu : elle ne contient pas d’installation WordPress.",
                "Commencer par `GUIDE_CORRECTION_WORDPRESS.md`, puis contrôler avec `GRILLE_VALIDATION.csv`.",
                "`FICHE_MAINTENANCE_MODELE.md` donne un exemple de fiche attendue.",
            ]),
        },
        "TP10/TP10_Correction.zip": {
            "index.html": page("Ocean Fest - Programme", CORPS_TP10, css=True, script=True),
            "styles.css": CSS_TP04,
            "script.js": JS_TP10,
            "BAREME.txt": BAREME_TP10,
            "GUIDE_CORRECTION_WORDPRESS.md": GUIDE_TP10,
            "README_CORRECTION.md": readme("évaluation 2", "JavaScript et WordPress", "index.html", [
                "Ne pas distribuer avant l’épreuve.",
                "Le `select` peut être écrit en HTML ou créé en JavaScript : les deux sont acceptés.",
                "`hidden` masque l’activité sans la retirer du DOM ; `classList` avec une classe CSS est aussi correct.",
                "Tester : 6 activités au chargement, 2 pour chaque type, puis 6 avec « Toutes ».",
            ]),
        },
        "TP10/TP10_Fichiers_depart.zip": {
            "index.html": page("Ocean Fest - Programme", CORPS_TP10_DEPART, css=True, script=True),
            "styles.css": CSS_TP04,
            "script.js": "// Évaluation 2 : écrire ici le code du filtre et du compteur.\n",
            "README.txt": (
                "Ouvrir index.html dans un navigateur.\n"
                "Compléter index.html et script.js selon le sujet, sans modifier les valeurs data-type.\n"
            ),
        },
    }
