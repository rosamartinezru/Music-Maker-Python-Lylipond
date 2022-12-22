# Numerical correspondence of notes and intervals

notes = {"C":0, "D":2,  "E":4, "F":5,  "G":7,  "A":9, "B":11, "C#":1, "D#":3,  "F#":6,  "G#":8,  "A#":10, "Db":1, "Eb":3, "Gb":6, "Ab":8, "Bb":10, "Cb":11, "B#":0, "E#":5, "Fb":4}

intervals = {"Unison":0,"2m":1, "2M":2, "3m":3, "3M":4, "4d":4, "4P":5, "4A":6, "5d":6, "5P":7, "5A":8, "6m":8, "6M":9, "7m":10, "7M":11, "Octave":12}

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

        key_list = list(notes_copy.keys())
        val_list = list(notes_copy.values())  

        result_note = (str(key_list[val_list.index(new_note)]))

    else:
        new_note = notes[base_note] + intervals[inter]

        if new_note > 11:
            new_note -= 12

        key_list = list(notes.keys())
        val_list = list(notes.values())  

        result_note = (str(key_list[val_list.index(new_note)]))

    return result_note
