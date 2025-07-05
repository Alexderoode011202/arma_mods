# Arma Mods Comparison Tool

## Description:
This repository is all about the Arma Mods Comparison Tool. This tool is a script written in python that offers the user a GUI where the user can select two arma/html mod files, which the tool then compares and shows the set-wise differences between them. To be more specific, it shows from the first mod file which mods are unique to only itself, and also does the same for the other one. This way, I as the creator, hope to provide a tool that solves the problem of knowing whether two sets of mods are truly the same or not, and if not, what is missing.

## Installation steps:
Technically one does not have to build the application from scratch due to the repository already including executables for both windows and linux found in the `dist` folder. If one wishes to rebuild the executable from scratch for some reason, then follow these steps:

1. clone the repo: `git clone https://github.com/Alexderoode011202/arma_mods.git` or just download the repo as a zip file & extract it.
2. move into the repo: `cd arma_mods`
3. (optional) If you don't have pyinstaller yet, download it with pip: `pip install pyinstaller`
4. now make the executable: `pyinstaller main.py --onefile --name test --windowed`
5. (optional) make a .desktop file or the windows derivative of it to easily find it.