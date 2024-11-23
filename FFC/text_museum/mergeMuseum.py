import os

if (os.path.exists("./museumFiles/") == True):
    binn = open("0.bin", "rb")
    whole = binn.read()
    binn.close()
    binn = open("0.bin", "rb")
    section = binn.read(16)
    binn.close()

    binn = open("0.bin", "wb")
    binn.write(section)
    binn.close()

    binn = open("0.bin", "ab")
    text = open("vivoNames.txt", "rt").read()
    offset = int.from_bytes(whole[12:16], "little")
    for i in range(209):
        offset = offset + os.stat("museumFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin").st_size
        binn.write(offset.to_bytes(4, "little"))
    binn.write((0x30950000).to_bytes(4, "big"))
    for i in range(210):
        binn.write(open("museumFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "rb").read())
    binn.close()