import os

binn = open("combined.bin", "rb")
whole = binn.read()
binn.close()
binn = open("combined.bin", "rb")
section = binn.read(20)
binn.close()
binn = open("combined.bin", "rb")
section2 = binn.read()[856:952]
binn.close()

binn = open("combined.bin", "wb")
binn.write(section)
binn.close()

binn = open("combined.bin", "ab")
text = open("vivoNames.txt", "rt").read()
offset = int.from_bytes(whole[16:20], "little")
for i in range(209):
    offset = offset + os.stat("vivoDescrFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin").st_size
    binn.write(offset.to_bytes(4, "little"))
binn.write(section2)
for i in range(210):
    binn.write(open("vivoDescrFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin", "rb").read())
binn.write(bytes(24))
binn.close()

binn = open("combined.bin", "rb").read()
open("_Decompressed_00000028.bin", "wb").write(binn[0:8192])
open("_Decompressed_00001028.bin", "wb").write(binn[8192:16384])
open("_Decompressed_00001F70.bin", "wb").write(binn[16384:24576])
open("_Decompressed_00002DFC.bin", "wb").write(binn[24576:os.stat("combined.bin").st_size])