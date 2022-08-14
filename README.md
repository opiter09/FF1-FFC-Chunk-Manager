# Attack-Defs-Tool
This a tool to make editing the file attack_defs from the NDS Fossil Fighters games easier. It is designed for the Fossil Fighters Champions version of the file;
small adjustments may have to be made to get it to work with FF1 (the hardest part would be making a new name list). To use this, first split apart attack_defs
with The Python MARtool (https://github.com/opiter09/MARtool), making sure you have the needed executables. Then drop the files from here in the same subfolder
as the _Decompressed files. If you run moves.bat, you will get a folder named "moveFiles," which features a list of little "chunks" of hex for each move. Running
decompMoves.bat then combines the chunks into a big file, and splits that file back apart into the _Decompressed files. From here you candrag-and-drop attack_defs
onto MARtool-C.bat and voila! You now have a new version of the file with your edit(s).

Credits go to jianminyong for generating this table of attack names.
