from initialize import initialize_sheet, start_sheet
from Translator_py_ly.translator import start_translator
from Automatic_bass.Bass import autobass
from finalize import compile_PDF

reference = "G4"
key_signature = "CM"
melody = "G-G | A_ G C | B__ G-G | A_ G D5 | C__ G-G | G5_ E C | B A__ | F5-F E_ C | D C__^ | C__. ||"

#reference = "C5"
#key_signature = "AbM"
#coldplay = "R_ R- C- C_ C | C__. D- B-^ | B__ R- B_ A- | B_ B-A C_ E4- F-^ | F-C5 C-C C-C C_ | C__. D- B-^ | B__ R- B_ A- | B_ B B C- A-^ | A- F_. R__ | R__ R_ R- E5- | " \
#            + "F_ F F-E F- E-^ | E_ B- C_ D_. | E_ E E-C E- C-^ | C_ F4- G_ A_. ||"

initialize_sheet()
start_sheet(reference, key_signature)

start_translator(melody, reference, key_signature)
#start_translator(coldplay, reference, key_signature)
#start_bass(coldplay, reference, key_signature)

autobass(melody, reference, key_signature)

compile_PDF()