import os
import math
try:
    os.mkdir("kasekiFiles")
except OSError as error:
    pass

file = open("0.bin", "rb")
whole = file.read()
file.close()

text = open("vivoNames.txt", "rt").read()
parts = [ "Head", "Body", "Arms", "Legs", "Other" ]
count = -1
for i in range(12, 0xFA5, 4):
    count = count + 1
    beg = int.from_bytes(whole[i:(i + 4)], "little")
    end = int.from_bytes(whole[(i + 4):(i + 8)], "little")
    if (i == 0xFA4):
        end = os.stat("0.bin").st_size

    if (count >= 1) and (count <= 464):
        fileName = "./kasekiFiles/" + str(count).zfill(4) + "_" + text.split("\n")[math.floor((count - 1) / 4)] + "_" + parts[(count - 1) % 4] + ".bin"
    else:
        fileName = "./kasekiFiles/" + str(count).zfill(4) + ".bin"

    new = open(fileName, "wb")
    new.write(whole[beg:end])
    new.close()

    