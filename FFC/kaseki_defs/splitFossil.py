import os
try:
    os.mkdir("kasekiFiles")
except OSError as error:
    pass

file = open("0.bin", "rb")
whole = file.read()
file.close()

text = open("vivoNames.txt", "rt").read()
parts = [ "Unused", "Head", "Body", "Arms", "Legs", "Single" ]
count = -1
for i in range(12, 0xFA5, 4):
    count = count + 1
    beg = int.from_bytes(whole[i:(i + 4)], "little")
    end = int.from_bytes(whole[(i + 4):(i + 8)], "little")
    if (i == 0xFA4):
        end = os.stat("0.bin").st_size

    fileName = "./kasekiFiles/" + str(count).zfill(4)
    if (count >= 1) and (count <= 570) and (whole[beg + 16] != 0):
        fileName = fileName + "_" + text.split("\n")[whole[beg + 16] - 1]
    elif (count == 900) or (count == 901) or (count == 902) or (count == 903):
        fileName = fileName + "_Silver"
    elif (count == 904):
        fileName = fileName + "_Gold_Head.bin"

    if (count >= 700) and (count <= 729):
        fileName = fileName + "_Other1.bin"
    elif (count >= 800) and (count <= 833):
        fileName = fileName + "_Other2.bin"
    elif (count != 904):
        fileName = fileName + "_" + parts[whole[beg + 8]] + ".bin"

    new = open(fileName, "wb")
    new.write(whole[beg:end])
    new.close()

    