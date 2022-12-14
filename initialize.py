from Translator_py_ly.translator import *

def initialize_sheet():                     # Initial text of LilyPond coding, includes title, composer and instrument
    title = input("Title: ")
    composer = input("Composer: ")
    instrument = input("Instrument: ")

    initial = ["\\version \"2.22.2\" ", 
               "\\header {", 
               "title = \"" + title + "\"",
               "composer = \"" + composer + "\"",
               "}",
               "\\score {\\new PianoStaff \\with { instrumentName = \"" +instrument+ "\" }"]

    with open("prueba.txt", "w") as f:
        f.write('\n'.join(initial))
    return

def start_sheet(reference, key_signature):          # Time signature, metronome and clef
    time = input("Define a time signature (f.e. 3/4): ")

    figure, metronome = input("Define a metronome tempo (figure tempo): ").split()

    clef = input("Define a cleff (treble/alto/tenor/bass): ")

    anacruse = input("Do you want to start with an anacruse? (Yes/No): ")       # Anacruse start check

    if anacruse == "Yes":
        time_anacruse = input("Rythm anacruse (in quarter notes): ")
    else:
        time_anacruse = str(0)

    oct = int(reference[1]) - 3

    start = ["\n <<",
             "\\new Staff \\relative " + pitchly[reference[0]] + octaves[oct] + "{",
             "\\clef " + clef,
             "\\key " + key_ly(key_signature)[0] + " \\" + key_ly(key_signature)[1],
             "\\time " + time,
             "\\tempo " + figure + " = " + metronome,
             "\\partial " + time_anacruse + "\n"]

    with open("prueba.txt", "a") as f:
        f.write('\n'.join(start))

    return