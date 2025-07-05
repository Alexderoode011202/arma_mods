from tkinter import Tk, Label, Entry, Button
from typing import List, Tuple, Set, Dict
from functions import fully_process


data: Dict[str, List[Tuple[str, str]]]

    
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
