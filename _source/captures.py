"""Régénère les captures des corrections (macOS : utilise Quick Look).

Usage : python captures.py   après build.py. Relancer ensuite build.py.
Les évaluations n'ont volontairement aucune capture.
"""
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from PIL import Image, ImageChops, ImageOps

RACINE = Path(__file__).resolve().parent.parent
SORTIE = Path(__file__).resolve().parent / "assets" / "captures"


def sans_section(html, titre):
    return re.sub(r'\s*<section>\s*<h2>' + titre + r'</h2>.*?</section>', "", html, flags=re.S)


def tp06(html):
    html = sans_section(sans_section(html, "Prochains événements"), "Horaires")
    html = re.sub(r'\s*<img [^>]*>', "", html)
    return (html.replace("<body>", '<body class="nuit">').replace(">Mode nuit<", ">Mode jour<")
            .replace(">Prêt !<", ">Prochain artiste : Ariane<"))


def tp07(html):
    taches = "".join(f'<li><span>{t} </span><button type="button">Supprimer</button></li>'
                     for t in ("Réserver la scène", "Imprimer le programme"))
    return (html.replace('<p id="erreur" role="alert"></p>', '<p id="erreur" role="alert">Saisissez une tâche.</p>')
            .replace(">0 tâche<", ">2 tâches<").replace('<ul id="liste"></ul>', f'<ul id="liste">{taches}</ul>'))


# nom, page, largeur rendue, transformation éventuelle, hauteur maximale gardée
PLANS = [("TP01", "index.html", 900, None, 900), ("TP02", "contact.html", 900, None, 900),
         ("TP03", "index.html", 1100, None, 955), ("TP04", "index.html", 1100, None, 640),
         ("TP06", "index.html", 1100, tp06, 760), ("TP07", "index.html", 1000, tp07, 640)]


def recadrer(chemin, hauteur):
    im = Image.open(chemin).convert("RGB")
    im = im.crop((0, 0, im.width, min(hauteur, im.height)))
    fond = Image.new("RGB", im.size, im.getpixel((im.width - 1, im.height - 1)))
    boite = ImageChops.difference(im, fond).getbbox()
    if boite:
        # Sur fond blanc (pages sans CSS), on retire aussi la marge vide à droite.
        droite = min(im.width, boite[2] + 24) if im.getpixel((im.width - 1, 0)) == (255, 255, 255) else im.width
        im = im.crop((0, 0, droite, min(im.height, boite[3] + 16)))
    return ImageOps.expand(im, border=2, fill=(201, 214, 227))


SORTIE.mkdir(parents=True, exist_ok=True)
for tp, page, largeur, transforme, hauteur in PLANS:
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        zipfile.ZipFile(RACINE / tp / f"{tp}_Correction.zip").extractall(t)
        if transforme:
            (t / page).write_text(transforme((t / page).read_text(encoding="utf-8")), encoding="utf-8")
        subprocess.run(["qlmanage", "-t", "-s", str(largeur), "-o", str(t), str(t / page)], capture_output=True, check=True)
        recadrer(t / f"{page}.png", hauteur).save(SORTIE / f"{tp.lower()}.png")
