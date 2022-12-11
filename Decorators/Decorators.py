
from Music_Theory.Chords import chord


# gis --> <gis gis'>

def melody_translate_DECORATOR(melody_py, reference, key_signature):
     i = 0                                                    # Posicion dentro del string de melodia
     staff = 0                                                # Numero de posicion del compas
     n_staff = melody_py.count("|")-1                         # Numero total de compases
     melody_ly = [str(" ")]*n_staff

     key_acc_notes = acc_notes(key_signature)
    
     # if posicion en string == pos de una barra + 2:
     #      cambiar funcion de traducir entera --> traducir + añadir octava
     # else:
     #      traducir normal
    
     while i < (len(melody_py)-2):
         space_tot = melody_py.find(" ", i, len(melody_py) - 1)     # Posicion del siguiente espacio con respecto a inicio
         space_loc = space_tot - i                                  # Posicion del siguiente espacio con respecto al compas



         for j in range(i,space_tot):  
                
            if melody_py[j] == 2:
             
                melody_ly += translate_octave(melody_py[j])

            else:

                if melody_py[j].isupper():                              # Si es letra mayuscula la pasa a minuscula
                    melody_ly[staff] += pitchly[melody_py[j]] 
                    if melody_py[j] in key_acc_notes:
                        melody_ly[staff] += acc_ly[key_acc_notes[len(key_acc_notes)-1]]

                elif melody_py[j] == "#" or melody_py[j]== "b":         # 
                    melody_ly[staff] += acc_ly[melody_py[j]]

                elif melody_py[j].isdigit():                            # Octavas
                    oct = int(melody_py[j]) - int(reference[1])
                    melody_ly[staff] += octaves[oct]

                elif melody_py[j] == "|":                               # Cambio de compas
                    staff += 1

                elif melody_py[j] == "^" or melody_py[j] == ".":
                    melody_ly[staff] += rythm_special[melody_py[j]]
                    melody_ly[staff] += " "
            
                else:                                                   # Ritmos
                    if melody_py[j+1] == "_":                           # Blanca tiene __ seguidos, necesita traduccion especial
                        melody_ly[staff] += rythm[melody_py[j:j+2]]
                        if melody_py[j+2] == "^" or melody_py[j+2] == ".":
                            melody_ly[staff] += rythm_special[melody_py[j+2]]
                            break
                        else:
                            break
                    else:
                        melody_ly[staff] += rythm[melody_py[j]]
                
                    melody_ly[staff] += " "

            

            melody_ly[staff] += " "            # A�ade espacio al final de la linea
            i += space_loc+1

     return(melody_ly)                                        # Melody traducida a ly





def translate_octave(melody_py):

    if melody_py[j].isupper():                              # Si es letra mayuscula la pasa a minuscula
                melody_ly[staff] += pitchly[melody_py[j]] 
                
                if melody_py[j] in key_acc_notes:
                    melody_ly[staff] += acc_ly[key_acc_notes[len(key_acc_notes)-1]]

                elif melody_py[j] == "#" or melody_py[j]== "b":         # 
                    melody_ly[staff] += acc_ly[melody_py[j]]

                    melody_ly[staff] += "<"
                    melody_ly[staff] += melody_py[j]
                    melody_ly[staff] += " "
                    melody_ly[staff] += melody_py[j]
                    melody_ly[staff] += "'"
                    melody_ly[staff] += ">"


                elif melody_py[j].isdigit():                            # Octavas
                    oct = int(melody_py[j]) - int(reference[1])
                    melody_ly[staff] += octaves[oct]

                elif melody_py[j] == "|":                               # Cambio de compas
                    staff += 1

                elif melody_py[j] == "^" or melody_py[j] == ".":
                    melody_ly[staff] += rythm_special[melody_py[j]]
                    melody_ly[staff] += " "
            
                else:                                                   # Ritmos
                    if melody_py[j+1] == "_":                           # Blanca tiene __ seguidos, necesita traduccion especial
                        melody_ly[staff] += rythm[melody_py[j:j+2]]
                        if melody_py[j+2] == "^" or melody_py[j+2] == ".":
                            melody_ly[staff] += rythm_special[melody_py[j+2]]
                            break
                        else:
                            break
                    else:
                        melody_ly[staff] += rythm[melody_py[j]]
                
                    melody_ly[staff] += " "


    return(melody_ly)

