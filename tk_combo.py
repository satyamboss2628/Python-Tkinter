import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

# windowwin frame
canvas = tk.Canvas(root, width = 600, height = 400)
canvas.pack()

# combobox
course = ["Java","Python","C & C++"]
combo = ttk.Combobox(root, values=course, width=10)
canvas.create_window(250, 50, window=combo)
combo.current(0)

root.mainloop()
