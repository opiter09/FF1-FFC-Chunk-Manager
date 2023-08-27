import os
    
f = open("0.bin", "rb")
r = f.read()
f.close()

big = int.from_bytes(r[4:8], "little")
newF = open("0.bin", "wb")
newF.close()
newF = open("0.bin", "ab")
newF.write(r[0:12])

for i in range(big):
    f2 = open("eventFiles/" + str(i).zfill(3) + ".bin", "rb")
    r2 = f2.read()
    f2.close()
    f2 = open("eventFiles/" + str(i).zfill(3) + ".bin", "wb")
    f2.close()
    f2 = open("eventFiles/" + str(i).zfill(3) + ".bin", "ab")
    for root, dirs, files in os.walk("eventFiles/" + str(i).zfill(3) + "_Files/"):
        small = len(files)
    f2.write(small.to_bytes(4, "little"))
    f2.write(r2[4:8])
    loc = (small + 2) * 4
    for j in range(small):
        f2.write(loc.to_bytes(4, "little"))
        loc = loc + os.stat("eventFiles/" + str(i).zfill(3) + "_Files/" + str(j).zfill(3) + ".bin").st_size
    for j in range(small):
        f3 = open("eventFiles/" + str(i).zfill(3) + "_Files/" + str(j).zfill(3) + ".bin", "rb")
        r3 = f3.read()
        f3.close()
        f2.write(r3)
    f2.close()

loc2 = int.from_bytes(r[12:16], "little")
for i in range(big):
    newF.write(loc2.to_bytes(4, "little"))
    loc2 = loc2 + os.stat("eventFiles/" + str(i).zfill(3) + ".bin").st_size

for i in range(big):
    f4 = open("eventFiles/" + str(i).zfill(3) + ".bin", "rb")
    r4 = f4.read()
    f4.close()
    newF.write(r4)
newF.close()
        
    
    