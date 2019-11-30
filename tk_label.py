import tkinter as tk

root= tk.Tk()


# window frame
canvas = tk.Canvas(root, width = 600, height = 400)
canvas.pack()

# label
label_input = tk.Label(root, text= 'Hello, world!', fg='blue', font=('courier new', 12, 'normal'))
canvas.create_window(300, 50, window=label_input)

root.mainloop()
