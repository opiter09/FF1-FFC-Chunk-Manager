import os

if (os.path.exists("./kasekiFiles/") == True):
    fileList = []
    for root, dirs, files in os.walk("./kasekiFiles"):
        fileList = files
    fileList.sort()

    old = open("0.bin", "rb")
    header = old.read()[0:16]
    old.close()

    new = open("0.bin", "wb")
    new.write(header)
    new.close()
    new = open("0.bin", "ab")

    size = int.from_bytes(header[12:16], "little")
    for i in range(len(fileList) - 1):
        size = size + os.stat("kasekiFiles/" + fileList[i]).st_size
        new.write(size.to_bytes(4, "little"))

    for i in range(len(fileList)):
        new.write(open("kasekiFiles/" + fileList[i], "rb").read())