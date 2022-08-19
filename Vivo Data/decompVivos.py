import os

binn = open("combined.bin", "rb")
whole = binn.read()
binn.close()
binn = open("combined.bin", "rb")
section = binn.read(48)
binn.close()

binn = open("combined.bin", "wb")
binn.write(section)
binn.close()

binn = open("combined.bin", "ab")
text = open("vivoNames.txt", "rt").read()
offset = int.from_bytes(whole[44:48], "little")
for i in range(209):
    offset = offset + os.stat("vivoFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin").st_size
    binn.write(offset.to_bytes(4, "little"))
binn.write(whole[884:1072])
for i in range(210):
    binn.write(open("vivoFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin", "rb").read())
binn.close()

binn = open("combined.bin", "rb").read()
open("_Decompressed_00000034.bin", "wb").write(binn[0:8192])
open("_Decompressed_00000DB8.bin", "wb").write(binn[8192:16384])
open("_Decompressed_00001AF4.bin", "wb").write(binn[16384:24576])
open("_Decompressed_00002808.bin", "wb").write(binn[24576:32768])
open("_Decompressed_00003714.bin", "wb").write(binn[32768:40960])
open("_Decompressed_0000466C.bin", "wb").write(binn[40960:49152])
open("_Decompressed_000054F4.bin", "wb").write(binn[49152:os.stat("combined.bin").st_size])