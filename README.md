# FF1-FFC-Chunk-Manager
This is code to make editing the files from the NDS Fossil Fighters games which have a series of pointers at the beginning easier.

Here is an outline of the process:

1. Download this repo itself. Github is a little weird about that, you have to click the green "Code" button and then click "Download Zip."

2. Install Python (3+) from https://www.python.org/downloads. If you are on Windows, you should get it from the Microsoft Store instead, to prevent problems where it can't find Python.

3. Use Nitro Explorer, Crystal Tile 2 (https://www.romhacking.net/utilities/818/), etc. to split apart the ROM.

4. Choose from among the following files what you wish to edit:
	- FF1:
		- episode/eXXXX: files for the various scripted events that occur in the game
		- text/japanese: basically all of the text in the game
		- etc/kaseki_defs: data for the individual fossils
		- etc/creature_defs: data for each vivosaur
		- etc/attack_defs: data for each move
	- FFC:
		- episode/eXXXX: files for the various scripted events that occur in the game
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

7. Select from among the folders in this repository the one with the same name as your file. Move the contents of that folder to the folder within the folder created in Step 6, i.e.
into the folder containing "0.bin."

8. Run the batch file (or Command-Line the python file if not on Windows) with "split" in its name. This will create a folder full of little chunks, which are
appropriately named for easy editing.

9. Edit those to your heart's content, using my the documentation found at https://github.com/opiter09/Fossil-Fighters-Documentation as a guide. This requires use of a Hex
Editor (I use HxD, which can be found at https://mh-nexus.de/en/hxd/), and some program to convert Hex to Decimal and back (Windows' Calculator app has a "programming" mode
that can do this).

10. Now you can run the "merge"-whatever batch/python. This will seem to do nothing, because it only changes existing files.

11. Go back out a few folders to where fftool.exe is. Now drag your Step 2 file onto compress.bat. This will create a new file, which may be a different size, named "output_filename."

12. Insert that new file back into the ROM.

For CrystalTiles 2, split apart the ROM as follows:
1. Load your ROM into it (via File -> Open), then go to Tools -> NDS File System.
2. In that sub-window, go to File -> Split ROM.
3. Choose a folder to put the ROM files' folder into. It will be named the internal name of the game (KASEKI or KASEKI2 in this case).

Also for CrystalTiles 2, insert the file as follows:
1. Load your ROM into it, then go to Tools -> NDS File System.
2. For convenience, click View a list of -> Directory to show files inside folders instead of in one gigantic list.
3. Scroll to your file, left click to select it, and then right click, press Import, and choose your edited file. If a popup appears talking
about how the file is too small, just press "Ok," and don't worry about it.
4. Once that is done, quit out of the sub-menu.
5. Now save the ROM. CrystalTile2 is weird, so if the Save option in the File menu is greyed-out, you will have to save by trying to quit
and clicking No to cancel, then quitting for real (which entails clicking Yes twice).

Credits to jianminyong for generating the very first name table used here, FFC attack names. And also, of course, for working out the compression of this
game, without which none of this would be possible.

PS: When it comes to text, you're honestly better just using Carbonizer (https://github.com/simonomi/carbonizer) for that these days. The text splitters will remain up here,
however, both for historical purposes, and in case you need them to figure out which messages refer to what.
