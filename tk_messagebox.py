import tkinter as tk
import tkinter.messagebox as messagebox

# function to show messagebox
def show_message():
    messagebox.showinfo('Python Tkonter', 'This is a test message.')
    
root = tk.Tk()

# windowwin frame
canvas = tk.Canvas(root, width = 600, height = 400)
canvas.pack()

# button
button = tk.Button(root, text='Show Message', command=show_message, bg='blue',fg='white', width = 20, height = 2)
canvas.create_window(300, 200, window=button)

root.mainloop()
