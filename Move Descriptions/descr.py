binn = open("combined.bin", "wb")
binn.write(open("_Decompressed_00000020.bin", "rb").read())
binn.write(open("_Decompressed_00000CA0.bin", "rb").read())
binn.close()

binn2 = open("combined.bin", "rb")
bytE = binn2.read()
text = open("names.txt", "rt").read()

import os
try:
    os.mkdir("descrFiles")
except OSError as error:
    pass
        
for i in range(799):
    oldOffset = bytE[(16 + (i * 4)):(20 + (i * 4))]
    newOffset = bytE[(20 + (i * 4)):(24 + (i * 4))]
    
    newFile = open("descrFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()
    
