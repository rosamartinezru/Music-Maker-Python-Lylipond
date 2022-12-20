import subprocess
from Translator_py_ly.dictionaries_lily import pitchly, octaves, key_ly

def header(reference, key_signature):                     # Initial text of LilyPond coding, includes title, composer and instrument

    title = input("Title: ")
    composer = input("Composer: ")
    instrument = input("Instrument: ")

    sheet_start = ["\\version \"2.22.2\" ", 
               "\\header {", 
               "title = \"" + title + "\"",
               "composer = \"" + composer + "\"",
               "}",
               "\\score {\\new PianoStaff \\with { instrumentName = \"" +instrument+ "\" }"]

    time = input("Define a time signature (f.e. 3/4): ")

    figure, metronome = input("Define a metronome tempo (figure tempo): ").split()

    clef = input("Define a cleff (treble/alto/tenor/bass): ")

    anacruse = input("Do you want to start with an anacruse? (Yes/No): ")       # Anacruse start check

    if anacruse == "Yes":
        time_anacruse = input("Rythm anacruse (in quarter notes): ")
    else:
        time_anacruse = str(0)

    oct = int(reference[1]) - 3

    melody_start = ["\n <<",
             "\\new Staff \\relative " + pitchly[reference[0]] + octaves[oct] + "{",
             "\\clef " + clef,
             "\\key " + key_ly(key_signature)[0] + " \\" + key_ly(key_signature)[1],
             "\\time " + time,
             "\\tempo " + figure + " = " + metronome,
             "\\partial " + time_anacruse + "\n"]


    return sheet_start, melody_start


def compile_PDF(full_text):

    finish = ["\n >>",
              "\\layout {}",
              "\\midi {}",
              "}"]

    with open("cancion.txt", "w") as f:
        f.write('\n'.join(full_text[0]))
    with open("cancion.txt", "a") as f:
        f.write('\n'.join(full_text[1]))
        f.write('\n'.join(full_text[2]))
        f.write('\n'.join(full_text[3]))
        f.write('\n'.join(finish))

    path_to_Lylipond = "C:\\Program Files (x86)\\LilyPond\\usr\\bin\\lilypond.exe"
    path_to_file = "C:\\Users\\rosam\\OneDrive\\Escritorio\\MUSE-1.1\\Ampliación de Matemáticas -1\\Music-Maker\\cancion.txt"
    
    return subprocess.call([path_to_Lylipond,path_to_file])
