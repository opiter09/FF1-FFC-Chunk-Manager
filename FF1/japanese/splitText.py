import os
try:
    os.mkdir("textFiles")
except OSError as error:
    pass

moveNames = open("moveNames.txt", "rb").read().decode("UTF-8", errors = "ignore")
vivoNames = open("vivoNamesN.txt", "rt").read()
enemyNames = open("enemyNames.txt", "rb").read().decode("UTF-8", errors = "ignore")

file = open("0.bin", "rb")
reading = file.read()

count = 0
for i in range(12, 15252, 4):
    oldOffset = int.from_bytes(reading[i:(i + 4)], "little")
    newOffset = int.from_bytes(reading[(i + 4):(i + 8)], "little")
    if (i == 15248):
        newOffset = os.stat("0.bin").st_size
        
    count = count + 1
    if (count < 24):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "wb")
    elif (count >= 24) and (count < 81):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_HelpText" + ".bin", "wb")
    elif (count >= 81) and (count < 85):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_SaveMessage" + ".bin", "wb")
    elif (count >= 85) and (count < 153):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MenuText" + ".bin", "wb")
    elif (count >= 153) and (count < 165):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_DigsiteDescr" + ".bin", "wb")
    elif (count >= 165) and (count < 176):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_BattleMenu" + ".bin", "wb")
    elif (count >= 176) and (count < 189):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "wb")
    elif (count >= 189) and (count < 205):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MenuText" + ".bin", "wb")
    elif (count >= 205) and (count < 275):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_Multiplayer" + ".bin", "wb")
    elif (count >= 275) and (count < 296):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_BattlePrep" + ".bin", "wb")
    elif (count >= 296) and (count < 322):
        new = open("textFiles/" + str(count - 1).zfill(4) + "CaseText" + ".bin", "wb")
    elif (count >= 322) and (count < 376):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_VMMText" + ".bin", "wb")
    elif (count >= 376) and (count < 433):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_RockText" + ".bin", "wb")
    elif (count >= 433) and (count < 442):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MuseumText" + ".bin", "wb")
    elif (count >= 442) and (count < 452):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MoreCannonText" + ".bin", "wb")
    elif (count >= 452) and (count < 505):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MenuHelpText" + ".bin", "wb")
    elif (count >= 505) and (count < 885):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_BattleHelpText" + ".bin", "wb")
    elif (count >= 885) and (count < 947):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "wb")
    elif (count >= 947) and (count < 1042):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_BattleMessages" + ".bin", "wb")
    elif (count >= 1042) and (count < 1159):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_VivoLongNames_" + vivoNames.split("\n")[count - 1042] + ".bin", "wb")
    elif (count >= 1159) and (count < 1276):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_VivoShortNames_" + vivoNames.split("\n")[count - 1159] + ".bin", "wb")
    elif (count >= 1276) and (count < 1393):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_VivoClass_" + vivoNames.split("\n")[count - 1276] + ".bin", "wb")
    elif (count >= 1393) and (count < 1509):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_VivoDescriptions_" + vivoNames.split("\n")[count - 1393] + ".bin", "wb")
    elif (count >= 1509) and (count < 1625):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_VivoMuseumText_" + vivoNames.split("\n")[count - 1509] + ".bin", "wb")
    elif (count == 1625) or (count == 1626):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "wb")
    elif (count >= 1627) and (count < 2035):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MoveNames_" + moveNames.split("\n")[count - 1627] + ".bin", "wb")
    elif (count == 2035) or (count == 2036) or (count == 2037):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_SupportTarget_" + ".bin", "wb")
    elif (count >= 2038) and (count < 2446):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MoveBattleDescr_" + moveNames.split("\n")[count - 2038] + ".bin", "wb")
    elif (count == 2446):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "wb")
    elif (count >= 2447) and (count < 2855):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MoveVMMDescr_" + moveNames.split("\n")[count - 2447] + ".bin", "wb")
    elif (count >= 2855) and (count < 2985):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_KeyItems" + ".bin", "wb")
    elif (count >= 2985) and (count < 3325):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_JournalEntries" + ".bin", "wb")
    elif (count >= 3325) and (count < 3363):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MaskNames" + ".bin", "wb")
    elif (count >= 3363) and (count < 3624):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_EnemyFighterNames_" + enemyNames.split("\n")[count - 3363] + ".bin", "wb")
    elif (count >= 3624) and (count < 3676):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "wb")
    elif (count >= 3676) and (count < 3686):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_JewelNames" + ".bin", "wb")
    elif (count >= 3686) and (count < 3807):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_MapNames" + ".bin", "wb")
    elif (count >= 3807):
        new = open("textFiles/" + str(count - 1).zfill(4) + "_ListHelpText" + ".bin", "wb")
    new.write(reading[oldOffset:newOffset])
    new.close()
