"""Textes des sujets et documents PDF. Entre accents graves : code."""

FICHE = "`Fiche_realisation_WordPress`"
OCEAN = "Vous participez à la conception du site fictif « Ocean Fest », festival culturel à La Rochelle."
REGLE_EVAL = (
    "Épreuve individuelle. Ressources autorisées : documentation technique et notes personnelles. "
    "Corrigés des TP, collaboration et IA générative interdits. À adapter au règlement de l’établissement."
)

SUJETS = [
    dict(
        num="01", titre="Comprendre le Web et créer une page HTML", projet="Ocean Fest",
        objectifs=[
            "Expliquer le rôle du navigateur, du serveur, de HTML, CSS et JavaScript.",
            "Construire un document HTML5 valide avec titres, paragraphes, images et liens.",
            "Utiliser un éditeur et les outils de développement du navigateur.",
        ],
        notions="HTTP(S), URL, client/serveur, élément, balise, attribut, doctype, head/body, h1/h2, img, a, alt.",
        situation=OCEAN,
        prep="Ordinateur, éditeur de texte (VS Code conseillé), navigateur et dossier de travail.",
        travail=[
            "Créer le dossier `oceanfest/` avec `index.html` et un sous-dossier `images/`.",
            "Écrire le squelette HTML5 : `lang=\"fr\"`, charset UTF-8, balise viewport et titre explicite.",
            "Ajouter un `h1` « Ocean Fest », deux `h2`, une présentation et un programme de trois activités.",
            "Ajouter un lien vers un site extérieur et une image avec un texte alternatif pertinent.",
            "Ouvrir le fichier dans le navigateur, puis inspecter le titre, la console et les éléments avec F12.",
            "Dans `reponses.txt`, expliquer en quelques lignes le rôle du navigateur, du serveur, de HTML, CSS et JavaScript, puis la différence entre HTTP et HTTPS.",
        ],
        contraintes="Pas de framework ni de générateur de site. La page doit s’ouvrir en local.",
        criteres="Page lisible, `h1` unique, titres structurés, image avec `alt`, lien utilisable, réponses justes.",
        rendre="Le dossier `oceanfest/` compressé : `index.html`, `images/` et `reponses.txt`.",
        plus="Ajouter un élément HTML absent du sujet (`figure`, `time`, etc.) et justifier ce choix en deux phrases.",
    ),
    dict(
        num="02", titre="Structurer un site multipage en HTML", projet="Ocean Fest",
        objectifs=[
            "Employer des balises sémantiques et une navigation relative.",
            "Organiser trois fichiers HTML et leurs ressources.",
            "Construire un formulaire accessible sans traitement serveur.",
        ],
        notions="header, nav, main, section, article, footer, ul/li, label, input, textarea, méthodes GET/POST (notions), liens relatifs.",
        situation=OCEAN,
        prep="Votre rendu du TP1 ou la correction du TP1 ; navigateur et éditeur.",
        travail=[
            "Réutiliser le dossier du TP1, en conservant l’image. Créer `apropos.html` et `contact.html`.",
            "Ajouter dans chaque page `header`, `nav`, `main` et `footer`.",
            "Créer un menu en liste avec des liens relatifs vers les trois pages. Indiquer le lien actif avec `aria-current=\"page\"` et un texte en gras (`strong`).",
            "Sur l’accueil : une liste `ul` des événements, un tableau de deux horaires et trois cartes `<article class=\"card\">` (titre et phrase) dans un `<div class=\"cards\">`.",
            "Sur `contact.html` : un formulaire avec nom, email, sujet, message et bouton. Relier chaque `label` à son champ et donner un `name` à chaque champ.",
            "Tester le bouton : les champs obligatoires vides sont signalés. Une fois remplis, observer les valeurs dans l’URL (GET).",
        ],
        contraintes="Le formulaire n’envoie rien : utiliser `action=\"#\"`, `method=\"get\"` et l’indiquer clairement sur la page.",
        criteres="Trois pages reliées, lien actif indiqué, HTML sémantique, formulaire avec labels, organisation claire.",
        rendre="Le dossier du site compressé : les trois pages HTML et `images/`.",
        plus="Expliquer en deux phrases pourquoi un vrai formulaire de contact utiliserait POST plutôt que GET.",
    ),
    dict(
        num="03", titre="Mettre en forme un site avec CSS", projet="Ocean Fest",
        objectifs=[
            "Relier une feuille de style externe aux pages.",
            "Employer sélecteurs, couleurs, polices et modèle de boîte.",
            "Comprendre la spécificité et la cascade.",
        ],
        notions="link rel=stylesheet, sélecteurs élément/classe/id, héritage, spécificité, margin, padding, border, box-sizing.",
        situation=OCEAN,
        prep="Votre rendu du TP2 ou la correction du TP2.",
        travail=[
            "Ajouter `styles.css` et le relier aux trois pages.",
            "Définir une palette et une typographie globale sur `body`, avec `box-sizing: border-box`.",
            "Styliser l’en-tête, le menu, les liens, les titres, les cartes et le pied de page.",
            "Utiliser `margin`, `padding` et `border` sur une carte, et commenter le rôle de chacun dans le CSS.",
            "Ajouter l’attribut `id=\"carte-phare\"` à une carte. Écrire deux règles concurrentes, une avec la classe et une avec l’id, puis expliquer dans un commentaire laquelle s’applique et pourquoi.",
        ],
        contraintes="Ne modifier ni les textes ni la structure HTML ; seul l’`id` de l’étape 5 s’ajoute. Pas de Flexbox, de Grid ni de media query : ils sont au programme du TP4.",
        criteres="Feuille CSS externe, styles cohérents, modèle de boîte maîtrisé, conflit de sélecteurs expliqué, aucun style inline.",
        rendre="Le dossier du site compressé, avec `styles.css`.",
        plus="Ajouter un état `:hover` sur les cartes et expliquer son effet en deux phrases.",
    ),
    dict(
        num="04", titre="Créer une interface responsive", projet="Ocean Fest",
        objectifs=[
            "Disposer des cartes avec CSS Grid et une navigation avec Flexbox.",
            "Mettre en œuvre des media queries pour mobile.",
            "Vérifier lisibilité, navigation au clavier et responsive.",
        ],
        notions="Flexbox, Grid, viewport, rem, %, max-width, @media, focus visible, responsive design.",
        situation=OCEAN,
        prep="Votre rendu du TP3 ou la correction du TP3 ; simulateur mobile du navigateur (F12).",
        travail=[
            "Disposer les 3 cartes événements sur trois colonnes avec CSS Grid.",
            "Réaliser une barre de navigation en Flexbox et une zone centrale limitée par `max-width`.",
            "Convertir les tailles de la feuille en `rem`.",
            "Écrire une media query à 700 px pour passer à une colonne et adapter la navigation.",
            "Tester à 375 px et 1280 px, sans défilement horizontal.",
            "Améliorer : état de focus visible, taille des liens, contraste. Vérifier la présence de la balise viewport et expliquer son rôle dans un commentaire.",
        ],
        contraintes="Rester compatible avec Firefox et Chrome récents, sans bibliothèque CSS.",
        criteres="Trois cartes en ligne sur grand écran et empilées sur mobile, aucun débordement, focus visible partout.",
        rendre="Le dossier du site compressé, avec `styles.css` mis à jour.",
        plus="Ajouter une deuxième étape à 2 colonnes pour les tablettes et la justifier en deux phrases. Vérifier le rendu au clavier.",
    ),
    dict(
        num="05", titre="ÉVALUATION 1 - HTML et CSS", projet="Forum des métiers du numérique", evaluation=True,
        objectifs=[
            "Mobiliser HTML sémantique et CSS, sans aide générative ni correction.",
            "Produire une interface conforme à un cahier des charges écrit.",
            "Déposer un rendu fonctionnel et organisé.",
        ],
        notions="HTML5, CSS externe, sémantique, responsive, fichiers cohérents et accessibles.",
        situation="Épreuve individuelle : un nouveau site, indépendant du projet Ocean Fest.",
        prep="Ce sujet, une machine et un éditeur configurés. Aucun fichier de départ. Vous rédigez les contenus.",
        travail=[
            "0-10 min : lire le cahier des charges et organiser les fichiers.",
            "10-70 min : construire la page.",
            "70-85 min : tester la version mobile, réparer les liens et les erreurs.",
            "85-90 min : déposer le dossier complet sous forme de ZIP.",
        ],
        cahier=("Cahier des charges : « Forum des métiers du numérique »", [
            "Fichiers : `index.html` et `styles.css` uniquement, sans JavaScript.",
            "Structure : en-tête avec navigation, section d’introduction, trois cartes métiers, bloc contact, pied de page.",
            "Métiers : Développeur web, UX Designer, Administrateur de systèmes, avec un contenu original de deux phrases chacun.",
            "Mise en page : en-tête centré ; introduction en bandeau coloré sur toute la largeur ; bloc contact visuellement distinct des cartes.",
            "Palette et typographie : différentes de celles du site Ocean Fest.",
            "Responsive : trois colonnes à partir de 700 px de large, une seule colonne sous 700 px, sans défilement horizontal.",
        ]),
        contraintes=REGLE_EVAL,
        criteres="Barème sur 100 : HTML et sémantique 30 ; styles et maquette 30 ; responsive 20 ; qualité et accessibilité 20.",
        rendre="Un ZIP contenant `index.html` et `styles.css`.",
    ),
    dict(
        num="06", titre="Découvrir JavaScript et les événements", projet="Ocean Fest",
        objectifs=[
            "Manipuler les variables, conditions, fonctions et événements.",
            "Brancher un fichier JavaScript externe et déboguer en console.",
            "Déclencher un changement de thème et un message.",
        ],
        notions="script defer, console.log, const/let, chaînes, booléens, conditions, fonctions, addEventListener.",
        situation=OCEAN,
        prep="Votre rendu du TP4 ou la correction du TP4 ; savoir ouvrir la console (F12).",
        travail=[
            "Créer `script.js` et le charger avec `defer` sur la page d’accueil.",
            "Afficher un message dans la console et déclarer un tableau de trois artistes.",
            "Ajouter un bouton « Mode nuit ». Écrire une fonction qui alterne une classe sur `body`, à l’aide d’un booléen et d’une condition qui adapte le texte du bouton.",
            "Ajouter une zone de message et un bouton « Voir le prochain artiste » : afficher successivement les trois noms, puis recommencer.",
            "Introduire volontairement une faute dans un sélecteur du script (par exemple `#theme` devient `#themes`). Lire l’erreur dans la console, noter sa signification en commentaire, puis corriger.",
            "Vérifier que les liens restent lisibles en mode nuit.",
        ],
        contraintes="Pas de bibliothèque JS. Les boutons sont de vrais `button` avec `type=\"button\"`, utilisables au clavier.",
        criteres="Thème opérationnel et lisible, cycle des artistes, fonctions, condition et écouteurs d’événements corrects.",
        rendre="Le dossier du site compressé, avec `script.js`.",
        plus="Ajouter une amélioration libre, la documenter en deux phrases et vérifier le rendu sur petit écran.",
    ),
    dict(
        num="07", titre="Manipuler le DOM et valider un formulaire", projet="Ocean Fest",
        objectifs=[
            "Sélectionner et modifier des nœuds du DOM.",
            "Gérer des événements utilisateur et une validation côté client.",
            "Ajouter et supprimer des tâches sans recharger la page.",
        ],
        notions="DOM, document.querySelector, createElement, append, remove, classList, preventDefault, trim.",
        situation=OCEAN + " Vous créez la liste de tâches de l’équipe, sur une page indépendante.",
        prep="Fonctions, événements et classes CSS vus au TP6. Vous pouvez réutiliser `styles.css` du TP4.",
        travail=[
            "Créer une page avec un formulaire de tâche (champ et bouton) et une liste vide.",
            "Écouter `submit`, empêcher le rechargement et vérifier que le champ n’est pas vide, avec `trim()`.",
            "Créer un élément `li` avec un bouton « Supprimer », puis l’ajouter à la liste.",
            "Ajouter un compteur de tâches, à jour après chaque ajout et suppression.",
            "Afficher une erreur accessible (`role=\"alert\"`) si le champ est vide.",
            "Tout tester au clavier. Après une suppression, le focus doit revenir sur le champ.",
        ],
        contraintes="La validation côté navigateur ne remplace jamais une validation côté serveur en production.",
        criteres="Ajout et suppression de tâches, compteur exact, saisies vides refusées, erreur annoncée, focus maîtrisé.",
        rendre="Le dossier compressé : la page HTML, `styles.css` et `script.js`.",
        plus="Ajouter un bouton « Tout supprimer » et documenter son comportement en deux phrases.",
    ),
    dict(
        num="08", titre="Découvrir WordPress et publier du contenu", projet="Ocean Fest",
        objectifs=[
            "Expliquer le rôle de PHP, du serveur et de la base de données dans WordPress.",
            "Créer pages, articles, catégories et menu via le tableau de bord.",
            "Différencier thème, extension, contenu et administration.",
        ],
        notions="CMS, WordPress, hébergement, PHP, MySQL/MariaDB, page, article, catégorie, thème, extension, URL permaliens.",
        situation=OCEAN,
        prep="Votre instance WordPress individuelle, déjà installée. Les identifiants et l’URL sont fournis par l’enseignant.",
        travail=[
            "Vous connecter à votre instance et donner au site le titre « Ocean Fest » (Réglages > Général).",
            "Créer et publier les pages Accueil, Programme, Contact et Actualités.",
            "Créer deux catégories et publier deux articles, chacun dans une catégorie.",
            "Définir Accueil comme page d’accueil statique et Actualités comme page des articles (Réglages > Lecture). Vérifier le format des permaliens.",
            "Configurer la navigation vers les quatre pages et vérifier le site en navigation privée.",
            "Dans la fiche, expliquer le rôle de PHP et de la base de données, et la différence entre thème, extension, contenu et administration.",
        ],
        contraintes="Ne pas installer de serveur. Conservez cette instance : elle sert aussi au TP9.",
        criteres="Pages et articles publiés, page d’accueil configurée, menu fonctionnel, catégories présentes, réponses justes.",
        rendre=f"La fiche {FICHE} complétée et des captures, sans identifiant ni mot de passe visible.",
        plus="Ajouter une image à un article avec un texte alternatif pertinent, et vérifier le site sur petit écran.",
    ),
    dict(
        num="09", titre="Personnaliser et administrer WordPress", projet="Ocean Fest",
        objectifs=[
            "Configurer navigation, thème, blocs, formulaire et rôles.",
            "Appliquer de bonnes pratiques de sécurité, sauvegarde et SEO.",
            "Documenter les paramétrages du site.",
        ],
        notions="Thèmes blocs, modèles, menus, extensions, rôles, maintenance, sauvegarde, formulaire, SEO.",
        situation=OCEAN,
        prep="Votre instance individuelle, dans son état final du TP8.",
        travail=[
            "Choisir un thème de blocs et appliquer une palette cohérente et lisible.",
            "Personnaliser l’en-tête et le pied de page avec l’éditeur de site.",
            "Créer un formulaire avec une extension autorisée et le tester avec des données fictives. Sinon, créer un formulaire de démonstration clairement indiqué comme non connecté.",
            "Vérifier les titres, les textes alternatifs, les permaliens et la version mobile.",
            "Si autorisé, créer un compte Éditeur fictif et justifier ce rôle dans la fiche.",
            "Rédiger une fiche de maintenance : mises à jour, sauvegarde, comptes, extensions.",
        ],
        contraintes="Installer une extension seulement si l’enseignant l’autorise. Jamais de vrai mot de passe dans les captures, jamais de donnée personnelle réelle dans le formulaire.",
        criteres="Identité graphique, navigation, formulaire ou alternative documentée, maintenance et accessibilité.",
        rendre=f"La fiche {FICHE}, la fiche de maintenance et des captures, sans identifiant ni mot de passe visible.",
        plus="Comparer deux rôles WordPress en deux phrases et vérifier la navigation au clavier.",
    ),
    dict(
        num="10", titre="ÉVALUATION 2 - JavaScript et WordPress", projet="Ocean Fest", evaluation=True,
        objectifs=[
            "Réaliser une tâche autonome en JavaScript et DOM.",
            "Administrer un site WordPress existant en respectant un cahier des charges.",
            "Livrer des preuves reproductibles de fonctionnement.",
        ],
        notions="DOM et événements, WordPress (pages, catégories, menu), tests et livrables.",
        situation="Épreuve individuelle : vous terminez la page de programme du festival Ocean Fest et complétez son site WordPress.",
        prep="L’archive `TP10_Fichiers_depart.zip` et une instance WordPress d’évaluation, avec ses identifiants, fournies par l’enseignant.",
        travail=[
            "Partie A, 60 min : dans le mini-site de départ, ajouter le filtre des activités et le compteur.",
            "Partie B, 25 min : compléter l’instance WordPress (page, catégorie, article, menu).",
            "5 min : déposer les fichiers et le document de preuves.",
        ],
        cahier=("Cahier des charges", [
            "**Partie A.** La page présente 6 activités portant un attribut `data-type` (`concert`, `atelier`, `rencontre`). Ne pas modifier ces valeurs.",
            "Créer un `select` avec son `label`, proposant Toutes, Concert, Atelier et Rencontre : le choix n’affiche que les activités correspondantes. L’option Toutes réaffiche les 6 activités.",
            "Créer un compteur du nombre d’activités visibles, exact dès le chargement de la page.",
            "**Partie B.** Créer et publier la page « Informations pratiques » (titre et texte).",
            "Créer la catégorie « Actualités » et l’affecter à l’article « Bilan de la dernière édition », déjà présent.",
            "Ajouter la page au menu et vérifier le résultat en navigation privée.",
        ]),
        contraintes=REGLE_EVAL + " Les opérations se font uniquement sur votre instance d’évaluation.",
        criteres="Barème sur 100 : JavaScript et DOM 60 (filtre 30, compteur 20, qualité 10) ; WordPress 30 ; livrables et tests 10.",
        rendre=f"Un ZIP avec `index.html`, `script.js` et la fiche {FICHE}, incluant une capture du menu et une de la catégorie, sans identifiant visible.",
    ),
]

REPARTITION = [
    ["TP", "Séance", "Notions principales"],
    ["01", "Comprendre le Web et créer une page HTML", "HTTP(S), URL, client/serveur, balises, img, a, alt"],
    ["02", "Structurer un site multipage en HTML", "Sémantique, liens relatifs, formulaire, GET/POST"],
    ["03", "Mettre en forme un site avec CSS", "Sélecteurs, héritage, spécificité, modèle de boîte"],
    ["04", "Créer une interface responsive", "Flexbox, Grid, rem, %, max-width, @media, focus"],
    ["05", "**ÉVALUATION 1** - HTML et CSS", "Sémantique, CSS externe, responsive, accessibilité"],
    ["06", "Découvrir JavaScript et les événements", "defer, const/let, conditions, fonctions, addEventListener"],
    ["07", "Manipuler le DOM et valider un formulaire", "querySelector, createElement, preventDefault, trim"],
    ["08", "Découvrir WordPress et publier du contenu", "CMS, PHP, base de données, pages, articles, permaliens"],
    ["09", "Personnaliser et administrer WordPress", "Thèmes de blocs, extensions, rôles, maintenance, SEO"],
    ["10", "**ÉVALUATION 2** - JavaScript et WordPress", "DOM, événements, pages, catégories, menu, preuves"],
]

DEROULE = dict(
    fichier="00_Deroule_10_TP.pdf", kicker="Développement web · Document enseignant",
    titre="Déroulé des 10 TP", meta="HTML · CSS · JavaScript · WordPress · 10 séances de 1h30",
    blocs=[
        ("h", "Présentation générale"),
        ("p", "**Public :** débutants découvrant le développement web. **Volume :** 10 séances de 1h30, soit 15 h, dont deux évaluations (TP5 et TP10)."),
        ("p", "**Projet fil rouge :** le site fictif Ocean Fest. Objectif final : créer des pages HTML/CSS, les rendre interactives en JavaScript et administrer un site WordPress."),
        ("p", "**Matériel :** navigateur récent, VS Code ou équivalent, et une instance WordPress individuelle par étudiant ou étudiante (voir `00_Guide_enseignant_WordPress.pdf`)."),
        ("h", "Répartition et progression"),
        ("schema", "frise", 1),
        ("table", REPARTITION, [1.0, 7.6, 9.4]),
        ("h", "Méthode recommandée"),
        ("p", "Séances d’apprentissage : 15 min de démonstration, 20 min d’exercice guidé, 45 min de travail autonome et 10 min de bilan."),
        ("p", "Chaque séance repart du rendu précédent ou de sa correction, à diffuser après la remise. Exception voulue : le TP5 porte sur un site et une feuille de style distincts du fil rouge. Les corrections diffusées ne donnent donc pas la réponse."),
        ("h", "Évaluations"),
        ("ul", [
            "**TP5 :** évaluation HTML/CSS, coefficient conseillé 40 %.",
            "**TP10 :** évaluation JavaScript et WordPress, coefficient conseillé 60 % : 60 min de JavaScript, 25 min de WordPress, 5 min de remise.",
            "Les barèmes détaillés (`BAREME.txt`) sont dans les corrections. Ils restent ajustables selon le niveau, les moyens techniques et les règles de l’établissement.",
        ]),
        ("h", "Compétences évaluées"),
        ("ul", [
            "Structurer une page avec des éléments HTML sémantiques et des liens fiables.",
            "Styliser un site et le rendre responsive avec CSS.",
            "Réagir aux événements et modifier le DOM en JavaScript.",
            "Créer, organiser et administrer des contenus dans WordPress ; identifier les contraintes de sécurité et de maintenance.",
        ]),
        ("h", "Diffusion aux étudiants"),
        ("ul", [
            "**À chaque séance :** le sujet PDF du TP.",
            "**TP8, TP9 et TP10 :** en plus, la fiche de réalisation WordPress.",
            "**TP10, le jour de l’épreuve :** en plus, `TP10_Fichiers_depart.zip`.",
            "**Après la remise uniquement :** le ZIP de correction du TP. Ne pas diffuser les corrections du TP5 et du TP10 avant la fin de toutes les sessions d’épreuve.",
            "**Jamais :** le dossier `_source/`, ce déroulé et le guide WordPress restent côté enseignant.",
        ]),
        ("p", "Les formulaires sont pédagogiques : aucune donnée personnelle réelle n’est collectée."),
        ("h", "Contenu du kit"),
        ("ul", [
            "`00_Deroule_10_TP.pdf` : ce document.",
            "`00_Guide_enseignant_WordPress.pdf` : préparation des instances.",
            "`Fiche_realisation_WordPress.pdf` et `.md` : modèle pour les étudiants.",
            "`TP01/` à `TP10/` : un sujet PDF et un ZIP de correction ; en plus, pour le TP10, les fichiers de départ.",
            "`Atelier_IA/` : séance d’essai facultative et non notée, à placer après le TP7 (hors des 10 séances).",
            "`site/` : site public du cours, sans correction ni sujet d’évaluation par défaut.",
            "`_source/` : textes et scripts qui régénèrent les PDF, les ZIP et le site.",
        ]),
    ],
)

GUIDE_WP = dict(
    fichier="00_Guide_enseignant_WordPress.pdf", kicker="Développement web · Document enseignant",
    titre="Préparer les instances WordPress", meta="À faire avant le TP8 · TP8, TP9 et TP10",
    blocs=[
        ("h", "Principe"),
        ("p", "**Prévoir une instance par étudiant ou étudiante.** Le titre du site, la page d’accueil, le menu et le thème sont des réglages globaux : sur une instance partagée, chacun écraserait le travail des autres. Aucun serveur ni compte n’est inclus dans ce kit."),
        ("schema", "instances", 1),
        ("h", "Instance de TP (TP8 et TP9)"),
        ("ul", [
            "WordPress à jour, en français, avec un thème de blocs récent (par exemple Twenty Twenty-Five) disponible.",
            "Un compte personnel avec le rôle Administrateur : les rôles inférieurs n’accèdent pas à tous les réglages demandés.",
            "Accès restreint à la formation, site exclu de l’indexation (Réglages > Lecture).",
            "Conservation de l’instance entre le TP8 et le TP9 : le TP9 repart de l’état final du TP8.",
            "Décision à prendre avant le TP9 : installation d’extensions autorisée ou non, et extension de formulaire retenue. Sans extension, les étudiants documentent un formulaire de démonstration.",
        ]),
        ("h", "Instance d’évaluation (TP10)"),
        ("p", "Utiliser une **nouvelle instance**, pas celle des TP : la catégorie « Actualités » y existe déjà depuis le TP8, ce qui fausserait la Partie B."),
        ("ul", [
            "Mêmes version, langue et thème que l’instance de TP.",
            "Un menu de navigation existant, avec au moins une page.",
            "Un article publié, intitulé exactement « Bilan de la dernière édition », dans la catégorie par défaut.",
            "Aucune page « Informations pratiques » et aucune catégorie « Actualités ».",
            "Un compte dédié à l’épreuve, désactivé à la fin.",
        ]),
        ("h", "Contrôle avant chaque séance"),
        ("ul", [
            "Se connecter avec un compte de test et vérifier l’accès à Réglages, Apparence, Pages et Articles.",
            "Vérifier que le site s’ouvre en navigation privée.",
            "Sauvegarder ou pouvoir recréer l’instance en cas d’erreur.",
            "Remettre les identifiants séparément du sujet, et prévoir des comptes de secours.",
        ]),
        ("h", "Si une instance par personne est impossible"),
        ("p", "Les TP8, TP9 et la Partie B du TP10 doivent alors être réécrits autour de contenus propres à chaque compte, sans réglage global. Les sujets actuels ne fonctionnent pas sur une instance partagée."),
        ("h", "Après la formation"),
        ("p", "Supprimer les instances et les comptes, et conserver uniquement les rendus utiles à l’évaluation, selon les règles de l’établissement."),
    ],
)

FICHE_DOC = dict(
    fichier="Fiche_realisation_WordPress.pdf", kicker="Développement web · TP8, TP9 et TP10",
    titre="Fiche de réalisation WordPress", meta="À compléter et à joindre au rendu · Version modifiable : fichier .md",
    blocs=[
        ("box", "Avant de déposer", [
            "Aucun identifiant ni mot de passe visible dans les captures.",
            "Aucune donnée personnelle réelle.",
        ]),
        ("h", "Identification"),
        ("table", [["Nom et prénom", ""], ["TP et date", ""], ["Adresse de l’instance", ""]], [5.0, 13.0]),
        ("h", "Actions réalisées"),
        ("table", [["Action", "Où dans l’administration", "Résultat vérifié", "Capture n°"],
                   ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]], [5.2, 5.0, 5.2, 2.6]),
        ("h", "Test en navigation privée"),
        ("table", [["Lien ou page testée", "Résultat attendu", "Résultat obtenu"],
                   ["", "", ""], ["", "", ""], ["", "", ""]], [6.0, 6.0, 6.0]),
        ("h", "Questions du sujet (TP8, TP9)"),
        ("lignes", 4),
        ("h", "Difficultés et solutions"),
        ("lignes", 3),
    ],
)

FICHE_MD = """# Fiche de réalisation WordPress

Avant de déposer : aucun identifiant ni mot de passe visible, aucune donnée personnelle réelle.

## Identification
- Nom et prénom :
- TP et date :
- Adresse de l’instance :

## Actions réalisées
| Action | Où dans l’administration | Résultat vérifié | Capture n° |
|---|---|---|---|
|  |  |  |  |

## Test en navigation privée
| Lien ou page testée | Résultat attendu | Résultat obtenu |
|---|---|---|
|  |  |  |

## Questions du sujet (TP8, TP9)

## Difficultés et solutions
"""

LISEZ_MOI = """KIT PÉDAGOGIQUE - 10 TP WEB - La Rochelle Université

DOCUMENT ENSEIGNANT : commencer par 00_Deroule_10_TP.pdf, puis 00_Guide_enseignant_WordPress.pdf.

Chaque dossier TP contient un sujet PDF et une archive ZIP de correction.
Les corrections restent réservées aux enseignants jusqu'à la remise, en particulier pour TP05 et TP10.
TP10 contient aussi TP10_Fichiers_depart.zip, à distribuer le jour de l'évaluation.
Fiche_realisation_WordPress.pdf et .md sont à distribuer pour TP08, TP09 et TP10.
WordPress : prévoir une instance par personne. Aucun serveur ni compte n'est inclus.
Atelier_IA/ contient une séance d'essai facultative, non notée (guide dans le ZIP de correction).
site/ contient le site public du cours, sans correction ni sujet d'évaluation par défaut.
_source/ contient de quoi régénérer les PDF, les ZIP et le site (voir _source/README.md).
"""
