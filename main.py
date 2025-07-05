from tkinter import Tk, Label, Entry, Button
from typing import List, Tuple, Set, Dict
from functions import fully_process


data: Dict[str, List[Tuple[str, str]]]
def test_click(*args) -> None:
    global root, data
    OWN_FILE: str = args[0]
    OTHER_FILE: str = args[1]
    
    data = fully_process(OWN_FILE, OTHER_FILE)
    
    own_only: List[Tuple[str, str]] = data["first only"]
    other_only: List[Tuple[str, str]] = data["second only"]
    
    own_labels: List[Label] = [Label(root, text=f"{mod[0]}") for mod in own_only]
    other_labels: List[Label] = [Label(root, text=f"{mod[0]}") for mod in other_only]
    
    own_label: Label = Label(root, text=f"{OWN_FILE}'s exclusive mods:")
    other_label: Label = Label(root, text=f"{OTHER_FILE}'s exclusive mods:")
    
    own_label.grid(column=0, row=2)
    other_label.grid(column=0, row=3)
    
    for idx, label in enumerate(own_labels):
        label.grid(column=idx+1, row=2)
        
    for idx, label in enumerate(other_labels):
        label.grid(column=idx+1, row=3)
        
    
    return None
    
root = Tk()
root.title("mod comparer")
root.geometry("1000x500")

first_file_button   : Button = Button(root, text="find first file:", width=20)
second_file_button  : Button = Button(root, text="find secondt file:", width=20)

first_file_label    : Label = Label(root)
second_file_label   : Label = Label(root)

some_test: Label = Label(root, text="test!")
some_test.config(text="new text!")

first_file_button.grid(column=0, row=0)
second_file_button.grid(column=0, row=1)

first_file_label.grid(column=1, row=0)
second_file_label.grid(column=1, row=1)

root.mainloop()

# to create installer, run: pyinstaller main.py --onefile --name test --windowed
