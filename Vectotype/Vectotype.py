#!/usr/bin/env python
"""
Vectotype v1.0
Execute from FontForge.
Reads unicode numbered SVGs and converts them to outline font on FontForge.
"""
import fontforge
from os import listdir
from shutil import rmtree

font = fontforge.font()

#
# User defined variables
#
glyph_width = 1024
font.ascent = 896
font.descent = 128

os2_ascent = None
os2_descent = None
os2_linegap = None

font.fontname = "VectotypeFont"
font.fullname = "Vectotype Font"
font.familyname = "Vectotype Font"

svg_path = "/Users/Farique/Desktop/Make_Fonts/Vectotype.nosync/SVGs"
#
#
#

# Internal assigned variables
font.os2_vendor = '    '
font.copyright = r'Created with Vectotype - https://github.com/farique1'

os2_ascent = os2_ascent if os2_ascent else font.ascent
os2_descent = os2_descent if os2_descent else font.descent
os2_linegap = os2_linegap if os2_linegap else 0

font.os2_winascent_add = 0
font.os2_winascent = os2_ascent
font.os2_windescent_add = 0
font.os2_windescent = os2_descent

font.os2_use_typo_metrics = False

font.os2_typoascent_add = 0
font.os2_typoascent = os2_ascent
font.os2_typodescent_add = 0
font.os2_typodescent = -os2_descent
font.os2_typolinegap = os2_linegap

font.hhea_ascent_add = 0
font.hhea_ascent = os2_ascent
font.hhea_descent_add = 0
font.hhea_descent = -os2_descent
font.hhea_linegap = os2_linegap

font.os2_capheight = font.ascent
font.os2_xheight = font.ascent + font.descent

font.os2_panose = (2, 0, 5, 9, 0, 0, 0, 0, 0, 0)

# Do the thing
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

glyph = font.createChar(32)
glyph.width = glyph_width

# Folder cleanup. Remove comment to delete SVGs folder
# rmtree(svg_path + '/', ignore_errors=True)
