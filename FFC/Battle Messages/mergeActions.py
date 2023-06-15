import os

binn = open("0.bin", "rb")
whole = binn.read()
binn.close()

binn = open("0.bin", "wb")
binn.close()
binn = open("0.bin", "ab")
text = open("actionNames.txt", "rt").read()

binn.write(whole[0:16])
offset = int.from_bytes(whole[12:16], "little")
for i in range(140):
    offset = offset + os.stat("actionFiles/" + str(i + 1).zfill(3) + "_" + text.split("\n")[i] + ".bin").st_size
    binn.write(offset.to_bytes(4, "little"))
for i in range(141):
    binn.write(open("actionFiles/" + str(i + 1).zfill(3) + "_" + text.split("\n")[i] + ".bin", "rb").read())
binn.close()