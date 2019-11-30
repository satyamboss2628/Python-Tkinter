import tkinter as tk

root= tk.Tk()


# window frame
canvas = tk.Canvas(root, width = 600, height = 400)
canvas.pack()

label_input = tk.Label(root, text= 'Enter your name', fg='blue', font=('courier new', 12, 'normal'))
canvas.create_window(300, 50, window=label_input)

# text box
textbox_input=tk.Text(root, height=1, width=25)
canvas.create_window(300, 100, window=textbox_input)

# function to read text box
def get_input():
    return textbox_input.get("1.0","end-1c")

# function to display "Hello World!"
def hello ():
	label = tk.Label(root, text= 'Hello, ' + get_input(), fg='green', font=('helvetica', 12, 'bold'))
	canvas.create_window(300, 250, window=label)

# command button
button = tk.Button(text='Click Me',command=hello, bg='blue',fg='white')
canvas.create_window(300, 150, window=button)

root.mainloop()
