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
		
	label = tk.Label(root, text= 'Checked = ' + str(v.get()),
		fg='green', font=('helvetica', 12, 'bold'))
	canvas.create_window(300, 250, window=label)

# check button
check = tk.Checkbutton(root, text='CheckButton Sample', 
	    command=show_status, variable=v, onvalue=1, offvalue=0)
canvas.create_window(100, 50, window=check)

root.mainloop()
