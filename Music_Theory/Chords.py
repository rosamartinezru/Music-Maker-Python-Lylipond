from Music_Theory.Intervals import interval


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



