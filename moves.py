binn = open("combined.bin", "wb")
binn.write(open("_Decompressed_00000030.bin", "rb").read())
binn.write(open("_Decompressed_00000CB8.bin", "rb").read())
binn.write(open("_Decompressed_00001490.bin", "rb").read())
binn.write(open("_Decompressed_00001C14.bin", "rb").read())
binn.write(open("_Decompressed_000023B0.bin", "rb").read())
binn.write(open("_Decompressed_00002B30.bin", "rb").read())
binn.close()

binn2 = open("combined.bin", "rb")
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
    
    newFile = open("moveFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()
    