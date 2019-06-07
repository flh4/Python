#Frederick Herzog
#A basic template for tkinter

import tkinter as tk 

HEIGHT = 300
WIDTH = 400
COLOR = '#81F79F'

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(window, bg=COLOR)
frame.place(relwidth=1, relheight=1)


window.mainloop()
