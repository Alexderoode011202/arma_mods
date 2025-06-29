from tkinter import *
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

own_msg = Label(root, text="own file: ")
other_msg = Label(root, text="other file: ")

own_entry = Entry(root, width=50)
own_entry.insert(0, "own.html")

other_entry = Entry(root, width=50)
other_entry.insert(0, "other.html")

process_button = Button(root, text="process", command=lambda :test_click(own_entry.get(), other_entry.get()))

own_msg.grid(column=0, row=0)
own_entry.grid(column=1, row=0)

other_msg.grid(column=0, row=1)
other_entry.grid(column=1, row=1)

process_button.grid(column=2, row=0, rowspan=2)

root.mainloop()
