#!/usr/bin/env python
"""
Chartotype-B v1.0
Auto generated from Chartotype-A.py
Execute from FontForge.
Reads unicode numbered SVGs made with Chartotype-A and converts them to outline font on FontForge.
"""
import fontforge
from os import listdir
from shutil import rmtree
font = fontforge.font()
font.copyright = r'Created with Chartotype, potrace and FontForge 2.0 - https://github.com/farique1'
font.os2_vendor = '    '
glyph_width = 768
font.ascent = 896
font.descent = 128
font.fontname = "MSXScreen0New"
font.fullname = "MSX Screen 0 New"
font.familyname = "MSX Screen 0 New"
font.os2_winascent_add = 0
font.os2_winascent = 896
font.os2_windescent_add = 0
font.os2_windescent = 128
font.os2_use_typo_metrics = False
font.os2_typoascent_add = 0
font.os2_typoascent = 896
font.os2_typodescent_add = 0
font.os2_typodescent = -128
font.os2_typolinegap = 0
font.hhea_ascent_add = 0
font.hhea_ascent = 896
font.hhea_descent_add = 0
font.hhea_descent = -128
font.hhea_linegap = 0
font.os2_capheight = font.ascent
font.os2_xheight = font.ascent + font.descent
font.os2_panose = (2, 0, 5, 9, 0, 0, 0, 0, 0, 0)
svg_path = "/Users/Farique/Desktop/Make_Fonts/Chartotype.nosync/MSX/SVGs"
for f in listdir(svg_path):
    if f.endswith(".svg"):
        glyph_code = int(f[:-4])
        glyph = font.createChar(glyph_code)
        glyph.importOutlines(svg_path + "/" + f)
        glyph.width = glyph_width
        glyph.round()
        glyph.simplify()
        glyph.simplify(1.02, 'forcelines')
        glyph.autoHint()
rmtree("/Users/Farique/Desktop/Make_Fonts/Chartotype.nosync/MSX/SVGs/", ignore_errors=True)
