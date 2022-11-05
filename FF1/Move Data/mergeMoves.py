import os
text = open("moveNames.txt", "rb").read().decode("UTF-8", errors = "ignore")

binn = open("0.bin", "rb")
section = binn.read(28)
binn.close()

binn = open("0.bin", "wb")
binn.write(section)
binn.close()

for i in range(1, 500):
    previousFile = open("0.bin", "rb")
    reading = previousFile.read()
    previousFile.close()
    size = os.stat("moveFiles/" + (text.split("\n") + ([chr(0x9FAF) + "Unused"] * 92))[i - 1] + "_" + str(i) + ".bin").st_size
    newOffset = size + int.from_bytes(reading[(24 + ((i - 1) * 4)):(28 + ((i - 1) * 4))], "little")
    binn = open("0.bin", "ab")
    binn.write(newOffset.to_bytes(4, "little"))
    binn.close()

binn = open("0.bin", "ab")
binn.write(bytes(8))
var = 32
binn.write(var.to_bytes(1, "little"))
binn.write(bytes(23))
for i in range(500):
    file = open("moveFiles/" + (text.split("\n") + ([chr(0x9FAF) + "Unused"] * 92))[i] + "_" + str(i + 1) + ".bin", "rb")
    binn.write(file.read())
    file.close()

binn.close()
