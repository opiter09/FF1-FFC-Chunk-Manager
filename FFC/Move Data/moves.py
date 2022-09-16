binn2 = open("0.bin", "rb")
bytE = binn2.read()
text = open("names.txt", "rt").read()

import os
try:
    os.mkdir("moveFiles")
except OSError as error:
    pass
        
for i in range(799):
    oldOffset = bytE[(20 + (i * 4)):(24 + (i * 4))]
    newOffset = bytE[(24 + (i * 4)):(28 + (i * 4))]
    
    newFile = open("moveFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()
    
