import subprocess

def compile_PDF():

    finish = ["\n >>",
              "\\layout {}",
              "\\midi {}",
              "}"]

    with open("prueba.txt", "a") as f:
        f.write('\n'.join(finish))

    path_to_Lylipond = "D:\\Program Files\\LilyPond\\usr\\bin\\lilypond.exe"
    path_to_file = "D:\\Descargas\\Aeroespecial\\MUSE 1\\Matematicas\\Programacion\\Programas\\Music Maker\\prueba.txt"
    
    return subprocess.call([path_to_Lylipond,path_to_file])