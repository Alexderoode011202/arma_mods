from tkinter import Tk, Label, Button
from tkinter.ttk import Treeview
from tkinter.filedialog import askopenfilename
from typing import List, Tuple, Union
from functions import fully_process
import os
import tkinter as tk

first_path: str 
second_path: str

def transpose(*columns: List[List[str]]) -> List[List[Union[str, int]]]:
    largest_size: int = 1 
    
    for column in columns:
        if len(column) > largest_size:
            largest_size = len(column)
            
    for column in columns:
        if len(column) == largest_size:
            continue 
        
        column.extend([""]*(largest_size-len(column)))
    
    return [[row[i] for row in columns] for i in range(len(columns[0]))]
        
    
    
    

def process_with_table(OWN_FILE: str, OTHER_FILE: str, column_to_start: int = 0, row_to_start: int = 3) -> None:
    global root, data
    
    data = fully_process(OWN_FILE, OTHER_FILE)
    
    own_only_name   : List[str] = list(map(lambda x: x[0], data["first only"]))
    other_only_name : List[str] = list(map(lambda x: x[0], data["second only"]))
    
    rows: List[List[str]] = transpose(own_only_name, other_only_name)
    
    columns = ("own exclusive mods", "other exclusive mods")
    tree = Treeview(root, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=300)
    
    for row in rows:
        tree.insert("", tk.END, values=row)
        
    tree.grid(column=0, columnspan=len(rows[0]), row=row_to_start, rowspan=len(rows))
    
    
    
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
        
    return None
          

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
process_button      : Button = Button(root, text="process.."         , width=20, command=lambda : process_with_table(first_path, second_path))

first_file_label    : Label = Label(root)
second_file_label   : Label = Label(root)

first_file_button.grid(column=0, row=0)
second_file_button.grid(column=0, row=1)

first_file_label.grid(column=1, row=0)
second_file_label.grid(column=1, row=1)

process_button.grid(column=0, row=2)

root.mainloop()

# to create installer, run: pyinstaller main.py --onefile --name test --windowed
