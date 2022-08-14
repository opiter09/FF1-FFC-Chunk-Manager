binn = open("combined.bin", "rb")
section = binn.read(3244)
binn.seek(42556)
section2 = binn.read(24)
binn.close()

binn = open("combined.bin", "wb")
binn.write(section)
binn.close()

binn = open("combined.bin", "ab")
text = open("names.txt", "rt").read()
for i in range(799):
    binn.write(open("moveFiles/" + text.split("\n")[i] + "_" + str(i) + ".bin", "rb").read())
binn.write(section2)
binn.close()

binn = open("combined.bin", "rb").read()
open("_Decompressed_00000030.bin", "wb").write(binn[0:8192])
open("_Decompressed_00000CB8.bin", "wb").write(binn[8192:16384])
open("_Decompressed_00001490.bin", "wb").write(binn[16384:24576])
open("_Decompressed_00001C14.bin", "wb").write(binn[24576:32768])
open("_Decompressed_000023B0.bin", "wb").write(binn[32768:40960])
open("_Decompressed_00002B30.bin", "wb").write(binn[40960:42580])