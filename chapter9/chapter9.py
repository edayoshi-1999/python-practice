import tkinter as tk 
from tkinter import ttk

# root = tk.Tk()
# root.title("タイトル")
# root.geometry("300x150+50+500")
# root.mainloop()

# root = tk.Tk()
# frame_pack = ttk.LabelFrame(text="pack")
# frame_pack.pack()
# label1 = ttk.Label(frame_pack, text="Hello")
# label1.pack(side="right")
# label2 = ttk.Label(frame_pack, text="tkinter!")
# label2.pack()
# frame_grid = ttk.LabelFrame(text="grid")
# frame_grid.pack()
# label3 = ttk.Label(frame_grid, text="Hello")
# label3.grid(row=0, column=0)
# label4 = ttk.Label(frame_grid, text="tkinter!")
# label4.grid(row=1, column=1)
# root.mainloop()

# def say_hello():
#     print("Hello tkinter!")
# root = tk.Tk()
# button = ttk.Button(text="Hello", command=say_hello)
# button.pack()
# root.mainloop()

def print_Entry():
    print(entry_variable.get())
root = tk.Tk()
entry_variable = tk.StringVar()
entry_variable.set("Hello tkinter!")
entry = ttk.Entry(textvariable=entry_variable)
entry.pack()
button = ttk.Button(text="Entry", command=print_Entry)
button.pack()
root.mainloop()
