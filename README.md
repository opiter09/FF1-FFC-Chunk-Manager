# FF1-FFC-Chunk-Manager
This is code to make editing the files from the NDS Fossil Fighters games which have a series of pointers at the beginning easier.

Here is an outline of the process:

1. Download this repo itself. Github is a little weird about that, you have to click the green "Code" button and then click "Download Zip."

2. Install Python (3+) from https://www.python.org/ (or, if you are on Windows, you can do what I recommend and get it from the Microsoft Store by opening up the Command
Prompt and typing the word "python" by itself, then hitting Enter).

3. Use Nitro Explorer, Crystal Tile 2 (https://www.romhacking.net/utilities/818/), etc. to split apart the ROM.

4. Choose from among the following files what you wish to edit:
	- FF1:
		- text/japanese: basically all of the text in the game
		- etc/kaseki_defs: data for the individual fossils
		- etc/creature_defs: data for each vivosaur
		- etc/attack_defs: data for each move
	- FFC:
		- text/text_attack_information: move descriptions in the VMM/formation screens
		- text/text_attack_info: in-battle move descriptions
		- text/text_attack_name: names of moves
		- text/text_dino_information: vivosaur VMM/Formation descriptions
		- text/text_dino_kind: vivosaur size and range info
		- text/text_dino_short_name: normal vivosaur names
		- text/text_dino_name: vivosaur species names (for the Fossilary)
		- text/text_battle_enemy_name: names of enemy fighters in battle
		- etc/kaseki_defs: data for the individual fossils
		- etc/creature_defs: data for each vivosaur
		- etc/attack_defs: data for each move

5. Download Fossil Fighters Tool, which can be found at https://github.com/jianmingyong/Fossil-Fighters-Tool/releases. Unzip it, and place the file from step 4 in the same folder
as fftool.exe. Also place the file from this repo named "compress.bat" into that same folder.

6. Drag the file from Step 4 onto fftool.exe. This will create a folder named "bin" if one was not there already, and inside that a folder with the same name as your file.

7. Select from among the folders in this repository the one that corresponds to your file; the names should be self-explanatory. Move the contents of that folder to the folder within
the folder created in Step 6, i.e. into the folder containing "0.bin."

8. Run the batch file (or Command-Line the python file if not on Windows) with "split" in its name. This will create a folder full of little chunks, which are
appropriately named for easy editing.

9. Edit those to your heart's content, using my the documentation found at https://github.com/opiter09/Fossil-Fighters-Documentation as a guide. This requires use of a Hex
Editor (I use HxD, which can be found at https://mh-nexus.de/en/hxd/), and some program to convert Hex to Decimal and back (Windows' Calculator app has a "programming" mode
that can do this).

10. Now you can run the "merge"-whatever batch/python. This will seem to do nothing, because it only changes existing files.

11. Go back out a few folders to where fftool.exe is. Now drag your Step 2 file onto compress.bat. This will create a new file, which may be a different size, named "output_filename."

12. Insert that new file back into the ROM.

For CrystalTiles 2, split apart the ROM as follows:
1. Load your ROM into it, then go to File -> NDS File System.
2. In that sub-window, go to File -> Split ROM.
3. Choose a folder to put the ROM files' folder into. It will be named the internal name of the game (KASEKI or KASEKI2 in this case).

Also for CrystalTiles 2, insert the file as follows:
1. Load your ROM into it, then go to File -> NDS File System.
2. For convenience, click View a list of -> Directory to show files inside folders instead of in one gigantic list.
3. Scroll to your file, left click to select it, and then right click, press Import, and choose your edited file.
4. Now save the ROM. CrystalTile2 is weird, so if the Save option in the File menu is greyed-out, you will have to save by trying to quit
and clicking No to cancel, then quitting for real.

Credits to jianminyong for generating the very first name table used here, FFC attack names. And also, of course, for working out the compression of this
game, without which none of this would be possible.
