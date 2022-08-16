# FFC_Chunk-Editor
This code to make editing the file attack_defs (and other files that feature pointers at the beginning) from the NDS Fossil Fighters games easier.
It is designed for the Fossil Fighters Champions version of the file; small adjustments would have to be made to get it to work with FF1 (the hardest part would be 
making a new name list). To use this, first split apart attack_defs with The Python MARtool (https://github.com/opiter09/MARtool), making sure you have the needed 
executables. Then drop the files from Attack Data here in the same folder as the _Decompressed files. If you run moves.bat, you will get a folder named "moveFiles," 
which features a list of little "chunks" of hex for each move. Running decompMoves.bat then combines the chunks into a big file, and splits that file back apart into the 
_Decompressed files. From here you can drag-and-drop attack_defs onto MARtool-C.bat and voila! You now have a new version of the file with your edit(s).

Similarly, to edit move descriptions, MARtool text_attack_information (NOT text_attack_info), then do basically the same as above but for the Move Descriptions folder 
here. Or for vivosaur files, use the code in Vivosaur Data and the file creature_defs.

The reason all this has to exist is that the location of key data (status effect, FP cost, etc.) is *very* inconsistent within each "chunk." So I cannot simply make a
GUI to do the work for you.

Credits go to jianminyong for generating this table of attack names.
