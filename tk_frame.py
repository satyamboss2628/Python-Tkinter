import tkinter as tk

root = tk.Tk()

# windowwin frame
canvas = tk.Canvas(root, width = 500, height = 400)
canvas.pack()

# layout frame
frame = tk.Frame(root, bg='blue', width = 300, height = 200)
canvas.create_window(10, 10, window=frame, anchor='nw')

root.mainloop()
