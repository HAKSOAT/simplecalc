import tkinter as tk

window = tk.Tk()

display = tk.Entry(window, state = tk.DISABLED)
display.grid(column = 0, columnspan = 4, row = 0, ipadx = 20, ipady = 8, pady = 10, padx = 15)

button_seven = tk.Button(window, text = "7")
button_seven.grid(column = 0, row = 1, sticky = tk.N+tk.S+tk.E+tk.W, padx = [15, 0])

button_eight = tk.Button(window, text = "8")
button_eight.grid(column = 1, row = 1, sticky = tk.N+tk.S+tk.E+tk.W)

button_nine = tk.Button(window, text = "9")
button_nine.grid(column = 2, row = 1, sticky = tk.N+tk.S+tk.E+tk.W)

button_plus = tk.Button(window, text = "+")
button_plus.grid(column = 3, row = 1, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])

button_four = tk.Button(window, text = "4")
button_four.grid(column = 0, row = 2, sticky = tk.N+tk.S+tk.E+tk.W, padx = [15, 0])

button_five = tk.Button(window, text = "5")
button_five.grid(column = 1, row = 2, sticky = tk.N+tk.S+tk.E+tk.W)

button_six = tk.Button(window, text = "6")
button_six.grid(column = 2, row = 2, sticky = tk.N+tk.S+tk.E+tk.W)

button_minus = tk.Button(window, text = "-")
button_minus.grid(column = 3, row = 2, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])

button_one = tk.Button(window, text = "1")
button_one.grid(column = 0, row = 3, sticky = tk.N+tk.S+tk.E+tk.W, padx = [15, 0])

button_two = tk.Button(window, text = "2")
button_two.grid(column = 1, row = 3, sticky = tk.N+tk.S+tk.E+tk.W)

button_three = tk.Button(window, text = "3")
button_three.grid(column = 2, row = 3, sticky = tk.N+tk.S+tk.E+tk.W)

button_times = tk.Button(window, text = "*")
button_times.grid(column = 3, row = 3, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])

button__ = tk.Label(window)
button__.grid(column = 0, row = 4, sticky = tk.N+tk.S+tk.E+tk.W, padx = [15, 0])

button_zero = tk.Button(window, text = "0")
button_zero.grid(column = 1, row = 4, sticky = tk.N+tk.S+tk.E+tk.W)

button_ = tk.Label(window)
button_.grid(column = 2, row = 4, sticky = tk.N+tk.S+tk.E+tk.W)

button_slash = tk.Button(window, text = "/")
button_slash.grid(column = 3, row = 4, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])

button_equals = tk.Button(window, text = "=")
button_equals.grid(column = 3, row = 5, sticky = tk.N+tk.S+tk.E+tk.W, padx = [5, 15])

button_clear = tk.Button(window, text = "Clear")
button_clear.grid(column = 1, columnspan = 2, row = 6, sticky = tk.N+tk.S+tk.E+tk.W, pady = 8)

window.mainloop()