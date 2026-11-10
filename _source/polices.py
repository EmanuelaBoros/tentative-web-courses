"""Prépare les polices Raleway à partir des fichiers variables de Google Fonts.

Usage : python polices.py Raleway.ttf
Dépendances : fonttools, brotli. À ne relancer que pour changer de graisses.

Raleway utilise par défaut des chiffres elzéviriens, peu lisibles dans « 700 px » ou
« 1h30 » : on remplace chaque chiffre par sa variante alignée (fonctionnalité lnum).
La licence SIL OFL réserve le nom Raleway : la version modifiée s'appelle donc Texte LRU.
"""
import sys
from pathlib import Path

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ASSETS = Path(__file__).resolve().parent / "assets"
GRAISSES = [("Regular", 400), ("SemiBold", 600), ("Bold", 700), ("ExtraBold", 800)]
WEB = {"Regular", "Bold", "ExtraBold"}
UNICODES = list(range(0x20, 0x7F)) + list(range(0xA0, 0x180)) + [
    0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2026, 0x202F, 0x20AC, 0x2264, 0x2265]


def chiffres_alignes(police):
    gsub = police["GSUB"].table
    correspondance = {}
    for enreg in gsub.FeatureList.FeatureRecord:
        if enreg.FeatureTag == "lnum":
            for i in enreg.Feature.LookupListIndex:
                for table in gsub.LookupList.Lookup[i].SubTable:
                    table = getattr(table, "ExtSubTable", table)
                    correspondance.update(getattr(table, "mapping", {}))
    for table in police["cmap"].tables:
        for code in range(0x30, 0x3A):
            if code in table.cmap:
                table.cmap[code] = correspondance.get(table.cmap[code], table.cmap[code])


def instance(source, graisse, nom):
    police = instantiateVariableFont(TTFont(source), {"wght": graisse})
    chiffres_alignes(police)
    for enreg in police["name"].names:
        if enreg.nameID in (1, 16):
            enreg.string = "Texte LRU"
        elif enreg.nameID == 3:
            enreg.string = f"TexteLRU-{nom}"
        elif enreg.nameID == 4:
            enreg.string = f"Texte LRU {nom}"
        elif enreg.nameID == 6:
            enreg.string = f"TexteLRU-{nom}"
    return police


droit = sys.argv[1]
for nom, graisse in GRAISSES:
    police = instance(droit, graisse, nom)
    police.save(ASSETS / f"TexteLRU-{nom}.ttf")
    if nom in WEB:
        options = Options()
        options.flavor = "woff2"
        options.layout_features = ["*"]
        allegee = TTFont(ASSETS / f"TexteLRU-{nom}.ttf")
        decoupe = Subsetter(options)
        decoupe.populate(unicodes=UNICODES)
        decoupe.subset(allegee)
        allegee.flavor = "woff2"
        (ASSETS / "web").mkdir(exist_ok=True)
        allegee.save(ASSETS / "web" / f"TexteLRU-{nom}.woff2")
