import snake
from tkinter import *
s = snake.Snake()

s.initGame(10)
s.step(2)
s.render()

master = Tk()
w = Canvas(master, width=200, height=200)
w.pack()
s.render(master, w)