cd ./
fftool.exe compress "./bin/%~n1" -c "Huffman" -c "LZSS" -i "0.bin" -o "output_%~n1"
