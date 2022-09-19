from tkinter import *
from turtle import left
import settings, utils

root = Tk() #window
#indow settings override
root.configure(bg='#EF9D5A')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('minesweeper game')
root.resizable(False, False) #avoiding resizing of a window

top_frame = Frame(
    root,
    bg='black',
    width=720,
    height=utils.height_percent(25),
)
top_frame.place(x=0, y=0)

#left sidebar for scores
left_frame = Frame(
    root,
    bg='#28D1C0',
    width=utils.width_percent(25),
    height=utils.height_percent(75),
)
left_frame.place(x=0, y=utils.height_percent(25))


#dedicated to the game
center_frame = Frame(
    root,
    bg = '#B2B8ED',
    width=utils.width_percent(75),
    height=utils.height_percent(75),
)
center_frame.place(
    x=utils.width_percent(25), 
    y=utils.height_percent(25)
    )

#run the window
root.mainloop()