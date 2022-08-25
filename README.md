# FFC-Chunk-Editor
This is code to make editing the files from from the NDS Fossil Fighters games (just FFC right now until FF1's text is cracked) relating to vivosaur moves easier.

Here is an outline of the process:

1. Download this repo itself. Github is a little weird about that, you have to click the green "Code" button and then click "Download Zip."
2. Install Python (3+) from https://www.python.org/ (or, if you are on Windows, you can do what I recommend and get it from the Microsoft Store by opening up the Command
Prompt and typing the word "python" by itself, then hitting Enter).
3. Use Nitro Explorer, Crystal Tiles 2, etc. to split apart the ROM.
4. Choose whether you wish to edit attack data, vivosaur data, VMM move descriptions, battle move descriptions, move names, or vivosaur descriptions. Then grab, in that order:
etc/attack_defs, etc/creature_defs, text/text_attack_information, text/text_attack_info, text/text_attack_name, or text/text_dino_information.
5. Download The Python MARtool, which can be found at https://github.com/opiter09/MARtool. Unzip it, and place the file from step 2 in the same folder as MARtool.py.
6. Using the link in The Python MARtool's Readme, download the "CUE" series of decompression tools. Put all the exe's you end up with from that into the same folder as MARtool.py.
7. Drag the file from Step 4 onto MARtool.bat, or Command-Line "python MARtool.py filename" if you're not on Windows. This will generate a new folder, and an MCM and folder inside that.
8. Select from among the folders in this repository the one that corresponds to your file; the names should be self-explanatory. Move the contents of that folder to the folder within
the folder created in Step 7, i.e. into the folder with the "_Decompressed" files in it.
9. Run the batch file (or Command-Line the python file if not on Windows) which does NOT have "decomp" in its name. This will create a folder full of little chunks, which are
appropriately named for easy editing.
10. Edit those to youe heart's content, using my Documentation.txt as a guide. This requires use of a Hex Editor (I use HxD), and some program to convert Hex to Decimal and back (Windows'
Calculator app has a "programming" mode that can do this).
11. Now you can run the "decomp"-whatever batch/python. This will seem to do nothing, because it only changes existing files.
12. Go back out a few folders to where MARtool.py is. Now drag your Step 2 file onto MARtool-C.bat (or Command Line "python MARtool-C.py filename"). This will create a much larger file
named "output_filename."
13. Insert that new file back into the ROM.

For CrystalTiles 2, insert the file as follows:
1. Load your ROM into it, go to File -> NDS File System. For convenience, click View a list of -> Directory to show files inside folders instead of in one
gigantic list. Then scroll down to your file.
12. Left click the file to select it, then right click, press Import, and choose your edited file.
3. Now save the ROM. CrystalTile2 is weird, so you have to save by trying to quit and then clicking No to cancel. Then quit for real to be done.

Credit to jianminyong for generating the table of attack names (names.txt).
