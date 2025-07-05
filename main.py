from tkinter import Tk, Label, Entry, Button
from tkinter.filedialog import askopenfilename
from typing import List, Tuple, Set, Dict
from functions import fully_process
import os

first_path: str 
second_path: str

def extract_path(path: int = 0) -> str:
    global first_path, second_path, first_file_label, second_file_label
    
    file_path: str = askopenfilename(initialdir=os.getcwd(), 
                                       title="get your mod file", 
                                       filetypes=(("HTML files", "*.html"), 
                                                  ("all files", "*.*")))
    if path == 0:
        first_path = file_path
        first_file_label.config(text=f"file: {file_path}")    
    elif path == 1:
        second_path = file_path
        second_file_label.config(text=f"file: {file_path}")    
    



root = Tk()
root.title("mod comparer")
root.geometry("1000x500")

first_file_button   : Button = Button(root, text="find first file:"  , width=20, command=lambda : extract_path(path=0))
second_file_button  : Button = Button(root, text="find secondt file:", width=20, command=lambda : extract_path(path=1))

first_file_label    : Label = Label(root)
second_file_label   : Label = Label(root)

first_file_button.grid(column=0, row=0)
second_file_button.grid(column=0, row=1)

first_file_label.grid(column=1, row=0)
second_file_label.grid(column=1, row=1)

root.mainloop()

# to create installer, run: pyinstaller main.py --onefile --name test --windowed
