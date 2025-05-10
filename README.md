# FF1-FFC-Chunk-Manager
This is code to make editing the files from the NDS Fossil Fighters games which have a series of pointers at the beginning, or
are a series of fixed-length sections, easier.

NOTE: This tool is is only designed for Windows (unless you want to try running the Python yourself, that is). For Mac and Linux,
I can only point you to WINE (https://www.winehq.org/).

Here is an outline of the process:

01. Download this repo itself. Github is a little weird about that, you have to click the green "Code" button and then click
   "Download Zip".

02. Install Python (3+) from https://www.python.org/downloads. If you are on Windows, you should get it from the Microsoft Store
   instead, to prevent problems where it can't find Python.

03. Use Nitro Explorer, CrystalTile2 (https://www.romhacking.net/utilities/818/), etc. to split apart the ROM. See the end
    for instructions for CrystalTile2 specifically.

04. Choose one of the "chunked" files to edit. The tool has been refactored to work on basically all of them, but here is the
   former list of candidates so you know what they contain:
	- FF1:
		- episode/eXXXX: files for the various scripted events that occur in the game
		- etc/creature_defs: data for each vivosaur
		- etc/kaseki_defs: data for the individual fossils
		- text/japanese: basically all of the non-dialogue text in the game (Note: This file has the special property that the
		  lengths of its chunks must all be multiples of 4, so please add/remove 00's at the end as needed. If the text would
		  be a multiple of 4 by itself, include 4 00's at the end instead of none)
		
	- FFC:
		- episode/eXXXX: files for the various scripted events that occur in the game
		- etc/attack_defs: data for each move
		- etc/creature_defs: data for each vivosaur
		- etc/kaseki_defs: data for the individual fossils
		- etc/state_effect_defs: data for the status effects
		- text/text_attack_info: in-battle move descriptions
		- text/text_attack_information: move descriptions in the VMM/formation screens
		- text/text_attack_name: names of moves
		- text/text_battle_enemy_name: names of enemy fighters in battle
		- text/text_dino_information: vivosaur VMM/Formation descriptions
		- text/text_dino_kind: vivosaur size and range info
		- text/text_dino_name: vivosaur species names (for the Fossilary)
		- text/text_dino_short_name: normal vivosaur names
		- text/text_museum: vivosaur Fossilary entries

05. Download Fossil Fighters Tool, which can be found at https://github.com/jianmingyong/Fossil-Fighters-Tool/releases. Unzip it,
   and place the file from step 4 in the same folder as "fftool.exe". Also place the file from this repo named "compress.bat"
   into that same folder.

06. Drag the file from Step 4 onto fftool.exe. This will create a folder named "bin" if one was not there already, and inside that
   a folder with the same name as your file.

07. Move/copy "chunk.exe" here inside the folder inside "bin", i.e. where the file "0.bin" is. Run "chunk.exe" by simply clicking
   it. At that point, a dialogue will pop up asking you to select a text file with names in them; choose the appropriate one
   from inside the folder "Text Files" here (the names should be obvious, and ignore the "_Zero" prefixes).

08. This will thus generate a folder named "chunkFiles" where the "0.bin" is, with a number of files that are each a separate
   "chunk" of the main one. You can then edit those to your heart's content, using my the documentation found at
   https://github.com/opiter09/Fossil-Fighters-Documentation as a guide. This requires use of a Hex Editor (I use HxD, which can
   be found at https://mh-nexus.de/en/hxd/), and some program to convert Hex to Decimal and back (Windows' Calculator app has a
   "programming" mode that can do this).

09. If you want to add a new chunk, you can simply create a new file in the folder, with the three digits of placement (generally
    right after the other ones), then an underscore, then literally anything, and then the ".bin" extension. Similarly, you can
	just remove files to delete them (you don't even have to rename anything since the code only cares about name order).

09. Now you can run "chunk.exe" again. This will seem to do nothing, because it only changes existing files.

10. Go back out a few folders to where "fftool.exe" is. Now drag your Step 2 file onto "compress.bat". This will create a new
    file, which may be a different size, named "output_FILENAME".

11. Insert that new file back into the ROM.

For CrystalTile2, split apart the ROM as follows:
1. Load your ROM into it (via File -> Open), then go to Tools -> NDS File System.
2. In that sub-window, go to File -> Split ROM.
3. Choose a folder to put the ROM files' folder into. It will be named the internal name of the game (KASEKI or KASEKI2 in this
   case).

Also for CrystalTile2, insert the file as follows:
1. Load your ROM into it, then go to Tools -> NDS File System.
2. For convenience, click View a list of -> Directory to show files inside folders instead of in one gigantic list.
3. Scroll to your file, left click to select it, and then right click, press Import, and choose your edited file. If a popup
   appears talking about how the file is too small, just press "Ok" and don't worry about it.
4. Once that is done, quit out of the sub-menu.
5. Now save the ROM. CrystalTile2 is weird, so if the Save option in the File menu is greyed-out, you will have to save by
   trying to quit and clicking No to cancel, then quitting for real (which entails clicking Yes twice).

Credits to jianminyong for generating the very first name table used here, FFC attack names. And also, of course, for working out
the compression of this game, without which none of this would be possible.
