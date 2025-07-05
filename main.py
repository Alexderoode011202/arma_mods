from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Treeview
from tkinter.filedialog import askopenfilename
from typing import List, Tuple, Set, Dict
from functions import fully_process
import os

first_path: str 
second_path: str

def process_with_table(OWN_FILE: str, OTHER_FILE: str, column_to_start: int = 0, row_to_start: int = 3) -> None:
    global root, data
    
    data = fully_process(OWN_FILE, OTHER_FILE)
    
    own_only: List[Tuple[str, str]] = data["first only"]
    other_only: List[Tuple[str, str]] = data["second only"]
    
    columns: Tuple[str] = ("first only", "second only")
    tree = Treeview(root, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
        
    
    
    

def process(OWN_FILE: str, OTHER_FILE: str, column_to_start: int = 0, row_to_start: int = 3) -> None:
    global root, data
    
    data = fully_process(OWN_FILE, OTHER_FILE)
    
    own_only: List[Tuple[str, str]] = data["first only"]
    other_only: List[Tuple[str, str]] = data["second only"]
    
    own_labels: List[Label] = [Label(root, text=f"{mod[0]}") for mod in own_only]
    other_labels: List[Label] = [Label(root, text=f"{mod[0]}") for mod in other_only]
    
    own_label: Label = Label(root, text=f"{OWN_FILE}'s exclusive mods:")
    other_label: Label = Label(root, text=f"{OTHER_FILE}'s exclusive mods:")
    
    own_label.grid(column=column_to_start, row=row_to_start)
    other_label.grid(column=column_to_start, row=row_to_start+1)
    
    for idx, label in enumerate(own_labels):
        label.grid(column=idx+1, row=row_to_start)
        
    for idx, label in enumerate(other_labels):
        label.grid(column=idx+1, row=row_to_start+1)

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
process_button      : Button = Button(root, text="process.."         , width=20, command=lambda : process(first_path, second_path))

first_file_label    : Label = Label(root)
second_file_label   : Label = Label(root)

first_file_button.grid(column=0, row=0)
second_file_button.grid(column=0, row=1)

first_file_label.grid(column=1, row=0)
second_file_label.grid(column=1, row=1)

process_button.grid(column=0, row=2)

root.mainloop()

# to create installer, run: pyinstaller main.py --onefile --name test --windowed
