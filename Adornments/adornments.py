from Music_Theory.Chords import chord

# gis'8 --> <gis' gis''>8
# <gis'8 gis''8>

def adorn_all_octaves(melody_ly):

    decorated_melody = [str(" ")]*len(melody_ly)

    for n in (range(len(melody_ly)-1)):

        bar = melody_ly[n]                      # string en linea n(compas)

        decorated_melody[n] = adorn_bar(bar)



    return decorated_melody

def adorn_bar(bar):

    i = 0
    bar_decorated = " "

    while i < len(bar):               # recorre el string del compas
            
            octava = " "

            if bar[i] != " ":                   # detecta el primer caracter que no es un espacio
                j = bar.find(" ",i,len(bar))    # CALCULAR posicion del siguiente espacio
                note = bar[i:j]           # primera nota = cosas entre 2 espacios p.e cis'4

                if (note[0] == '~') or (note[0] == 'r') or (note[0] == "."):
                    octava = note
                else:        
                    for m in note:  
                       if m == "'":
                           mPos = note.find("'")
                           octava = "<" + note[0:mPos+1] + " " + note[0:mPos+1] + " " + ">" + note[mPos+1:len(note)]
                           break
                       elif m == ",": 
                           mPos = note.find(",")
                           octava = "<" + note[0:mPos+1] + " " + note[0:mPos]  + ">" + note[mPos+1:len(note)]
                           break
                       elif m.isdigit():
                           mPos = note.find(m)
                           note_clean = note[0:len(note)-1]
                           octava = "<" + note_clean[0:mPos] + " " + note_clean[0:mPos] + "'"  + ">" + note[mPos:len(note)]
                           break
                       else:
                           if m == note[-1]:
                               octava = "<" + note + " " +  note[0] + "'" + ">"
                               break       # termina el bucle

                i += len(note) 

            i += 1

            bar_decorated += octava + " "

    return(bar_decorated)



def adorn_first_note_octave(melody_ly):     # Coge nota p.e. a4 y saca <a4 a4'> 

   # n_bars = len(melody_ly)

    melody_ly_decorator = [str(" ")]*len(melody_ly)

    for n in range(len(melody_ly)):
        if n>0:
            bar_prev = melody_ly[n-1]
        bar = melody_ly[n]                      # string en linea n(compas)
        for i in range(len(bar)):               # recorre el string del compas
            if bar[i] != " ":                   # detecta el primer caracter que no es un espacio
                j = bar.find(" ",i,len(bar))    # CALCULAR posicion del siguiente espacio
                first_note = bar[i:j]           # primera nota = cosas entre 2 espacios p.e cis'4
                print(first_note)

                if n>0 and bar_prev[-3] == "~":
                    octava = first_note 
                elif first_note[0] != "r":
                   for m in first_note:  
                       if m == "'":
                           mPos = first_note.find("'")
                           octava = "<" + first_note[0:mPos+1] + " " + first_note[0:mPos+1] + " " + ">" + first_note[mPos+1:len(first_note)]
                           break
                       elif m == ",": 
                           mPos = first_note.find(",")
                           octava = "<" + first_note[0:mPos+1] + " " + first_note[0:mPos]  + ">" + first_note[mPos+1:len(first_note)]
                           break
                       elif m.isdigit():
                           mPos = first_note.find(m)
                           first_note_clean = first_note[0:len(first_note)-1]
                           octava = "<" + first_note_clean[0:mPos] + " " + first_note_clean[0:mPos] + "'"  + ">" + first_note[mPos:len(first_note)]
                           break
                       else:
                           if m == first_note[-1]:
                               octava = "<" + first_note + " " +  first_note[0] + "'" + ">"
                               break       # termina el bucle
                else:        
                    octava = first_note
                print(octava)
                break
                    

        melody_ly_decorator[n] = "  " + octava + bar[j:len(bar)]

    return(melody_ly_decorator) 
