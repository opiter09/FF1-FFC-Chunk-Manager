import os

if (os.path.exists("./statusFiles/") == True):
    f = open("0.bin", "rb")
    r = f.read()
    f.close()

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

    big = int.from_bytes(r[8:12], "little")
    newF = open("0.bin", "wb")
    newF.close()
    newF = open("0.bin", "ab")
    newF.write(r[0:16])

    for i in range(big):
        f = open("statusFiles/" + str(i).zfill(2) + "_" + names[i] + ".bin", "rb")
        r = f.read()
        f.close()
        newF.write(r)
    newF.close()
            
        
        