# Translator dictionary (from python language to lylipond format)

# Pitch or notes (R is from rest)

pitchly = {"A":"a", "B":"b", "C":"c", "D":"d", "E":"e", "F":"f", "G":"g", "R":"r"} 

# Rythms

# whole: Go
# half: G__
# quarter: G
# eight: G-G ó A-
# sixteenth: G=G ó A=

rythm = {"o": "1", "__": "2", "_": "4", "-": "8", "=": "16"}

# "^":ligature junction 
# ".": musical dot 

rythm_special = {"^": "~", ".": "."}

# Pitch octave correpondance

octaves = {1:"'", 2:"''", 3:"'''", -1:",", -2:",,", -3:",,,"}

# Accidentals 

acc_ly = {"#": "is" , "b": "es", "##": "isis", "bb": "eses"}

# Key signature modes

mode_ly = {"M":"major", "m":"minor" }

           
# Bass mode

bass_mode = {"M": " ", "m":"m" }
