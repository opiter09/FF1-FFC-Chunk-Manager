# FFC-Chunk-Editor
This is code to make editing the files from from the NDS Fossil Fighters games (just FFC right now until FF1's text is cracked) relating to vivosaur moves easier.

Here is an outline of the process:

0. Install Python (3+) from https://www.python.org/
1. Use Nitro Explorer, Crystal Tiles 2, etc. to split apart the ROM.
2. Choose whether you wish to edit attack data, vivosaur data, VMM move descriptions, or battle move descriptions. Then grab, in that order: etc/attack_defs, etc/creature_defs,
text/text_attack_information, or text/text_attack_info.
3. Download The Python MARtool, which can be found at https://github.com/opiter09/MARtool. Unzip it, and place the file from step 2 in the same folder as MARtool.py.
4. Using the link in The Python MARtool's Readme, download the "CUE" series of decompression tools. Put all the exe's you end up with from that into the same folder as MARtool.py.
5. Drag the file from Step 2 onto MARtool.bat, or Command-Line "python MARtool.py filename" if you're not on Windows. This will generate a new folder, and an MCM and folder inside that.
6. Select from among the folders in this repository the one that corresponds to your file: Attack Data for attack_defs, Battle Move Descriptions for text_attack_info,
Move Descriptions for text_attack_information, and Vivo Data for creature_defs. Move the contents of that folder to the folder within the folder created in Step 5, i.e. the
folder with the "_Decompressed" files in it.
7. Run the batch file (or Command-Line the python file if not on Windows) which does NOT have "decomp" in its name. This will create a folder full of little chunks, which are
appropriately named for easy editing.
8. Edit those to youe heart's content, using my Documentation.txt as a guide. This requires use of a Hex Editor (I use HxD), and some program to convert Hex to Decimal and back (Windows'
Calculator app has a "programming" mode that can do this).
9. Now you can run the "decomp"-whatever batch/python. This will seem to do nothing, because it only changes existing files.
10. Go back out a few folders to where MARtool.py is. Now drag your Step 2 file onto MARtool-C.bat (or Command Line "python MARtool-C.py filename"). This will create a much larger file
named "output_filename."
11. Insert that new file back into the ROM.

For CrystalTiles 2, insert the file as follows:
1. Load your ROM into it, go to File -> NDS File System. For convenience, click View a list of -> Directory to show files inside folders instead of in one
gigantic list. Then scroll down to your file.
12. Left click the file to select it, then right click, press Import, and choose your edited file.
3. Now save the ROM. CrystalTile2 is weird, so you have to save by trying to quit and then clicking No to cancel. Then quit for real to be done.

Credits go to jianminyong for generating the table of attack names (names.txt).
