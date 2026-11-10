# Sources du kit

- `sujets.py` : textes des sujets, du déroulé, du guide et de la fiche.
- `corrections.py` : contenu des ZIP de correction et des fichiers de départ.
- `atelier_ia.py` : sujet et fichiers de la séance d'essai sur l'IA.
- `figures.py` : schémas et placement des figures dans les sujets.
- `captures.py` : captures d'écran des corrections (macOS, à relancer si une correction change).
- `polices.py` : prépare les polices à partir de Raleway (à ne relancer que pour changer de graisses).
- `build.py` : génère les PDF et les ZIP dans le dossier parent.
- `build_site.py` : génère le site public dans `../site`, après `build.py`.

Pour régénérer le kit : `pip install reportlab==4.2.5`, puis `python build.py`.

## Gabarit
D'après l'extrait de la charte graphique 2024 de La Rochelle Université : A4, logo de 3 cm en haut à gauche, marges de 1,5 cm en tête et à gauche, zone de protection autour du logo. Police : Raleway, celle du document de la charte.

- `assets/logo-la-rochelle-universite.png` provient du site de l'université (240 × 240 px). La charte demande de contacter la direction de la communication (communication@univ-lr.fr) pour obtenir le fichier de logo : remplacer celui-ci par le fichier officiel, sous le même nom.
- `assets/TexteLRU-*` : polices dérivées de Raleway (licence SIL OFL, voir `assets/LICENCE-police.txt`), avec des chiffres alignés. La licence réserve le nom Raleway, d'où le nom Texte LRU. `polices.py` les régénère.
- Tailles et couleurs reprises du document de la charte : texte Regular 10 pt noir, titres ExtraBold `#256CB4` à 25 et 14 pt. Les PDF n'utilisent aucune autre police, y compris pour le code. La mention « Source Sans Pro » de la charte est un texte blanc invisible sur fond blanc.
- L'extrait public ne contient ni la palette ni les gabarits de documents : le bleu vient du logo, le bleu marine du site de l'université.

## Site public
`site/` est statique : le contenu de ce dossier se dépose tel quel sur GitHub Pages ou un autre hébergement.

Par défaut, il ne contient ni correction, ni sujet d'évaluation, ni fichier de départ du TP10. Pour les libérer, modifier les réglages en tête de `build_site.py` (`SUJETS_EVALUATION_PUBLIES`, `CORRECTIONS_PUBLIEES`, `DEPART_TP10_PUBLIE`, `DATES`, `ATELIER_IA_PUBLIE`, `DATE_ATELIER_IA`), puis relancer le script. Ne jamais publier `_source/`, ni le reste du kit.
