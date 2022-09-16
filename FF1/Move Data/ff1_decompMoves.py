import os
text = open("ff1_names.txt", "rb").read().decode("UTF-8", errors = "ignore")

binn = open("0.bin", "rb")
section = binn.read(28)
binn.seek(1660)
section2 = binn.read(396)
binn.seek(27212)
section3 = binn.read(2944)
binn.close()

binn = open("0.bin", "wb")
binn.write(section)
binn.close()

for i in range(1, 409):
    previousFile = open("0.bin", "rb")
    reading = previousFile.read()
    previousFile.close()
    size = os.stat("moveFiles/" + text.split("\n")[i - 1] + "_" + str(i) + ".bin").st_size
    newOffset = size + int.from_bytes(reading[(24 + ((i - 1) * 4)):(28 + ((i - 1) * 4))], "little")
    binn = open("0.bin", "ab")
    binn.write(newOffset.to_bytes(4, "little"))
    binn.close()

binn = open("0.bin", "ab")
binn.write(section2)

binn = open("0.bin", "ab")
text = open("ff1_names.txt", "rb").read().decode("UTF-8", errors = "ignore")
for i in range(408):
    file = open("moveFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "rb")
    binn.write(file.read())
    file.close()

binn.write(section3)
binn.close()
