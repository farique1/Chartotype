#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Chartotype-A v1.0
Convert bitmap font dumps into SVG files to be loaded into FontForge with Chartotype-B
"""
from sys import argv
from sys import stdout
from os import system
from os import getcwd
from os import makedirs
from PIL import Image
from shutil import rmtree
from unicodedata import name
from itertools import product
from io import open as openio

# Base for the Chartotype-B FontForge script.
chartotype_b = '''#!/usr/bin/env python
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
font.os2_winascent_add = 0
font.os2_windescent_add = 0
font.os2_use_typo_metrics = False
font.os2_typoascent_add = 0
font.os2_typodescent_add = 0
font.hhea_ascent_add = 0
font.hhea_descent_add = 0
font.os2_capheight = font.ascent
font.os2_xheight = font.ascent + font.descent
font.os2_panose = (2, 0, 5, 9, 0, 0, 0, 0, 0, 0)
for f in listdir(svg_path):
    if f.endswith(".svg"):
        glyph_code = int(f[:-4])
        glyph = font.createChar(glyph_code)
        glyph.importOutlines(svg_path + "/" + f)
        glyph.width = glyph_width
        glyph.round()
        glyph.simplify()
        glyph.simplify(1.02, 'forcelines')
        glyph.autoHint()'''

# Put into an array
chartotype_b = chartotype_b.split('\n')

# Get command line arguments
verbose = 1
if len(argv) >= 2:
    font_base = argv[1]
else:
    font_base = 'Odyssey2'

if len(argv) == 3:
    try:
        verbose = int(argv[2])
    except ValueError:
        verbose = 1

# Assign variable values
system_folder = font_base + '/'
png_folder = system_folder + 'PNGs/'
bmp_folder = system_folder + 'BMPs/'
svg_folder = system_folder + 'SVGs/'
current_folder = getcwd()

char_tbale_image = font_base + 'CharMap.png'
with openio(system_folder + font_base + 'CharMap.txt', 'r', encoding='utf-8') as char_map:
    char_string = char_map.read()
char_lenght = len(char_string)

# Get general .ini arguments
chartotype_ini = [line for line in open('Chartotype.ini', 'r')]
auto_save = True if chartotype_ini[1][11:].strip() == 'True' else False
save_report = True if chartotype_ini[2][13:].strip() == 'True' else False
save_raw_png = True if chartotype_ini[3][14:].strip() == 'True' else False
delete_folders = True if chartotype_ini[4][16:].strip() == 'True' else False

# Get system specific .ini arguments
system_ini = [line for line in open(system_folder + font_base + 'Chartotype.ini', 'r')]
char_width = int(system_ini[1][12:])
char_height = int(system_ini[2][13:])
trim_width = int(system_ini[3][12:])
trim_height = int(system_ini[4][13:])
resize_factor = int(system_ini[5][15:])
invert_luma = True if system_ini[6][13:].strip() == 'True' else False
glyph_width = int(system_ini[8][13:])
ascent = reduce(lambda x, y: x - y, map(int, system_ini[9][8:].strip().split(' - ')))
descent = int(system_ini[10][9:])
fontname = system_ini[11][10:].strip()
fullname = system_ini[12][10:].strip()
familyname = system_ini[13][12:].strip()
os2_ascent = ascent if system_ini[15][12:].strip() == "" else int(system_ini[15][12:])
os2_descent = descent if system_ini[16][13:].strip() == "" else int(system_ini[16][13:])
os2_linegap = 0 if system_ini[17][13:].strip() == "" else int(system_ini[17][13:])

# Assign Chartotype-B script values
chartotype_b.insert(13, 'glyph_width = ' + str(glyph_width))
chartotype_b.insert(14, 'font.ascent = ' + str(ascent))
chartotype_b.insert(15, 'font.descent = ' + str(descent))
chartotype_b.insert(16, 'font.fontname = "' + fontname + '"')
chartotype_b.insert(17, 'font.fullname = "' + fullname + '"')
chartotype_b.insert(18, 'font.familyname = "' + familyname + '"')
chartotype_b.insert(20, 'font.os2_winascent = ' + str(os2_ascent))
chartotype_b.insert(22, 'font.os2_windescent = ' + str(os2_descent))
chartotype_b.insert(25, 'font.os2_typoascent = ' + str(os2_ascent))
chartotype_b.insert(27, 'font.os2_typodescent = -' + str(os2_descent))
chartotype_b.insert(28, 'font.os2_typolinegap = ' + str(os2_linegap))
chartotype_b.insert(30, 'font.hhea_ascent = ' + str(os2_ascent))
chartotype_b.insert(32, 'font.hhea_descent = -' + str(os2_descent))
chartotype_b.insert(33, 'font.hhea_linegap = ' + str(os2_linegap))
chartotype_b.insert(37, 'svg_path = "' + current_folder + '/' + system_folder + 'SVGs"')
if auto_save:
    chartotype_b.append('font.save("' + current_folder + '/' + system_folder + fullname + '.sfd")')
    chartotype_b.append('font.generate("' + current_folder + '/' + system_folder + fullname + '.ttf")')
if delete_folders:
    chartotype_b.append('rmtree("' + current_folder + '/' + svg_folder + '", ignore_errors=True)')

# Interpret image character map
img = Image.open(system_folder + char_tbale_image)
image_x = img.width
image_y = img.height
chars_in_image = (image_x * image_y) / (char_width * char_height)

# Get image mid point luminance
colors = img.getcolors()
colors.sort(reverse=True)
luma_1 = 0.2126 * colors[0][1][0] + 0.7152 * colors[0][1][1] + 0.0722 * colors[0][1][2]
luma_2 = 0.2126 * colors[1][1][0] + 0.7152 * colors[1][1][1] + 0.0722 * colors[1][1][2]
luma_avg = (luma_1 + luma_2) / 2
if luma_1 < luma_2:
    invert_luma = not invert_luma


def black_white(x):  # Convert pixel to black or white
    pixel = 255 if x > luma_avg else 0
    if invert_luma:
        pixel = abs(pixel - 255)
    return pixel


# Folder management
if save_raw_png:
    rmtree(png_folder, ignore_errors=True)
rmtree(bmp_folder, ignore_errors=True)
rmtree(svg_folder, ignore_errors=True)

if save_raw_png:
    makedirs(png_folder)
makedirs(bmp_folder)
makedirs(svg_folder)

# Process image
number = 0
chars_list = []
output_list = ['bitmap x, bitmap y, number, unicode, character, name']
for y, x in product(range(0, image_y, char_height), range(0, image_x, char_width)):

    if number > char_lenght - 1:
        break

    char_actual = char_string[number]
    char_unicode = ord(char_actual)

    try:
        char_name = name(char_actual)
    except ValueError:
        n = ""

    if verbose == 1:
        stdout.write('.')
        stdout.flush()
    elif verbose >= 2:
        print x, y, number, char_unicode, char_actual, char_name
    output_list.append(','.join((str(x), str(y), str(number), str(char_unicode), char_actual, char_name)))

    # If character is repeated
    if char_unicode in chars_list:
        if verbose >= 2:
            print '* Above already exists *'
        output_list.append('* Above already exists *')
        number += 1
        continue

    chars_list.append(char_unicode)

    img_crop = img.crop((x, y, x + char_width - trim_width, y + char_height - trim_height))
    if save_raw_png:
        img_crop.save(png_folder + str(char_unicode) + '.png')
    img_crop = img_crop.convert('L').point(black_white, mode='1')
    img_crop = img_crop.resize(((char_width - trim_width) * resize_factor, (char_height - trim_height) * resize_factor))
    img_crop.save(bmp_folder + str(char_unicode) + '.bmp')
    system('./potrace-1.15.mac-x86_64/potrace ' + bmp_folder + str(char_unicode) + '.bmp -o ' + svg_folder + str(char_unicode) + '.svg -z left -s')
    number += 1

if verbose == 1:
    print

# Save Chartotype-B script
with open('Chartotype-B.py', 'w') as f:
    for line in chartotype_b:
        f.write(line + '\n')

# Save report file
if save_report:
    output_list = map(unicode, output_list)
    with openio(system_folder + font_base + 'Report.txt', 'w', encoding='utf-8') as f:
        for line in output_list:
            f.write(line + '\n')

# Delete temporary folder
if delete_folders:
    rmtree(bmp_folder, ignore_errors=True)
