from Music_Theory.Chords import interval

# Major and minor chord modes and intervals between scale notes

M_scale = ["M","m","m","M","M","m","d"]
M_scale_intervals = ["2M","3M","4P","5P","6M","7M"]

m_scale = ["m","d","M","m","m","M","M"]
m_scale_intervals = ["2M","3m","4P","5P","6m","7m"]

# Key signature and accidentals

key_sig = {"CM": [0,"#"], "Am":[0, "#"],  
           "GM": [1, "#"], "Em": [1, "#"], 
           "DM": [2, "#"], "Bm": [2, "#"], 
           "AM": [3, "#"], "Fm": [3,"#"],
           "EM": [4, "#"], "C#m": [4, "#"], 
           "BM": [5, "#"], "G#m": [5, "#"],
           "F#M": [6, "#"], "D#m": [6, "#"],
           "C#M": [7, "#"], "A#m": [7, "#"],
           "FM": [1, "b"], "Dm": [1, "b"],
           "BbM": [2, "b"], "Gm":[2, "b"],
           "EbM": [3, "b"], "Cm":[3, "b"],
           "AbM": [4, "b"], "Fm":[4, "b"],
           "DbM":[5, "b"], "Bbm":[5, "b"],
           "GbM":[6, "b"], "Ebm":[6, "b"],
           "CbM":[7, "b"], "Abm":[7, "b"]}


def key_scale(note, mode): 

    """
    key_scale It forms the scale corresponding to a key-signature 

    :param note: base note of the scale
    :param mode: mode of the scale (major/minor)
    :return: notes of the scale with their corresponding accidentals

    """

    scale = [str(" ")]*7
    scale[0] = note

    if mode == "M":
        inter_mode = M_scale_intervals
    elif mode == "m":
        inter_mode = m_scale_intervals

    for i in range(1,7):
        scale[i]= interval(inter_mode[i-1], note)

        if i>0 and scale[i][0] == scale[i-1][0]: # It changes between unison notes to make the scale more understandable [D# --> Eb or viceversa]
            scale[i] = interval("Change", scale[i])

    return scale



def acc_notes(key_signature):   

    """
    acc_notes Translates key signature into accidental notes through circle of fifths 

    :param key_signature: Key signature 
    :return: Accidental notes correponding to the key signature and its accidental symbol (# or b)

    """

    fifths_cycle = ["F", "C", "G", "D", "A", "E", "B" ]

    [number_acc, type_acc] = key_sig[key_signature]

    if type_acc == "#":
         key_acc_notes = fifths_cycle[0:number_acc]
         key_acc_notes += "#"
    else:
         key_acc_notes = fifths_cycle[len(fifths_cycle)-1:len(fifths_cycle)-number_acc -1:-1]
         key_acc_notes += "b"
     
    return key_acc_notes

