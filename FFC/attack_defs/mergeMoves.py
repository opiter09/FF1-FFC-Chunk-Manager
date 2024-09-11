import os

if (os.path.exists("./moveFiles/") == True):
    text = open("moveNames.txt", "rt").read()

    binn = open("0.bin", "rb")
    section = binn.read(24)
    binn.seek(3216)
    section2 = binn.read(28)
    binn.seek(int.from_bytes(section2[0:4], "little"))
    section3 = binn.read(24)
    binn.close()

    binn = open("0.bin", "wb")
    binn.write(section)
    binn.close()

    for i in range(1, 800):
        previousFile = open("0.bin", "rb")
        reading = previousFile.read()
        previousFile.close()
        size = os.stat("moveFiles/" + text.split("\n")[i - 1] + "_" + str(i) + ".bin").st_size
        newOffset = size + int.from_bytes(reading[(20 + ((i - 1) * 4)):(24 + ((i - 1) * 4))], "little")
        binn = open("0.bin", "ab")
        binn.write(newOffset.to_bytes(4, "little"))
        binn.close()

    binn = open("0.bin", "ab")
    binn.write(section2[4:28])

    binn = open("0.bin", "ab")
    for i in range(799):
        binn.write(open("moveFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "rb").read())
    binn.write(section3)
    binn.close()
