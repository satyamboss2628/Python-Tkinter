import tkinter as tk
import tkinter.scrolledtext as scrolledtext

root = tk.Tk()
root.resizable(0,0)

# windowwin frame
canvas = tk.Canvas(root, width = 520, height = 400)
canvas.pack()

# scrolledtext
input_textbox = scrolledtext.ScrolledText(root, undo=True, font=('courier new', 10))
canvas.create_window(10, 40, width = 500, height = 300, window=input_textbox, anchor='nw')

root.mainloop()
