import os

try:
    os.mkdir("eventFiles")
except:
    pass
    
f = open("0.bin", "rb")
r = f.read()
f.close()

big = int.from_bytes(r[4:8], "little")
for i in range(big):
    old = int.from_bytes(r[(12 + (i * 4)):(16 + (i * 4))], "little")
    new = int.from_bytes(r[(16 + (i * 4)):(20 + (i * 4))], "little")
    if (i == (big - 1)):
        new = os.stat("0.bin").st_size
    f = open("eventFiles/" + str(i).zfill(3) + ".bin", "wb")
    f.write(r[old:new])
    f.close()
    try:
        os.mkdir("eventFiles/" + str(i).zfill(3) + "_Files")
    except:
        pass
    countP = int.from_bytes(r[old:(old + 4)], "little")
    for j in range(countP):
        old2 = int.from_bytes(r[(old + 8 + (j * 4)):(old + 12 + (j * 4))], "little")
        new2 = int.from_bytes(r[(old + 12 + (j * 4)):(old + 16 + (j * 4))], "little")
        if (j == (countP - 1)):
            new2 = new - old
        f = open("eventFiles/" + str(i).zfill(3) + "_Files/" + str(j).zfill(3) + ".bin", "wb")
        f.write(r[(old + old2):(old + new2)])
        f.close()
    