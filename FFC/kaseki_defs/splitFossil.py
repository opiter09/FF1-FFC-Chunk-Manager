import os
try:
    os.mkdir("kasekiFiles")
except OSError as error:
    pass

file = open("0.bin", "rb")
whole = file.read()
file.close()

text = open("vivoNames.txt", "rt").read()
parts = [ "Other", "Head", "Body", "Arms", "Legs", "Single" ]

text2 = list(open("jewelNames.txt", "rt").read().split("\n"))
text2D = {}
for i in range(len(text2)):
    text2D[int(text2[i].split(": ")[0])] = text2[i].split(": ")[1]

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
    elif (count in text2D.keys()):
        fileName = "./kasekiFiles/" + str(count).zfill(4) + "_" + text2D[count] + ".bin"
    
    if (count != 904) and (count not in text2D.keys()):
        fileName = fileName + "_" + parts[whole[beg + 8]] + ".bin"

    new = open(fileName, "wb")
    new.write(whole[beg:end])
    new.close()

    