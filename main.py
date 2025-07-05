from tkinter import Tk, Label, Button
from functions import extract_path, process_with_table
import tkinter as tk

"""
        -------------------------------------------------------------------------------------------
        <--------------------------------- ASSET CREATION SECTION -------------------------------->
        -------------------------------------------------------------------------------------------
"""
# 1. create boilerplate nonsense
# ------------------------------
first_path: str 
second_path: str
    
root = Tk()
root.title("mod comparer")
root.geometry("1200x800")
# //////////////////////////////

# 2. create buttons for extracting the files
# ------------------------------
first_file_button   : Button = Button(root, text="find first file:"  , width=20, command=lambda : extract_path(path=0))
second_file_button  : Button = Button(root, text="find secondt file:", width=20, command=lambda : extract_path(path=1))
process_button      : Button = Button(root, text="process.."         , width=20, command=lambda : process_with_table(first_path, second_path))
# //////////////////////////////

# 3. create labels for representing the selected file (for clarity)
# ------------------------------
first_file_label    : Label = Label(root)
second_file_label   : Label = Label(root)
# //////////////////////////////



"""
        -------------------------------------------------------------------------------------------
        <------------------------------ ASSET VISUALISATION SECTION ------------------------------>
        -------------------------------------------------------------------------------------------
"""

# 1. show the file extraction buttons                                       visual, grid-like layout:
# ------------------------------                                            _____
first_file_button.grid(column=0, row=0)                 # 1                 |1|3|
second_file_button.grid(column=0, row=1)                # 2                 |2|4|
# //////////////////////////////                                            |5
                                                        #                   -----
# 2. show the file extraction labels                                        |table
# ------------------------------
first_file_label.grid(column=1, row=0)                  # 3
second_file_label.grid(column=1, row=1)                 # 4
# //////////////////////////////

# 3. show the procesing button
# ------------------------------
process_button.grid(column=0, row=2)                    # 5
# //////////////////////////////
root.mainloop()

# to create installer, run: pyinstaller main.py --onefile --name test --windowed
