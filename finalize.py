import subprocess

def compile_PDF():

    finish = ["\n >>",
              "\\layout {}",
              "\\midi {}",
              "}"]

    with open("prueba.txt", "a") as f:
        f.write('\n'.join(finish))

    path_to_Lylipond = "C:\\Program Files (x86)\\LilyPond\\usr\\bin\\lilypond.exe"
    path_to_file = "C:\\Users\\rosam\\OneDrive\\Escritorio\\Music-Maker-Python-Lylipond-tomas\\prueba.txt"
    
    return subprocess.call([path_to_Lylipond,path_to_file])
