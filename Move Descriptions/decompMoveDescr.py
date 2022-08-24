import os
text = open("names.txt", "rt").read()

binn = open("combined.bin", "rb")
section = binn.read(16)
binn.close()

binn = open("combined.bin", "wb")
binn.write(section)
binn.close()

binn = open("combined.bin", "ab")
var = 3213
binn.write(var.to_bytes(4, "little"))
binn.close()
for i in range(1, 799):
    previousFile = open("combined.bin", "rb")
    reading = previousFile.read()
    previousFile.close()
    size = os.stat("moveDescrFiles/" + text.split("\n")[i - 1] + "_" + str(i - 1) + ".bin").st_size
    newOffset = size + int.from_bytes(reading[(16 + ((i - 1) * 4)):(20 + ((i - 1) * 4))], "little")
    binn = open("combined.bin", "ab")
    binn.write(newOffset.to_bytes(4, "little"))
    binn.close()

binn = open("combined.bin", "ab")
binn.write(bytes(1))
for i in range(799):
    binn.write(open("moveDescrFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin", "rb").read())            
binn.close()

binn = open("combined.bin", "rb").read()
open("_Decompressed_00000020.bin", "wb").write(binn[0:8192])
open("_Decompressed_00000CA0.bin", "wb").write(binn[8192:os.stat("combined.bin").st_size])
