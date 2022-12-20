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

def key_ly(key):    

     """
     key_ly This fuction translates the key signature into lylipond language 

     :param key: Input key signature (python)
     :return: Lylipond key signature

     """

     if len(key)==3:
         note_acc = pitchly[key[0]] + acc_ly[key[1]]
         keysig_ly = (note_acc, mode_ly[key[2]])

     elif len(key)==2:
         keysig_ly = (pitchly[key[0]], mode_ly[key[1]])

     return keysig_ly
