import os

if (os.path.exists("./moveDescrFiles/") == True):
    text = open("moveNames.txt", "rt").read()

    binn = open("0.bin", "rb")
    section = binn.read(16)
    binn.close()

    binn = open("0.bin", "wb")
    binn.write(section)
    binn.close()

    binn = open("0.bin", "ab")
    var = 3213
    binn.write(var.to_bytes(4, "little"))
    binn.close()
    for i in range(1, 799):
        previousFile = open("0.bin", "rb")
        reading = previousFile.read()
        previousFile.close()
        size = os.stat("moveDescrFiles/" + text.split("\n")[i - 1] + "_" + str(i) + ".bin").st_size
        newOffset = size + int.from_bytes(reading[(16 + ((i - 1) * 4)):(20 + ((i - 1) * 4))], "little")
        binn = open("0.bin", "ab")
        binn.write(newOffset.to_bytes(4, "little"))
        binn.close()

    binn = open("0.bin", "ab")
    binn.write(bytes(1))
    for i in range(799):
        binn.write(open("moveDescrFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "rb").read())            
    binn.close()