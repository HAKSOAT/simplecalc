import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.maxsize(215, 250)
window.minsize(215, 250)
window.title("Simple Calc")

equals_clicked = 0

def click(event):
	global equals_clicked
	if equals_clicked == 1:
		display['state'] = tk.NORMAL
		display.delete(0, tk.END)
		display.insert(tk.END, event.widget["text"])
		print(display.get())
		display['state'] = tk.DISABLED
		equals_clicked = 0
	else:
		display['state'] = tk.NORMAL
		display.insert(tk.END, event.widget["text"])
		print(display.get())
		display['state'] = tk.DISABLED

def calculate(event):
	global equals_clicked
	if display.get()[-1] in ["+", "-", "*", "/"]:
		message = "This is an invalid\n maths operation"
		messagebox.showerror("Invalid Operation", message)
		clear()

	elif display.get()[0] in ["*", "/"]:
		message = "This is an invalid\n maths operation"
		messagebox.showerror("Invalid Operation", message)
		clear()

	else:
		answer = eval(display.get())
		display['state'] = tk.NORMAL
		display.delete(0, tk.END)
		display.insert(0, answer)
		display['state']= tk.DISABLED
		equals_clicked = 1

def clear(event = None):
	display['state'] = tk.NORMAL
	display.delete(0, tk.END)
	display['state']= tk.DISABLED
	


v = tk.StringVar()
display = tk.Entry(window, textvariable = v, state= tk.DISABLED)
display.grid(column = 0, columnspan = 4, row = 0, ipadx = 20, ipady = 8, pady = 10, padx = 15)

button_seven = tk.Button(window, text = "7")
button_seven.grid(column = 0, row = 1, sticky = tk.N+tk.S+tk.E+tk.W, padx = [15, 0])
button_seven.bind('<Button-1>', click)

button_eight = tk.Button(window, text = "8")
button_eight.grid(column = 1, row = 1, sticky = tk.N+tk.S+tk.E+tk.W)
button_eight.bind('<Button-1>', click)

button_nine = tk.Button(window, text = "9")
button_nine.grid(column = 2, row = 1, sticky = tk.N+tk.S+tk.E+tk.W)
button_nine.bind('<Button-1>', click)

button_plus = tk.Button(window, text = "+")
button_plus.grid(column = 3, row = 1, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])
button_plus.bind('<Button-1>', click)

button_four = tk.Button(window, text = "4")
button_four.grid(column = 0, row = 2, sticky = tk.N+tk.S+tk.E+tk.W, padx = [15, 0])
button_four.bind('<Button-1>', click)

button_five = tk.Button(window, text = "5")
button_five.grid(column = 1, row = 2, sticky = tk.N+tk.S+tk.E+tk.W)
button_five.bind('<Button-1>', click)

button_six = tk.Button(window, text = "6")
button_six.grid(column = 2, row = 2, sticky = tk.N+tk.S+tk.E+tk.W)
button_six.bind('<Button-1>', click)

button_minus = tk.Button(window, text = "-")
button_minus.grid(column = 3, row = 2, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])
button_minus.bind('<Button-1>', click)

button_one = tk.Button(window, text = "1")
button_one.grid(column = 0, row = 3, sticky = tk.N+tk.S+tk.E+tk.W, padx = [15, 0])
button_one.bind('<Button-1>', click)

button_two = tk.Button(window, text = "2")
button_two.grid(column = 1, row = 3, sticky = tk.N+tk.S+tk.E+tk.W)
button_two.bind('<Button-1>', click)

button_three = tk.Button(window, text = "3")
button_three.grid(column = 2, row = 3, sticky = tk.N+tk.S+tk.E+tk.W)
button_three.bind('<Button-1>', click)

button_times = tk.Button(window, text = "*")
button_times.grid(column = 3, row = 3, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])
button_times.bind('<Button-1>', click)

button_zero = tk.Button(window, text = "0")
button_zero.grid(column = 1, row = 4, sticky = tk.N+tk.S+tk.E+tk.W)
button_zero.bind('<Button-1>', click)

button_slash = tk.Button(window, text = "/")
button_slash.grid(column = 3, row = 4, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])
button_slash.bind('<Button-1>', click)

button_equals = tk.Button(window, text = "=")
button_equals.grid(column = 3, row = 5, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])
button_equals.bind('<Button-1>', calculate)

button_clear = tk.Button(window, text = "Clear")
button_clear.grid(column = 1, columnspan = 2, row = 6, sticky = tk.N+tk.S+tk.E+tk.W, pady = 8)
button_clear.bind('<Button-1>', clear)

window.mainloop()