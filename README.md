# Get Font Chars

Lightweight python 3 script used to output all characters supported by a font into text file or console output. One of the usages is to get supported font characters for Unity's TextMesh Pro font asset generation. 

Bonus: [pre-generated maps of popular fonts](maps)

## Requirements

Developed with `Python 3.9`

Installed fonttools: `pip3 install fonttools`

## Usage

Basic usage, **output all font characters to the text file**: `python getfontchars.py -i font.ttf -o font.txt`

**Print all font characters to console**: `python getfontchars.py -i font.ttf -t`

**Specify font page** if the font has multiple pages (pages are starting from 0): `python getfontchars.py -i font.ttf -p 1 -o font.txt`

Help page:

```
usage: getfontchars.py [-h] [-p PAGE] [-t [PRINT]] [-o OUTPUT] -i INPUT


optional arguments:
  -h, --help            show this help message and exit
  -p PAGE, --page PAGE  Font page if multipage font
  -t [PRINT], --print [PRINT]
                        Print list of character to console
  -o OUTPUT, --output OUTPUT
                        Output UTF-8 txt file

required named arguments:
  -i INPUT, --input INPUT
                        Input font file
```

## Limitations

**Some fonts can't be processed, such as Webdings or Symbols.**

## Also

Check out [already generated character maps](maps)
