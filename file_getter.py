import tkinter as tk
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(initialdir=os.getcwd(), 
                                       title="get your mod file", 
                                       filetypes=(("HTML files", "*.html"), 
                                                  ("all files", "*.*")))
print(file_path)
print(type(file_path))