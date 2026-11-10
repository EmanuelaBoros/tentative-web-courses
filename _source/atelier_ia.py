"""Séance d'essai « Atelier IA » : sujet, fichiers de départ et correction.

Le sujet de réservation est volontairement différent du filtre évalué au TP10.
"""
from corrections import CSS_TP04, SVG, page

ATELIER = dict(
    num="IA", titre="Atelier IA : générer, puis vérifier", projet="Ocean Fest",
    kicker="Développement web · Séance d’essai, non notée",
    objectifs=[
        "Repérer les défauts d’une page générée par une IA, même si elle semble correcte.",
        "Rédiger une demande précise et tester la réponse obtenue.",
        "Expliquer et assumer le code que l’on rend.",
    ],
    notions="Prompt, audit, tests, accessibilité, vérification des faits, responsabilité de l’auteur.",
    situation="L’équipe d’Ocean Fest a reçu une page générée par une IA et veut y ajouter la réservation des ateliers. Vous vérifiez, corrigez et complétez ce travail.",
    prep="Les TP1 à TP7 ; l’archive `Atelier_IA_Fichiers_depart.zip`. Outil conseillé, sans compte : Duck.ai. Sans accès ou sans souhait d’utiliser une IA, le dossier `secours/` contient des réponses enregistrées.",
    travail=[
        "**30 min, audit.** Ouvrir `audit/index.html` et lire `audit/BRIEF.md`. Avec `audit/GRILLE_AUDIT.md`, trouver au moins 8 défauts, puis en corriger au moins 5.",
        "**45 min, génération.** Lire `reservation/CONSIGNE.md`. Demander la page à l’IA, d’abord avec une demande vague, puis avec une demande précise. Passer les tests T1 à T6, corriger, et remplir `JOURNAL_IA.md` au fil de l’eau.",
        "**15 min, explication.** À deux, chacun choisit 5 lignes dans le code de l’autre. L’auteur ou l’autrice explique ce qu’elles font et comment il ou elle les a vérifiées.",
    ],
    cahier=("Règles de l’atelier", [
        "L’IA est autorisée dans cette séance uniquement. Elle reste interdite aux évaluations.",
        "Aucune donnée personnelle, aucun identifiant et aucun mot de passe dans une demande.",
        "Une réponse de l’IA peut être fausse, même si elle paraît sûre d’elle : vous restez responsable de ce que vous rendez.",
    ]),
    contraintes="Rendre uniquement du code que vous savez expliquer. Noter dans le journal tout ce qui vient de l’IA.",
    criteres="Défauts trouvés et corrigés, tests T1 à T6 réussis, journal honnête et précis, explication claire de vos lignes de code.",
    rendre="Un ZIP avec `audit/` corrigé, `reservation/` et `JOURNAL_IA.md` complété.",
)

BRIEF = """# Brief d'Ocean Fest

Seuls ces faits sont vrais. Tout autre fait présent sur la page est à vérifier.

- Ocean Fest est un festival culturel fictif, à La Rochelle.
- Il propose des concerts, des ateliers et des rencontres.
- Le site est pédagogique : aucune date, aucun tarif ni aucune fréquentation ne sont connus.
- Le formulaire de contact est une démonstration : il n'envoie rien et doit le dire.
"""

GRILLE_AUDIT = """# Grille d'audit

Pour chaque ligne : ce que vous avez observé, et le fichier concerné.

| À vérifier | Comment | Observation |
|---|---|---|
| Langue, viewport et titre de la page | Lire le `head` | |
| Balises sémantiques | Chercher `header`, `nav`, `main`, `footer` | |
| Hiérarchie des titres | Un seul `h1`, aucun niveau sauté | |
| Images | Texte alternatif pertinent | |
| Formulaire | Chaque `label` est relié à son champ | |
| Honnêteté du formulaire | Où partent les données ? Que dit la page ? | |
| Liens | Cliquer sur chacun | |
| Faits | Comparer le texte à `BRIEF.md` | |
| Petit écran | Mode responsive à 375 px : défilement horizontal ? | |
| Contraste | Tous les textes sont-ils bien lisibles ? | |
| Clavier | Parcourir avec Tab : le focus est-il visible ? | |
| Console | Ouvrir F12 : y a-t-il une erreur ? | |
| Saisie affichée | Saisir `<b>test</b>` comme nom : que se passe-t-il ? | |
"""

JOURNAL = """# Journal de l'atelier IA

Ne jamais y copier de donnée personnelle ni d'identifiant.

Outil utilisé (ou dossier `secours/`) :

## Audit
Défauts trouvés :

Défauts corrigés :

Le défaut le plus difficile à repérer, et pourquoi :

## Génération
Demande vague (copiée telle quelle) :

Ce qui manquait ou était faux dans la réponse :

Demande précise (copiée telle quelle) :

| Test | Réussi du premier coup ? | Ce que vous avez corrigé |
|---|---|---|
| T1 | | |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |
| T6 | | |

Ce que l'IA a inventé ou supposé sans que vous le demandiez :

## Bilan de la séance d'essai
Ce que l'IA vous a fait gagner :

Ce qu'elle vous a fait perdre, ou risquer de ne pas apprendre :

Cette séance devrait-elle rester dans le cours ? Pourquoi ?
"""

CONSIGNE = """# Consigne : réservation des ateliers

Créer une page qui permet de réserver une place dans un atelier. Tout reste dans le navigateur : rien n'est envoyé ni enregistré.

## Attendu
- Deux ateliers : Recyclage (2 places) et Dessin (1 place).
- Un formulaire : un nom (fictif), le choix de l'atelier et un bouton.
- Les places restantes de chaque atelier sont affichées.
- La liste des réservations s'affiche sur la page.

## Tests à passer
- **T1.** Au chargement, la page affiche 2 places pour Recyclage et 1 pour Dessin.
- **T2.** Une réservation valide retire une place et ajoute le nom à la liste.
- **T3.** Un nom vide ou composé d'espaces est refusé, avec un message visible.
- **T4.** Un atelier complet refuse la réservation : les places ne deviennent jamais négatives.
- **T5.** Le nom `<b>test</b>` s'affiche tel quel, sans passer en gras.
- **T6.** Tout fonctionne au clavier, et chaque champ a un `label` relié.
"""

PROMPT_VAGUE = "Fais-moi une page de réservation pour un festival."

PROMPT_PRECIS = """Je suis débutant en HTML, CSS et JavaScript. Écris une page en français, sans bibliothèque, avec le JavaScript dans une balise script.
Elle permet de réserver une place dans deux ateliers : Recyclage (2 places) et Dessin (1 place).
Formulaire : un nom, un select pour l'atelier, un bouton. Afficher les places restantes et la liste des réservations.
Rien n'est envoyé à un serveur. Commente brièvement le code."""

# Réponses enregistrées : la première oublie presque tout, la seconde échoue à T3 et T5.
REPONSE_VAGUE = """<!-- Demande : """ + PROMPT_VAGUE + """ -->
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Réservation</title>
</head>
<body>
  <h1>Réservez votre pass festival !</h1>
  <p>Du 12 au 14 juillet. Pass 3 jours : 89 €.</p>
  Nom : <input id="nom"><br>
  E-mail : <input id="email"><br>
  Carte bancaire : <input id="carte"><br>
  <button onclick="reserver()">Payer et réserver</button>
  <script>
    function reserver() {
      alert("Merci " + document.getElementById("nom").value + ", votre pass est réservé !");
    }
  </script>
</body>
</html>
"""

REPONSE_PRECISE = """<!-- Demande :
""" + PROMPT_PRECIS + """
-->
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Réservation des ateliers</title>
</head>
<body>
  <h1>Réservation des ateliers</h1>
  <p>Recyclage : <span id="places-recyclage">2</span> places</p>
  <p>Dessin : <span id="places-dessin">1</span> place</p>

  <form id="formulaire">
    <label for="nom">Nom</label>
    <input id="nom" type="text">
    <label for="atelier">Atelier</label>
    <select id="atelier">
      <option value="recyclage">Recyclage</option>
      <option value="dessin">Dessin</option>
    </select>
    <button type="submit">Réserver</button>
  </form>
  <p id="message"></p>
  <ul id="reservations"></ul>

  <script>
    // Nombre de places restantes par atelier
    const places = { recyclage: 2, dessin: 1 };

    document.querySelector("#formulaire").addEventListener("submit", (evt) => {
      evt.preventDefault();
      const nom = document.querySelector("#nom").value;
      const atelier = document.querySelector("#atelier").value;
      const message = document.querySelector("#message");

      if (nom === "") {
        message.textContent = "Saisissez un nom.";
        return;
      }
      if (places[atelier] === 0) {
        message.textContent = "Cet atelier est complet.";
        return;
      }

      // On retire une place et on ajoute la réservation
      places[atelier] = places[atelier] - 1;
      document.querySelector(`#places-${atelier}`).textContent = places[atelier];
      document.querySelector("#reservations").innerHTML += `<li>${nom} : ${atelier}</li>`;
      message.textContent = "Réservation enregistrée.";
    });
  </script>
</body>
</html>
"""

AUDIT_HTML = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Accueil</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="conteneur">
    <div class="haut">
      <div class="logo">Ocean Fest</div>
      <div class="menu">
        <a href="index.html">Accueil</a>
        <a href="programme.html">Programme</a>
        <a href="#contact">Contact</a>
      </div>
    </div>

    <h1>Ocean Fest</h1>
    <h1>Le festival de l’océan</h1>
    <p>Depuis 2009, Ocean Fest réunit plus de 40 000 festivaliers à La Rochelle, du 2 au 4 juillet. L’entrée est gratuite.</p>
    <img src="images/ocean.svg" width="400" height="180">

    <h4>Au programme</h4>
    <div class="cartes">
      <div class="carte"><h5>Concerts</h5><p>Des artistes au bord de l’Atlantique.</p></div>
      <div class="carte"><h5>Ateliers</h5><p>Créer et apprendre ensemble.</p></div>
      <div class="carte"><h5>Rencontres</h5><p>Échanger autour de l’océan.</p></div>
    </div>

    <h4 id="contact">Contact</h4>
    <p>Votre message sera transmis à notre équipe sous 24 heures.</p>
    <form id="formulaire" action="https://billetterie-oceanfest.example/envoyer" method="post">
      <label>Nom</label>
      <input id="nom" name="nom">
      <label>Message</label>
      <textarea name="message"></textarea>
      <button type="submit">Envoyer</button>
    </form>
    <p id="merci"></p>
    <div class="bas">Ocean Fest</div>
  </div>
  <script src="script.js"></script>
</body>
</html>
"""

AUDIT_CSS = """body {
  margin: 0;
  font-family: Arial, sans-serif;
  color: #18304c;
  background: #fff;
}

.conteneur {
  width: 1100px;
  margin: 0 auto;
}

.haut {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  color: #fff;
  background: #16365a;
}

.menu a {
  margin-left: 16px;
  color: #fff;
}

a:focus,
button:focus,
input:focus,
textarea:focus {
  outline: none;
}

.cartes {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.carte {
  padding: 18px;
  border: 1px solid #d7e1ed;
}

.carte p {
  color: #a7b4c2;
}

label,
input,
textarea {
  display: block;
  margin-bottom: 8px;
}

button {
  padding: 10px 16px;
  color: #fff;
  background: #12639b;
  border: 0;
}

.bas {
  margin-top: 24px;
  padding: 16px;
  color: #fff;
  background: #16365a;
  text-align: center;
}
"""

AUDIT_JS = """const formulaire = document.querySelector("#formulaire");

formulaire.addEventListener("submit", (evt) => {
  evt.preventDefault();
  const nom = document.querySelector("#nom").value;
  document.querySelector("#merci").innerHTML = "Merci " + nom + " !";
});

// Affiche le nombre de visiteurs du jour
document.querySelector("#visiteurs").textContent = "1 204 visiteurs aujourd’hui";
"""

CORPS_AUDIT_CORRIGE = """    <h1>Ocean Fest</h1>
    <p>Un festival culturel fictif à La Rochelle : concerts, ateliers et rencontres.</p>
    <img src="images/ocean.svg" width="400" height="180" alt="Vagues stylisées représentant l’océan">

    <section>
      <h2>Au programme</h2>
      <div class="cards">
        <article class="card">
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

    <section id="contact">
      <h2>Contact</h2>
      <p>Ce formulaire est une démonstration : aucun message n’est envoyé ni enregistré.</p>
      <form id="formulaire">
        <p>
          <label for="nom">Nom</label>
          <input id="nom" name="nom" type="text">
        </p>
        <p>
          <label for="message">Message</label>
          <textarea id="message" name="message"></textarea>
        </p>
        <button type="submit">Tester le formulaire</button>
      </form>
      <p id="merci" aria-live="polite"></p>
    </section>
"""

JS_AUDIT_CORRIGE = """const formulaire = document.querySelector("#formulaire");

formulaire.addEventListener("submit", (evt) => {
  evt.preventDefault();
  const nom = document.querySelector("#nom").value.trim();
  // textContent affiche la saisie comme du texte, sans l'interpréter comme du HTML.
  document.querySelector("#merci").textContent = `Merci ${nom} !`;
});
"""

CORPS_RESERVATION = """    <h1>Réservation des ateliers</h1>
    <p>Démonstration : rien n’est envoyé ni enregistré. Utilisez un nom fictif.</p>
    <ul>
      <li>Recyclage : <span id="places-recyclage">2</span> place(s)</li>
      <li>Dessin : <span id="places-dessin">1</span> place(s)</li>
    </ul>

    <form id="formulaire" novalidate>
      <p>
        <label for="nom">Nom fictif</label>
        <input id="nom" name="nom" type="text" aria-describedby="message">
      </p>
      <p>
        <label for="atelier">Atelier</label>
        <select id="atelier" name="atelier">
          <option value="recyclage">Recyclage</option>
          <option value="dessin">Dessin</option>
        </select>
      </p>
      <button type="submit">Réserver</button>
    </form>
    <p id="message" role="status"></p>

    <h2>Réservations</h2>
    <ul id="reservations"></ul>
"""

JS_RESERVATION = """"use strict";

const places = { recyclage: 2, dessin: 1 };

const formulaire = document.querySelector("#formulaire");
const champNom = document.querySelector("#nom");
const choixAtelier = document.querySelector("#atelier");
const message = document.querySelector("#message");
const reservations = document.querySelector("#reservations");

function ajouterReservation(nom, atelier) {
  places[atelier] = places[atelier] - 1;
  document.querySelector(`#places-${atelier}`).textContent = places[atelier];

  const ligne = document.createElement("li");
  ligne.textContent = `${nom} : ${choixAtelier.selectedOptions[0].textContent}`;
  reservations.append(ligne);
}

formulaire.addEventListener("submit", (evt) => {
  evt.preventDefault();
  const nom = champNom.value.trim();
  const atelier = choixAtelier.value;

  if (nom === "") {
    message.textContent = "Saisissez un nom.";
    champNom.focus();
    return;
  }
  if (places[atelier] === 0) {
    message.textContent = "Cet atelier est complet.";
    return;
  }

  ajouterReservation(nom, atelier);
  message.textContent = "Réservation enregistrée.";
  champNom.value = "";
  champNom.focus();
});
"""

GUIDE = """# Guide enseignant : Atelier IA (séance d'essai)

Réservé aux enseignants. Séance non notée, à placer après le TP7.

## Avant la séance
- Vérifier le règlement de l'établissement sur les outils d'IA.
- Tester Duck.ai depuis le réseau de la salle : ses limites d'usage ne sont pas publiées, et de nombreuses demandes depuis une même adresse peuvent être limitées. Prévoir de travailler à deux si besoin.
- Rappeler qu'aucun étudiant n'est obligé d'utiliser une IA : le dossier `secours/` permet de faire toute la séance sans compte ni connexion.

## Les 12 défauts de `audit/`
La page a été générée par une IA, puis des défauts y ont été ajoutés. Elle est volontairement présentable.

| # | Défaut | Où | Correction |
|---|---|---|---|
| 1 | Pas de `lang` | `index.html` | `<html lang="fr">` |
| 2 | Pas de balise viewport | `index.html` | Ajouter la balise |
| 3 | Titre de page vague (`Accueil`) | `index.html` | Titre explicite |
| 4 | Des `div` à la place de `header`, `nav`, `main`, `footer` | `index.html` | Balises sémantiques |
| 5 | Deux `h1`, puis des `h4` et `h5` | `index.html` | Un `h1`, puis `h2`, `h3` |
| 6 | Image sans `alt` | `index.html` | Texte alternatif |
| 7 | `label` non reliés aux champs | `index.html` | `for` et `id` |
| 8 | Faits inventés : 2009, 40 000 festivaliers, dates, gratuité, 1 204 visiteurs, réponse sous 24 heures | `index.html`, `script.js` | Retirer ; s'en tenir à `BRIEF.md` |
| 9 | Formulaire trompeur, avec un service d'envoi inventé | `index.html` | Dire que c'est une démonstration, retirer `action` |
| 10 | Lien cassé vers `programme.html` et largeur fixe de 1100 px (débordement à 375 px) | `index.html`, `styles.css` | Retirer le lien ; `max-width` |
| 11 | Texte des cartes peu contrasté, focus supprimé | `styles.css` | Couleur plus sombre ; retirer `outline: none` |
| 12 | Erreur en console (`#visiteurs` absent), et `innerHTML` avec une saisie | `script.js` | Retirer la ligne ; `textContent` |

Trouver 8 défauts suffit. Les faits inventés (8) et le formulaire trompeur (9) sont les plus instructifs, car aucun outil ne les signale : le code est valide, mais le contenu est faux.

## Réponses de secours
- `secours/reponse_demande_vague.html` invente des dates et un tarif, et demande une carte bancaire. Elle échoue à tous les tests.
- `secours/reponse_demande_precise.html` paraît correcte et réussit T1, T2, T4 et T6. Elle échoue à T3 (pas de `trim`) et à T5 (`innerHTML`), ce qui montre l'intérêt de tester.

Les réponses réelles varient d'une IA et d'un essai à l'autre : corriger avec les tests, pas avec un modèle unique. `reservation/` donne une solution de référence.

## Pendant l'explication à deux
Si quelqu'un ne sait pas expliquer une ligne, l'inviter à la relire avec son binôme, ou à la réécrire plus simplement.

## Évaluer l'essai
- Observer : combien de défauts sont trouvés, et si les tests sont vraiment passés.
- Lire la partie « Bilan » des journaux.
- Décider si l'atelier mérite d'être intégré au cours, par exemple en le découpant entre le TP4 et le TP7.
"""


def fichiers_depart():
    return {
        "audit/index.html": AUDIT_HTML,
        "audit/styles.css": AUDIT_CSS,
        "audit/script.js": AUDIT_JS,
        "audit/images/ocean.svg": SVG,
        "audit/BRIEF.md": BRIEF,
        "audit/GRILLE_AUDIT.md": GRILLE_AUDIT,
        "reservation/CONSIGNE.md": CONSIGNE,
        "secours/LISEZ_MOI.txt": (
            "Réponses d'IA enregistrées, à utiliser sans compte ni connexion.\n"
            "Chaque fichier indique en tête la demande utilisée. Ouvrir, tester, comparer, corriger.\n"
        ),
        "secours/reponse_demande_vague.html": REPONSE_VAGUE,
        "secours/reponse_demande_precise.html": REPONSE_PRECISE,
        "JOURNAL_IA.md": JOURNAL,
    }


def fichiers_correction():
    return {
        "GUIDE_ENSEIGNANT.md": GUIDE,
        "audit_corrigee/index.html": page("Ocean Fest - Festival culturel fictif", CORPS_AUDIT_CORRIGE, css=True, script=True),
        "audit_corrigee/styles.css": CSS_TP04,
        "audit_corrigee/script.js": JS_AUDIT_CORRIGE,
        "audit_corrigee/images/ocean.svg": SVG,
        "reservation/index.html": page("Ocean Fest - Réservation des ateliers", CORPS_RESERVATION, css=True, script=True),
        "reservation/styles.css": CSS_TP04,
        "reservation/script.js": JS_RESERVATION,
    }
