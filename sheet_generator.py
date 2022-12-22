import subprocess
from Translator_py_ly.dictionaries_lily import pitchly, octaves, key_ly

def header(header_input):                     # Initial text of LilyPond coding, includes title, composer and instrument
    key_signature = header_input[4]
    print(header_input[4])
    title = header_input[0]
    composer = header_input[1]
    instrument = header_input[2]

    sheet_start = ["\\version \"2.22.2\" ", 
               "\\header {", 
               "title = \"" + title + "\"",
               "composer = \"" + composer + "\"",
               "}",
               "\\score {\\new PianoStaff \\with { instrumentName = \"" +instrument+ "\" }"]

    time = header_input[6]

    figure, metronome = header_input[5], header_input[7]

    clef = header_input[8]
    anacruse = header_input[9]       # Anacruse start check

    if anacruse == "Yes":
        time_anacruse = header_input[10]
    else:
        time_anacruse = str(0)
    
    oct = int((header_input[3])[1]) - 3

    melody_start = ["\n <<",
             "\\new Staff \\relative " + pitchly[(header_input[3])[0]] + octaves[oct] + "{",
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
    path_to_file = "C:\\Users\\Usuario\\Documents\\MUSE\\Primero\\Ampliacion de matematicas\\Juan Antonio\\Music-Maker-Python-Lylipond-order_fix\\cancion.txt"
    
    return subprocess.call([path_to_Lylipond,path_to_file])
