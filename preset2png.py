# seigneurfuo
# 30 May 2017
# v0.02

import sys

def preset2png(inputFilename):
    """Extracting PNG data from a CM3D2 preset file"""
    
    # Input file
    inputFile = open(inputFilename, "rb")
    
    # Ouput file
    outputFilename = "%s.png" %inputFilename
    outputFile = open(outputFilename, "wb")

    # Start reading all the input file from the 25th position
    inputFile.seek(25, 0)

    content = inputFile.read()
    
    # Split where the PNG ends
    contentSplit = content.split(b"\x49\x45\x4e\x44\xae\x42")
    
    # And get the first part
    pngData = contentSplit[0]

    # Writing ouput file
    outputFile.write(pngData)
    outputFile.write(b"\x49\x45\x4e\x44\xae\x42")
        
    # Closing files
    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        preset2png(filename)
        
    else:
        print("Usage: preset2png.py <preset file>")
