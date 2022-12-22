#from GUI.gui import GUI
from Translator_py_ly.translator import translator
from Automatic_bass.Bass import autobass
from Adornments.adornments import adorn_all_octaves
from sheet_generator import compile_PDF, header
from GUI.GUI import start_GUI


## Happy Birthday

#reference = "G4"
#key_signature = "CM"
#melody = "G-G | A_ G C | B__ G-G | A_ G D5 | C__ G-G | G5_ E C | B A__ | F5-F E_ C | D C__^ | C__. ||"

## Coldplay 

# reference = "C5"
# key_signature = "AbM"
# melody = "R_ R- C- C_ C | C__. D- B-^ | B__ R- B_ A- | B_ B-A C_ E4- F-^ | F-C5 C-C C-C C_ | C__. D- B-^ | B__ R- B_ A- | B_ B B C- A-^ | A- F_. R__ | R__ R_ R- E5- | " \
#             + "F_ F F-E F- E-^ | E_ B- C_ D_. | E_ E E-C E- C-^ | C_ F4- G_ A_. ||"

# reference, key_signature, melody = GUI()

start_GUI()

# [Title, Composer, Instrument, Reference, key_signature, figure, Time, metronome, Clef, Anacruse, time_anacruse, song]
#    0      1           2           3           4           5       6       7       8       9           10          11

header_input = [str(" ")]*12
f = open('music_data.txt', 'r')
Lines = f.readlines()
count = 0
for line in Lines:
    header_input[count] = line[0:-1]
    if count == 11:
        header_input[count] = line
    count += 1

print(header_input)
sheet_start, melody_start = header(header_input)

melody_ly = translator(header_input)

decorated_melody = adorn_all_octaves(melody_ly)
bass = autobass(header_input)

full_txt_sheet = [sheet_start, melody_start, decorated_melody, bass]

compile_PDF(full_txt_sheet)

