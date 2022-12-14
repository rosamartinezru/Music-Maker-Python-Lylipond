## ACTIVE TRANSLATOR

from Translator_py_ly.dictionaries import *
from Music_Theory.Scales_and_modes import acc_notes
from Decorators.Decorators import decorator_octava

def start_translator(melody_py, reference, key_signature):          # Melody translation

    melody_ly = melody_translate(melody_py, reference, key_signature)
    melody_ly_decorated = decorator_octava(melody_ly)
    finish_staff = ["\n \\bar \"|.\"}"]

    with open("prueba.txt", "a") as f:
        f.write('\n'.join(melody_ly_decorated))
    #    f.write('\n'.join(melody_ly))
        f.write('\n'.join(finish_staff))

    return

def melody_translate(melody_py, reference, key_signature):

     """
     melody_translate This fuction translates the input melody (in python language) into lylipond language 

     :param melody_py: base note of the scale
     :param reference: mode of the scale (major/minor)
     :param key_signature: mode of the scale (major/minor)
     :return: Lylipond melody ready to be written into a .txt

     """

     i = 0                                                    
     staff = 0                                                
     n_staff = melody_py.count("|")-1   # Number of staffs                      
     melody_ly = [str(" ")]*n_staff

     key_acc_notes = acc_notes(key_signature) # Accidental notes 
    
     while i < (len(melody_py)-2):
         space_tot = melody_py.find(" ", i, len(melody_py) - 1)  # Find the gaps between notes   
         space_loc = space_tot - i  # Position of the gap inside the staff                                

         for j in range(i,space_tot):      
             
            if melody_py[j].isupper():   # An upper string correponds to the name of a note                           
                melody_ly[staff] += pitchly[melody_py[j]] 

                if melody_py[j] in key_acc_notes: # It adds the accidental note if it is inside the key signature
                    melody_ly[staff] += acc_ly[key_acc_notes[len(key_acc_notes)-1]]

            elif melody_py[j] in acc_ly:  # Accidental note outside the key signature 
                melody_ly[staff] += acc_ly[melody_py[j]]
                
            elif melody_py[j].isdigit():   # A digit correponds to a change in the note octave, refered to the current reference
                oct = int(melody_py[j]) - int(reference[1])

                if oct == 0:
                    melody_ly[staff] += octaves[oct+1]
                else:
                    melody_ly[staff] += octaves[oct]
                    reference =  melody_py[j-1] + melody_py[j]

            elif melody_py[j] == "|":  # Staff change
                staff += 1

            elif melody_py[j] in rythm_special: # Ligature or musical dot 
                melody_ly[staff] += rythm_special[melody_py[j]]
                melody_ly[staff] += " "
            
            else:    # Rythms                                               
                if melody_py[j+1] == "_":    # If it is a half note                       
                    melody_ly[staff] += rythm[melody_py[j:j+2]]

                    if melody_py[j+2] == "^" or melody_py[j+2] == ".":
                        melody_ly[staff] += rythm_special[melody_py[j+2]]
                    break

                else:
                    melody_ly[staff] += rythm[melody_py[j]]
                
                melody_ly[staff] += " "

         melody_ly[staff] += " " 
         i += space_loc+1

     return(melody_ly)   


 
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
