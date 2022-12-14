from Translator_py_ly.dictionaries import *
from Translator_py_ly.translator import key_ly
from Music_Theory.Chords import chord, interval
from Music_Theory.Scales_and_modes import M_scale, m_scale, key_scale, M_scale_intervals, m_scale_intervals, acc_notes
from numpy import zeros, array, size, amax, argmax, delete, multiply
import copy

def autobass(melody_py, reference, key_signature):           
    
    bass_ly = melody_bass_translate(melody_py, key_signature)

    start_bass = ["\n <<",
                  "\\new Staff \\relative " + "{",
                  "\\clef bass",
                  "\\key " + key_ly(key_signature)[0] + " \\" + key_ly(key_signature)[1],
                  "\\chordmode " + "{"]

    finish_bass = [ "\n" + "}" + "}",
                   ">>"]
                  
    with open("prueba.txt", "a") as f:
        f.write('\n'.join(start_bass))
        f.write('\n'.join(bass_ly))
        f.write('\n'.join(finish_bass))

    return 

def melody_bass_translate(melody_py, key):

    """
    melody_bass_translate Calls step by step the automatic bass formation

    :param melody_py: Input melody in python language
    :param key: Input key-signature
    :return: The generated bass in lylipond language, ready to be written into the .txt

    """

    n_staff = melody_py.count("|")-1                       
    d_start = 0                                              
    chords = " "                                                                                                
    chord_ly= [str(" ")]*n_staff
    last_saved = 0
   

    for n in range(n_staff):

        d_final = melody_py.find("|", d_start, len(melody_py) - 1)            
        bar = melody_py[d_start:d_final] # Sectioning the melody string into bars
        d_start = d_final + 2                                                      

        staff_note = staff_notes(bar) # Notes on the bar
        bass_chord = select_chord(staff_note, key, "First", None ) # Most probable chord of the measure
        bass_rythm, last_saved = staff_rythm(bar, last_saved) # Bar rythm
        bass_correction = chord_correction(staff_note, bass_rythm, bass_chord, key) # Chord correction
        for m in range(len(bass_correction)):
            chord_ly[n] += bass_correction[m] + " "

    return chord_ly




def staff_notes(bar):
    
     """
     staff_notes Selects and separates the notes of the measure, with their repective accidentals

     :param bar: Bar notes and rythm (string)
     :return: List with the notes of the bar

     """

     tied_quarter_notes = 0
     counter = 0

     for j in range(len(bar)-1):
         if bar[j] == "-" and bar[j+1].isupper():
            tied_quarter_notes += 1   # The second note of a tied quarter note is not important to auto generate the bass

     staff_notes = [str(" ")]*(sum(1 for char in bar if char.isupper()) - tied_quarter_notes)   

     for j in range(len(bar)):
            
            if j>0:
                if bar[j-1] == "-":
                    continue
            if bar[j].isupper():
                staff_notes[counter] = bar[j]
                counter += 1 

            if bar[j] == "#" or bar[j]== "b":
                staff_notes[counter-1] += bar[j]

     return staff_notes


def staff_rythm(bar, last):

     """
     staff_rythm Selects and separates the rythms of the measure

     :param bar: Bar notes and rythm (string)
     :param last: Last rythm of the last bar, in case it is needed for the following note
     :return: List with the rythms of the bar

     """

     staff_note = staff_notes(bar)
     counter = 0

     staff_rythm = [str(" ")]*sum(1 for char in bar if char.isupper())  
     
     for j in range(len(bar)):

         if bar[j] == " ":
             if bar[j-1] not in rythm and bar[j-1] not in rythm_special:
                
                if counter == 0:
                    staff_rythm[counter] = last
                else:
                    staff_rythm[counter] = staff_rythm[counter-1]

                counter += 1

         elif bar[j] in rythm_special:
             staff_rythm[counter-1] += rythm_special[bar[j]]

         elif bar[j] in rythm:
             if j > 0:
                if bar[j-1] == "_" and bar[j] == "_":                           
                        staff_rythm[counter-1] = rythm[bar[j-1:j+1]]
                        continue
             staff_rythm[counter] = rythm[bar[j]]
             counter += 1

     last_saved = staff_rythm[len(staff_rythm)-1] 
     bass_rythm = staff_rythm.copy()

     tied_quarter_notes = 0
     counter = 0

     for j in range(len(bar)-1):
         if bar[j] == "-" and bar[j+1].isupper():
            tied_quarter_notes += 1

     staff_rythm = [str(" ")]*(sum(1 for char in bar if char.isupper()) - tied_quarter_notes)  
     step = 0

     for i in range(len(bass_rythm)): # Changes the eight tied notes to a quarter note
         if i>0 and bass_rythm[i]==bass_rythm[i-1] and int(bass_rythm[i][0])>=8 and staff_note[counter-1] != "R" and "~" not in bass_rythm[i] and step < 1:
            staff_rythm[counter-1] = "4"
            step +=1
            continue
            
         else:
            staff_rythm[counter] = bass_rythm[i]
            counter += 1
         if step == 1: # If there are more than one eight tied notes followed by each other
                
             step = 0


     return staff_rythm, last_saved

 
def select_chord(staff_notes, key, other, out_note):

    """
    select_chord Selects the most probable chord of the measure or the necessary correction chord for a note

    :param staff_notes: Notes on the bar
    :param key: Input key-signature
    :param other: "First" time selecting the chord or "Second" when it performs corrections
    :param out_note: Out of the chord note in which the correction is performed (only with "Second")
    :return: Name of the most probable chord of the measure or name of the bass chord correction

    """

    if key[len(key)-1] == "M":
        scale_mode = M_scale
    else:
        scale_mode = m_scale
    
    accidental_notes = acc_notes(key)
    first, third, fourth, fifth = primary_chord(key)
    primary_matrix = array([first, third, fourth, fifth])

    if accidental_notes[len(accidental_notes)-1].isupper() == False:
        for i in range(4):
            for j in range(3):
                if len(primary_matrix[i][j])==2 and primary_matrix[i][j] not in accidental_notes:
                    primary_matrix[i][j] = interval("Change", primary_matrix[i][j])

    counter_chord = zeros([4,1])
    weight = array([[1], [0.4], [0.5], [0.8]])  # Weight of the different chords in an ordinary song
    
    for w in range(len(staff_notes)):
        if staff_notes[w] in accidental_notes:
            staff_notes[w] += accidental_notes[len(accidental_notes)-1]

    if other == "First": # Most probable chord of the measure
        for i in range(size(staff_notes)):
            if staff_notes[i] != "R":
                for j in range(4):
                    if staff_notes[i] in primary_matrix[j][:]:
                        counter_chord[j,0] += 1

        counter_chord = multiply(counter_chord,weight)

        indx_max = argmax(counter_chord)

        if len(primary_matrix[indx_max][0]) == 2:
            selected_chord = pitchly[primary_matrix[indx_max][0][0]] + primary_matrix[indx_max][0][1]
        else:
            selected_chord = pitchly[primary_matrix[indx_max][0]] 

    elif other == "Second": # Chord correction for a note out of the most probable chord 

        note_grade = note_grades(key, out_note) 

        out_chord = chord(out_note, scale_mode[note_grade-1])

        for w in range(len(out_chord)):
            if len(out_chord[w])==2 and accidental_notes[len(accidental_notes)-1] not in out_chord[w]:
                out_chord[w] = interval("Change", out_chord[w])

        for i in range(len(out_chord)):
            if out_chord[i] in primary_matrix[i][:]:
                counter_chord[i] += 1
                if out_chord[0] in primary_matrix[i][0]:
                    counter_chord[i] += 1

        indx_max = argmax(counter_chord)

        if len(primary_matrix[indx_max][0]) == 2:
            selected_chord = pitchly[primary_matrix[indx_max][0][0]] + primary_matrix[indx_max][0][1]
        else:
            selected_chord = pitchly[primary_matrix[indx_max][0]]

    return selected_chord



def chord_correction(staff_note, bass_rythm, bass_chord_initial, key):

    """
    chord_correction Makes the correponding changes in the bass chord in order to make it consonant 

    :param staff_notes: Notes on the bar
    :param key: Input key-signature
    :param bass_rythm: Rythm of the bar notes
    :param bass_chord_initial: Most probable chord of the measure
    :return: List with the chords and its respective rythms for every single note of the measure

    """

    if key[len(key)-1] == "M":
        scale_mode = M_scale
    else:
        scale_mode = m_scale

    bass_correction = [str(" ")]*len(bass_rythm)
    accidental_notes = acc_notes(key)

    for j in range(len(bass_rythm)):

        if len(bass_chord_initial) == 1:
            bass_chord_notes = chord(bass_chord_initial.upper(), scale_mode[note_grades(key, bass_chord_initial[0].upper())-1])
        else:
            bass_chord_notes = chord(bass_chord_initial[0].upper() + bass_chord_initial[1], scale_mode[note_grades(key, bass_chord_initial[0].upper())-1])
        
        for w in range(len(bass_chord_notes)):
            if len(bass_chord_notes[w])==2 and accidental_notes[len(accidental_notes)-1] not in bass_chord_notes[w]:
                bass_chord_notes[w] = interval("Change", bass_chord_notes[w])

        counter_notes = 0

        if len(bass_chord_initial)==2:
              bass_chord = bass_chord_initial[0] + acc_ly[bass_chord_initial[1]]
        else:
              bass_chord = bass_chord_initial

        if staff_note[j] != "R":
            note_grade = note_grades(key, staff_note[j])

            if staff_note[j] not in bass_chord_notes:
                self_chord = chord(staff_note[j], scale_mode[note_grade-1])

                for w in range(len(self_chord)):
                    if len(self_chord[w])==2 and accidental_notes[len(accidental_notes)-1] not in self_chord[w]:
                        self_chord[w] = interval("Change", self_chord[w])

                for n in range(3):
                    if self_chord[n] in bass_chord_notes:
                        counter_notes += 1

                if counter_notes == 2:               
                    if scale_mode[note_grades(key, bass_chord_initial[0].upper())-1] != "M":
                        
                        bass_correction[j] = bass_chord + "," + bass_rythm[j] + ":" + scale_mode[note_grades(key, bass_chord_initial[0].upper())-1]
                    else:
                        bass_correction[j] = bass_chord + "," + bass_rythm[j]
                else:
                    bass_chord_new = select_chord(staff_note, key, "Second", staff_note[j])
                    if len(bass_chord_new) == 2:
                        bass_new = bass_chord_new[0] + acc_ly[bass_chord_new[1]]
                    else:
                        bass_new = bass_chord_new

                    if scale_mode[note_grades(key, bass_chord_new[0].upper())-1] != "M":
                        bass_correction[j] = bass_new + "," + bass_rythm[j] + ":" + scale_mode[note_grades(key, bass_chord_new[0].upper())-1]
                    else:
                        bass_correction[j] = bass_new + "," + bass_rythm[j]
            else:
                if scale_mode[note_grades(key, bass_chord_initial[0].upper())-1] != "M":
                    bass_correction[j] = bass_chord + "," + bass_rythm[j] + ":" + scale_mode[note_grades(key, bass_chord_initial[0].upper())-1]
                else:
                    bass_correction[j] = bass_chord + "," + bass_rythm[j]

            if "~" in bass_correction[j]:
                bass_correction[j] = bass_correction[j].replace("~", "")
                bass_correction[j] += "~"
        else:        
            bass_correction[j] = "r" + bass_rythm[j]

    return bass_correction


def note_grades(key, note):

    """
    note_grades Calculates the number of the note inside the scale of the tonality

    :param note: Input note 
    :param key: Input key-signature
    :return: Position of the note on the corresponding scale

    """

    accidental_notes = acc_notes(key)

    if note in accidental_notes:
            note_grade = key_scale(key[:(len(key)-1)],key[len(key)-1]).index(note+accidental_notes[len(accidental_notes)-1]) +1
    else:
            note_grade = key_scale(key[:(len(key)-1)],key[len(key)-1]).index(note) +1

    return note_grade

def primary_chord(key):        

    """
    primary_chord Makes the first, third, fourth and fifth chord of the input key-signature

    :param key: Input key-signature
    :return: Lists with chord notes

    """
    if key[len(key)-1] == "M":
        scale_mode = M_scale
        interval_mode = M_scale_intervals
    else:
        scale_mode = m_scale
        interval_mode = m_scale_intervals

    if len(key) ==2:     
        first = chord(key[0], scale_mode[0])
        third = chord(interval(interval_mode[1], key[0]), scale_mode[2])
        fourth = chord(interval(interval_mode[2], key[0]), scale_mode[3])
        fifth = chord(interval(interval_mode[3], key[0]), scale_mode[4])

    else:
        first = chord(key[0:2], scale_mode[0])
        third = chord(interval(interval_mode[1], key[0:2]), scale_mode[2])
        fourth = chord(interval(interval_mode[2], key[0:2]), scale_mode[3])
        fifth = chord(interval(interval_mode[3], key[0:2]), scale_mode[4])

    return first, third, fourth, fifth
