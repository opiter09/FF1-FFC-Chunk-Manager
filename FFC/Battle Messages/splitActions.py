binn2 = open("0.bin", "rb")
bytE = binn2.read()

import os
try:
    os.mkdir("actionFiles")
except OSError as error:
    pass
        
for i in range(141):
    oldOffset = bytE[(12 + (i * 4)):(16 + (i * 4))]
    newOffset = bytE[(16 + (i * 4)):(20 + (i * 4))]
    if (i == 140):
        newOffset = (os.stat("0.bin").st_size).to_bytes(4, "little")
    
    newFile = open("actionFiles/" + str(i + 1).zfill(4) + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()


