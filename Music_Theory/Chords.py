
# Numerical correspondence of notes and intervals

notes = {"C":0, "D":2,  "E":4, "F":5,  "G":7,  "A":9, "B":11, "C#":1, "D#":3,  "F#":6,  "G#":8,  "A#":10, "Db":1, "Eb":3, "Gb":6, "Ab":8, "Bb":10}

intervals = {"Unison":0,"2m":1, "2M":2, "3m":3, "3M":4, "4d":4, "4P":5, "4A":6, "5d":6, "5P":7, "5A":8, "6m":8, "6M":9, "7m":10, "7M":11, "Octave":12}

# Intervals between triads according to the mode of the chord

chords = {"M":      ["Unison", "3M", "5P"], 
          "m":      ["Unison", "3m", "5P"], 
          "d":      ["Unison", "3m", "5d"], 
          "A":      ["Unison", "3M", "5A"], 
          "S":      ["Unison", "4P", "5P"], 
          "M7":     ["Unison", "3M", "5P", "7M"], 
          "m7":     ["Unison", "3m", "5P", "7m"], 
          "D7":     ["Unison", "3M", "5P", "7m"], 
          "d7":     ["Unison", "3m", "5d", "6M"], 
          "H7":     ["Unison", "3m", "5d", "7m"], 
          "Mm7":    ["Unison", "3m", "5P", "7M"], 
          "Octave": ["Unison", "3M", "5A", "Octave"]
          }


def chord(note, chord_type):        # Returns the notes of a chord given the base note and the chord type

    """
    chord It forms a chord from a base note and a chord type 

    :param note: base note of the chord
    :param chord_type: type of chord (see chords dictionary)
    :return: notes of the chord with their corresponding accidentals

    """
    
    acorde = chords[chord_type]     

    if len(chord_type) == 1:
        chord = [interval(acorde[0], note), interval(acorde[1], note), interval(acorde[2], note)]

    else:
        chord = [interval(acorde[0], note), interval(acorde[1], note), interval(acorde[2], note), interval(acorde[3], note)]

    return chord


def interval(inter, base_note):

    """
    interval It forms a chosen interval over a base note

    :param inter: Interval type (see intervals dictionary)
    :param base_note: Note over which the interval is formed
    :return: The new note which correponds to the selected interval

    """
    
    if inter == "Change":
        notes_copy = notes.copy()
        notes_copy.pop(base_note)
        new_note = notes[base_note] + intervals["Unison"] 

    else:
        new_note = notes[base_note] + intervals[inter]

        if new_note > 11:
            new_note -= 12

    key_list = list(notes.keys())
    val_list = list(notes.values())  

    result_note = (str(key_list[val_list.index(new_note)]))

    return result_note