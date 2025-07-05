import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Table")

# Define columns
columns = ("Name", "Age", "Occupation")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Set column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insert data
data = [
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Doctor"),
    ("Charlie", 22, "")
]
for row in data:
    tree.insert("", tk.END, values=row)

tree.pack()

root.mainloop()