# MS-Steganography-Tool
MS Steganography Tool created for encryption vs. hiding your data in Microsoft Office Documents. The structure of the documents will be not violated! WARNING! If you will be changed any data in encrypted document then hidden encrypted information will be vanished! Support the project please. Monero: 43kpHUzR5otCHnqYJxDNz3S4uPBaKq6YCBwY4BtnCCABEhRpbbYud8nf4PCYbL2HxqgbzGQesJ13m4nPMbtZeuJW4cquM3R

![st](https://user-images.githubusercontent.com/34070575/147986451-d2d9d6ea-e469-4932-9fea-f150cbabae31.jpg)

# Install for Windows Python3

cd MS-Steganography-Tool-main

python -m pip install -r requirements.txt

python MSST.py

# Build exe for Windows Pyinstaller

cd MS-Steganography-Tool-main

pyinstaller --onefile --windowed MSST.py

cd dist

start MSST.exe

# Install for Linux Python3

git clone https://github.com/LordAT1/MS-Steganography-Tool.git

cd MS-Steganography-Tool

python3 -m pip install -r requirements.txt

python3 MSST.py

# How to fix ModuleNotFoundError:Tkinter on Linux

python3 -m pip install tk-tools

or

sudo apt-get install python3-tk


# Build package for Linux Pyinstaller

cd MS-Steganography-Tool

pyinstaller --onefile --windowed MSST.py

cd dist

chmod 777 MSST

./MSST

# Example
![demonstr(1)](https://user-images.githubusercontent.com/34070575/146655520-550919ae-6998-43c8-8c32-d8c885c737b3.gif)
