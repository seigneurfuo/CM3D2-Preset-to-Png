# seigneurfuo
# 30 avril 2017
# v0.01

import sys

dossier = sys.argv[1]
def preset2png(INFILENAME):
    fo = open(INFILENAME, "rb") # Fichier d'entrée
    fi = open("%s.png" %INFILENAME, "wb") # Fichier de sortie

    fo.seek(25, 0) # Commencement à la position

    content = fo.read() # Lecture de tout le document
    contentSplit = content.split(b"\x49\x45\x4e\x44\xae\x42")
    pngData = contentSplit[0]


    fi.write(pngData)
    fi.write(b"\x49\x45\x4e\x44\xae\x42")
        
    fo.close()
    fi.close()

if __name__ == "__main__":
    import glob, os
    
    for file in glob.glob("%s/*.preset" %dossier):
        print(file)
        preset2png(file)
