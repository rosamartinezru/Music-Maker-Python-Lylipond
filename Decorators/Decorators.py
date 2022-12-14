
from Music_Theory.Chords import chord


# gis'8 --> <gis' gis''>8
# <gis'8 gis''8>

def decorator_octava(melody_ly):     # Coge nota p.e. a4 y saca <a4 a4'> 

   # n_bars = len(melody_ly)

    melody_ly_decorator = [str(" ")]*len(melody_ly)

    for n in range(len(melody_ly)):
        bar = melody_ly[n]                      # string en linea n(compas)
        for i in range(len(bar)):               # recorre el string del compas
            if bar[i] != " ":                   # detecta el primer caracter que no es un espacio
                j = bar.find(" ",i,len(bar))    # CALCULAR posicion del siguiente espacio
                first_note = bar[i:j]           # primera nota = cosas entre 2 espacios p.e cis'4
                
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
                break
        melody_ly_decorator[n] = "  " + octava + bar[j:len(bar)]

    return(melody_ly_decorator) 