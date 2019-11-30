import tkinter as tk

root= tk.Tk()
click_count = 0

# window frame
canvas = tk.Canvas(root, width = 600, height = 400)
canvas.pack()

# function to display click_count
def show_status ():
	global click_count
	click_count += 1
	label = tk.Label(root, text= 'Click = ' + str(click_count), fg='green', font=('helvetica', 12, 'bold'))
	canvas.create_window(300, 250, window=label)

# command button
button = tk.Button(text='Click This Button',command=show_status, bg='blue', fg='white', width = 20, height = 2)
canvas.create_window(300, 150, window=button)

root.mainloop()
