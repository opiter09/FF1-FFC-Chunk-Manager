binn2 = open("0.bin", "rb")
bytE = binn2.read()
text = open("enemyNames.txt", "rb").read()

import os
try:
    os.mkdir("enemyNameFiles")
except OSError as error:
    pass
        
for i in range(73):
    oldOffset = bytE[(12 + (i * 4)):(16 + (i * 4))]
    newOffset = bytE[(16 + (i * 4)):(20 + (i * 4))]
    if (i == 72):
        newOffset = len(bytE).to_bytes(4, "little")
    
    listing = text.split((10).to_bytes(1, "little"))
    newFile = open("enemyNameFiles/" + str(i + 1).zfill(2) + "_" + listing[i].decode("UTF-8", errors = "ignore") + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()
    
