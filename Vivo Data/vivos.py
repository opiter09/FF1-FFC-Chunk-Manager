binn = open("combined.bin", "wb")
binn.write(open("_Decompressed_00000034.bin", "rb").read())
binn.write(open("_Decompressed_00000DB8.bin", "rb").read())
binn.write(open("_Decompressed_00001AF4.bin", "rb").read())
binn.write(open("_Decompressed_00002808.bin", "rb").read())
binn.write(open("_Decompressed_00003714.bin", "rb").read())
binn.write(open("_Decompressed_0000466C.bin", "rb").read())
binn.write(open("_Decompressed_000054F4.bin", "rb").read())
binn.close()

binn2 = open("combined.bin", "rb")
bytE = binn2.read()
text = open("vivoNames.txt", "rt").read()

import os
try:
    os.mkdir("vivoFiles")
except OSError as error:
    pass
        
for i in range(210):
    oldOffset = bytE[(44 + (i * 4)):(48 + (i * 4))]
    newOffset = bytE[(48 + (i * 4)):(52 + (i * 4))]
    if (i == 209):
        newOffset = 53916
        newOffset = newOffset.to_bytes(4, "little")
    
    newFile = open("vivoFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()
    
