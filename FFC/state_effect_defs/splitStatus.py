import os

try:
    os.mkdir("statusFiles")
except:
    pass

names = [
    "Nothing",
	"Normal Poison",
	"Gold Poison",
	"Venom (U-Raptor)",
	"Normal Sleep",
	"Gold Sleep",
	"Normal Scare",
	"Gold Scare",
	"Normal Enrage",
	"Gold Enrage",
	"Normal Confusion",
	"Gold Confusion",
	"Normal Excite",
	"Gold Excite",
	"Counter",
	"Super Counter",
	"Enflame",
	"Super Enflame",
	"Harden",
	"Super Harden",
	"Quicken",
	"Super Quicken",
	"Charge",
	"Super Charge (Unused)"
]

f = open("0.bin", "rb")
r = f.read()
f.close()

big = int.from_bytes(r[8:12], "little")
for i in range(big):
    old = 16 + (i * 12)
    new = old + 12
    f = open("statusFiles/" + str(i).zfill(2) + "_" + names[i] + ".bin", "wb")
    f.write(r[old:new])
    f.close()
    