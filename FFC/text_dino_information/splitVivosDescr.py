binn2 = open("0.bin", "rb")
bytE = binn2.read()
text = open("vivoNames.txt", "rt").read()

import os
try:
    os.mkdir("vivoDescrFiles")
except OSError as error:
    pass
        
for i in range(210):
    oldOffset = bytE[(16 + (i * 4)):(20 + (i * 4))]
    newOffset = bytE[(20 + (i * 4)):(24 + (i * 4))]
    if (i == 209):
        newOffset = len(bytE).to_bytes(4, "little")
    
    newFile = open("vivoDescrFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()
    
