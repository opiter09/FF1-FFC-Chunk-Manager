import os

fileList = []
for root, dirs, files in os.walk("./textFiles"):
    fileList = files
fileList.sort()

old = open("0.bin", "rb")
header = old.read()[0:16]
old.close()

new = open("0.bin", "wb")
new.write(header)
new.close()
new = open("0.bin", "ab")

moveNames = open("moveNames.txt", "rb").read().decode("UTF-8", errors = "ignore")
vivoNames = open("vivoNamesN.txt", "rt").read()

size = int.from_bytes(header[12:16], "little")
count = 0
for i in range(12, 15248, 4):
    count = count + 1
    if (count < 24):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 24) and (count < 81):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_HelpText" + ".bin", "rb")
    elif (count >= 81) and (count < 85):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_SaveMessage" + ".bin", "rb")
    elif (count >= 85) and (count < 153):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MenuText" + ".bin", "rb")
    elif (count >= 153) and (count < 165):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_DigsiteDescr" + ".bin", "rb")
    elif (count >= 165) and (count < 176):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattleMenu" + ".bin", "rb")
    elif (count >= 176) and (count < 189):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 189) and (count < 205):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MenuText" + ".bin", "rb")
    elif (count >= 205) and (count < 275):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Multiplayer" + ".bin", "rb")
    elif (count >= 275) and (count < 296):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattlePrep" + ".bin", "rb")
    elif (count >= 296) and (count < 322):
        small = open("textFiles/" + str(count - 1).zfill(4) + "CaseText" + ".bin", "rb")
    elif (count >= 322) and (count < 376):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VMMText" + ".bin", "rb")
    elif (count >= 376) and (count < 433):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_RockText" + ".bin", "rb")
    elif (count >= 433) and (count < 442):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MuseumText" + ".bin", "rb")
    elif (count >= 442) and (count < 452):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoreCannonText" + ".bin", "rb")
    elif (count >= 452) and (count < 505):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MenuHelpText" + ".bin", "rb")
    elif (count >= 505) and (count < 885):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattleHelpText" + ".bin", "rb")
    elif (count >= 885) and (count < 947):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 947) and (count < 1042):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattleMessages" + ".bin", "rb")
    elif (count >= 1042) and (count < 1159):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoLongNames_" + vivoNames.split("\n")[count - 1042] + ".bin", "rb")
    elif (count >= 1159) and (count < 1276):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoShortNames_" + vivoNames.split("\n")[count - 1159] + ".bin", "rb")
    elif (count >= 1276) and (count < 1393):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoClass_" + vivoNames.split("\n")[count - 1276] + ".bin", "rb")
    elif (count >= 1393) and (count < 1509):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoDescriptions_" + vivoNames.split("\n")[count - 1393] + ".bin", "rb")
    elif (count >= 1509) and (count < 1625):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoMuseumText_" + vivoNames.split("\n")[count - 1509] + ".bin", "rb")
    elif (count == 1625) or (count == 1626):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 1627) and (count < 2035):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoveNames_" + moveNames.split("\n")[count - 1627] + ".bin", "rb")
    elif (count == 2035) or (count == 2036) or (count == 2037):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_SupportTarget_" + ".bin", "rb")
    elif (count >= 2038) and (count < 2446):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoveBattleDescr_" + moveNames.split("\n")[count - 2038] + ".bin", "rb")
    elif (count == 2446):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 2447) and (count < 2855):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoveVMMDescr_" + moveNames.split("\n")[count - 2447] + ".bin", "rb")
    elif (count >= 2855) and (count < 2985):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_KeyItems" + ".bin", "rb")
    elif (count >= 2985) and (count < 3325):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_JournalEntries" + ".bin", "rb")
    elif (count >= 3325) and (count < 3363):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MaskNames" + ".bin", "rb")
    elif (count >= 3363) and (count < 3624):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_EnemyFighterNames" + ".bin", "rb")
    elif (count >= 3624) and (count < 3676):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 3676) and (count < 3686):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_JewelNames" + ".bin", "rb")
    elif (count >= 3686) and (count < 3807):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MapNames" + ".bin", "rb")
    elif (count >= 3807):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_ListHelpText" + ".bin", "rb")
    
    size = size + len(small.read())
    new.write(size.to_bytes(4, "little"))
    small.close()

count = 0
for i in range(12, 15252, 4):
    count = count + 1
    if (count < 24):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 24) and (count < 81):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_HelpText" + ".bin", "rb")
    elif (count >= 81) and (count < 85):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_SaveMessage" + ".bin", "rb")
    elif (count >= 85) and (count < 153):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MenuText" + ".bin", "rb")
    elif (count >= 153) and (count < 165):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_DigsiteDescr" + ".bin", "rb")
    elif (count >= 165) and (count < 176):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattleMenu" + ".bin", "rb")
    elif (count >= 176) and (count < 189):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 189) and (count < 205):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MenuText" + ".bin", "rb")
    elif (count >= 205) and (count < 275):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Multiplayer" + ".bin", "rb")
    elif (count >= 275) and (count < 296):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattlePrep" + ".bin", "rb")
    elif (count >= 296) and (count < 322):
        small = open("textFiles/" + str(count - 1).zfill(4) + "CaseText" + ".bin", "rb")
    elif (count >= 322) and (count < 376):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VMMText" + ".bin", "rb")
    elif (count >= 376) and (count < 433):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_RockText" + ".bin", "rb")
    elif (count >= 433) and (count < 442):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MuseumText" + ".bin", "rb")
    elif (count >= 442) and (count < 452):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoreCannonText" + ".bin", "rb")
    elif (count >= 452) and (count < 505):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MenuHelpText" + ".bin", "rb")
    elif (count >= 505) and (count < 885):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattleHelpText" + ".bin", "rb")
    elif (count >= 885) and (count < 947):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 947) and (count < 1042):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_BattleMessages" + ".bin", "rb")
    elif (count >= 1042) and (count < 1159):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoLongNames_" + vivoNames.split("\n")[count - 1042] + ".bin", "rb")
    elif (count >= 1159) and (count < 1276):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoShortNames_" + vivoNames.split("\n")[count - 1159] + ".bin", "rb")
    elif (count >= 1276) and (count < 1393):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoClass_" + vivoNames.split("\n")[count - 1276] + ".bin", "rb")
    elif (count >= 1393) and (count < 1509):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoDescriptions_" + vivoNames.split("\n")[count - 1393] + ".bin", "rb")
    elif (count >= 1509) and (count < 1625):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_VivoMuseumText_" + vivoNames.split("\n")[count - 1509] + ".bin", "rb")
    elif (count == 1625) or (count == 1626):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 1627) and (count < 2035):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoveNames_" + moveNames.split("\n")[count - 1627] + ".bin", "rb")
    elif (count == 2035) or (count == 2036) or (count == 2037):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_SupportTarget_" + ".bin", "rb")
    elif (count >= 2038) and (count < 2446):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoveBattleDescr_" + moveNames.split("\n")[count - 2038] + ".bin", "rb")
    elif (count == 2446):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 2447) and (count < 2855):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MoveVMMDescr_" + moveNames.split("\n")[count - 2447] + ".bin", "rb")
    elif (count >= 2855) and (count < 2985):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_KeyItems" + ".bin", "rb")
    elif (count >= 2985) and (count < 3325):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_JournalEntries" + ".bin", "rb")
    elif (count >= 3325) and (count < 3363):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MaskNames" + ".bin", "rb")
    elif (count >= 3363) and (count < 3624):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_EnemyFighterNames" + ".bin", "rb")
    elif (count >= 3624) and (count < 3676):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_Unused" + ".bin", "rb")
    elif (count >= 3676) and (count < 3686):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_JewelNames" + ".bin", "rb")
    elif (count >= 3686) and (count < 3807):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_MapNames" + ".bin", "rb")
    elif (count >= 3807):
        small = open("textFiles/" + str(count - 1).zfill(4) + "_ListHelpText" + ".bin", "rb")
    
    new.write(small.read())
    small.close()
new.close()