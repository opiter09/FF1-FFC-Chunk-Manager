import os

text = open("enemyNames.txt", "rb").read()
listing = text.split((10).to_bytes(1, "little"))

old = open("0.bin", "rb")
header = old.read()[0:16]
old.close()

new = open("0.bin", "wb")
new.write(header)
new.close()
new = open("0.bin", "ab")

size = int.from_bytes(header[12:16], "little")
for i in range(len(listing) - 1):
    size = size + os.stat("enemyNameFiles/" + str(i + 1).zfill(2) + "_" + listing[i].decode("UTF-8", errors = "ignore") + ".bin").st_size
    new.write(size.to_bytes(4, "little"))

for i in range(len(listing)):
    new.write(open("enemyNameFiles/" + str(i + 1).zfill(2) + "_" + listing[i].decode("UTF-8", errors = "ignore") + ".bin", "rb").read())