# Vectotype

***Vec To Type***  
A Python **FontForge** script to load a series of unicode numbered SVG files into **FontForge** and export them as a font file.  
**Vectotype** is a standalone version of [Chartotype-B](https://github.com/farique1/Chartotype) with all the configurations defined inside the code.  


## How to use  

### The SVGs  

**Vectotype** needs a folder with a series os individual `.svg` files each with one character named with its unicode number (ie. `33.svg` should be an exclamation mark).  


### The code  

The font characteristics must be set on this section of the code:  
```
...
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

svg_path = "/CURRENT_PATH/Vectotype/SVGs"
#
...
```
TrueType fonts prefer to have a power of two size, usually 1024, so the sum of the `ascent` and `descent` should be this number. The `width` must be the horizontal size of the font (this will create a monospaced font, obviously).  

The `os2` settings can be used to change the vertical (line) spacing without altering the fonts. They can be left as `None`.  

Next comes the font name and family.  

And lastly is the full SVGs folder path.   

### The execution  

Put all the SVGs into a folder, edit the code with the font settings and run the script with **FontForge** on the `File > Script Menu` menu (pasting the script straight to the `Execute Script...` box doesn't always work). Configure the `Script Menu` on `File > Preferences... > Script Menu` this only needs to be done once as long as the path to `Vectotype.py` doesn't change.  

**Vectotype** will load each character into it's own glyph slot on **FontForge** and apply the settings defined on the Python code.  

Check if everything went alright and export the font file and save the **FontForge** Project.  


## The Tools  

The font can be created with the included `Vectotype.ai` Illustrator template. The layers are named after the unicode characters numbers and names.  
These layers can be exported as SVGs individually using the `MultiExporter_UnicodeNames.jsx` Illustrator script (a slightly modified version of Tom Bryne's and Matthew Ericson's [MultiExporter.jsx](https://gist.github.com/TomByrne/7816376) script)  
By checking the `Unicode Number Only` checkbox, the files will be saved with a name taken from the unicode layer number (anything before the first ` - ` (*space dash space*))  
The script will not export any layer beginning with `-` (that can be used as guides) and will include all layers beginning with `+`.  

You can also create a bunch of illustrator layers by using the `illustratorCreateLayers.jsx` script, directing it to a text file where each line will name a layer (`Unicode List.txt` is included as an example).  

>Execute the scripts with the `File > Scripts` menu.  


## Acknowledgements  

Enjoy and send feedback.  
Thanks.  

***Vectotype** is offered as is, with no guaranties whatsoever. I think it will behave however (mostly).*  