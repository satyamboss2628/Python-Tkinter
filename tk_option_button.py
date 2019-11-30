import tkinter as tk

root= tk.Tk()
v = tk.IntVar()
v.set(1)

# window frame
canvas = tk.Canvas(root, width = 600, height = 400)
canvas.pack()

# function to display click_count
def show_status ():
	global v
	label = tk.Label(root, text= 'Click = ' + str(v.get()), fg='green', font=('helvetica', 12, 'bold'))
	canvas.create_window(300, 250, window=label)

# option button one
radio_one = tk.Radiobutton(root, text="One", variable=v, value=1, command=show_status)
canvas.create_window(50, 50, window=radio_one)

# option button two
radio_two = tk.Radiobutton(root, text="Two", variable=v, value=2, command=show_status)
canvas.create_window(50, 100, window=radio_two)

# option button three
radio_three = tk.Radiobutton(root, text="Three", variable=v, value=3, command=show_status)
canvas.create_window(50, 150, window=radio_three)

root.mainloop()
