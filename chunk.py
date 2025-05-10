import FreeSimpleGUI as psg
import os
import shutil

if (os.path.exists("0 - Backup.bin") == False):
    shutil.copyfile("0.bin", "0 - Backup.bin")
f = open("0 - Backup.bin", "rb")
whole = f.read()
f.close()
pointer = "None"
for i in range(8, len(whole) - 4, 4):
    num = int.from_bytes(whole[i:(i + 4)], "little")
    if (num == (i + 4)):
        startLoc = num
        fileCount = int.from_bytes(whole[(i - 4):i], "little")
        pointer = "True"
        startP = int.from_bytes(whole[startLoc:(startLoc + 4)], "little")
        fixed = 0
        if (startP != (startLoc + (fileCount * 4))):
            pointer = "False"
            startP = 0
            fixed = (len(whole) - startLoc) // fileCount
        break
fileSizes = []
for i in range(4, startLoc - 8, 4):
    if (int.from_bytes(whole[i:(i + 4)]) == len(whole)):
        fileSizes.append(i)
    

if (pointer == "None"):
    psg.popup("This is not a chunked file!", title = "")
else:
    if (os.path.exists("./chunkFiles/") == False):
        names = []
        textF = psg.popup_get_file("Names File:", title = "", file_types = [("Text Files", "*.txt")], font = "-size 12")
        if ((textF != None) and (textF != "")):
            f = open(textF, "rb")
            r = f.read()
            f.close()
            rtext = r.decode("UTF-8", errors = "ignore")
            names = list(rtext.replace("\r", "").split("\n"))
        os.mkdir("./chunkFiles/")
        for i in range(fileCount):
            if (pointer == "True"):
                oldOffset = int.from_bytes(whole[(startLoc + (i * 4)):(startLoc + 4 + (i * 4))], "little")
                newOffset = int.from_bytes(whole[(startLoc + 4 + (i * 4)):(startLoc + 8 + (i * 4))], "little")
            else:
                oldOffset = startLoc + (i * fixed)
                newOffset = startLoc + fixed + (i * fixed)
            if (i == (fileCount - 1)):
                newOffset = len(whole)
            if (len(names) > i):
                text = names[i]
            else:
                text = "Extra"
            newFile = open("chunkFiles/" + str(i).zfill(4) + "_" + text + ".bin", "wb")
            newFile.write(whole[oldOffset:newOffset])
            newFile.close()
    else:
        f = open("0.bin", "wb")
        f.close()
        f = open("0.bin", "ab")
        f.write(whole[0:(startLoc - 8)])
        theFiles = list(os.listdir("./chunkFiles/"))
        theFiles.sort() # just to be safe
        f.write(len(theFiles).to_bytes(4, "little"))
        f.write(startLoc.to_bytes(4, "little"))
        if (pointer == "True"):
            place = startLoc + (len(theFiles) * 4)
            f.write(place.to_bytes(4, "little"))
            for i in range(len(theFiles) - 1):
                place = place + os.stat("./chunkFiles/" + theFiles[i]).st_size
                f.write(place.to_bytes(4, "little"))
        for i in range(len(theFiles)):
            tf = open("./chunkFiles/" + theFiles[i], "rb")
            tfr = tf.read()
            if (pointer == "False"):
                if (len(tfr) < fixed):
                    tfr = tfr + bytes(fixed - len(tfr))
                elif (len(tfr) > fixed):
                    tfr = tfr[0:fixed]
            f.write(tfr)
        f.close()
    if (len(fileSizes) > 0):
        cf = open("0.bin", "rb")
        cfr = cf.read()
        cf.close()
        cf = open("0.bin", "wb")
        cf.close()
        cf = open("0.bin", "ab")
        cf.write(cfr[0:fileSizes[0]])
        cf.write(len(cfr).to_bytes(4, "little"))
        if (len(fileSizes) == 1):
            cf.write(cfr[(filesSizes[0] + 4):])
            cf.close()
        else:
            for i in range(1, len(fileSizes)):
                cf.write(cfr[(fileSizes[i - 1] + 4):fileSizes[i]])
                cf.write(len(cfr).to_bytes(4, "little"))
                if (i == (len(fileSizes) - 1)):
                    cf.write(cfr[(fileSizes[i] + 4):])
            cf.close()
            
        

