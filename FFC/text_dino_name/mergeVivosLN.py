import os

if (os.path.exists("./vivoLongNameFiles/") == True):
    binn = open("0.bin", "rb")
    whole = binn.read()
    binn.close()
    binn = open("0.bin", "rb")
    section = binn.read(20)
    binn.close()

    binn = open("0.bin", "wb")
    binn.write(section)
    binn.close()

    binn = open("0.bin", "ab")
    text = open("vivoNamesL.txt", "rt").read()
    offset = int.from_bytes(whole[16:20], "little")
    for i in range(203):
        offset = offset + os.stat("vivoLongNameFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin").st_size
        binn.write(offset.to_bytes(4, "little"))
    binn.write((0x4E6F6E6500).to_bytes(5, "big"))
    for i in range(204):
        binn.write(open("vivoLongNameFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "rb").read())
    binn.close()