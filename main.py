#from GUI.gui import GUI
from Translator_py_ly.translator import translator
from Automatic_bass.Bass import autobass
from Adornments.adornments import adorn_all_octaves
from sheet_generator import compile_PDF, header

## Happy Birthday

#reference = "G4"
#key_signature = "CM"
#melody = "G-G | A_ G C | B__ G-G | A_ G D5 | C__ G-G | G5_ E C | B A__ | F5-F E_ C | D C__^ | C__. ||"

## Coldplay

reference = "C5"
key_signature = "AbM"
melody = "R_ R- C- C_ C | C__. D- B-^ | B__ R- B_ A- | B_ B-A C_ E4- F-^ | F-C5 C-C C-C C_ | C__. D- B-^ | B__ R- B_ A- | B_ B B C- A-^ | A- F_. R__ | R__ R_ R- E5- | " \
            + "F_ F F-E F- E-^ | E_ B- C_ D_. | E_ E E-C E- C-^ | C_ F4- G_ A_. ||"

# reference, key_signature, melody = GUI()

sheet_start, melody_start = header(reference, key_signature)

melody_ly = translator(melody, reference, key_signature)

decorated_melody = adorn_all_octaves(melody_ly)

bass = autobass(melody, reference, key_signature)

full_txt_sheet = [sheet_start, melody_start, decorated_melody, bass]

compile_PDF(full_txt_sheet)
