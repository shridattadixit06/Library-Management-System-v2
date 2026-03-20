from modules.stylings import *
from tkinter import *

def menu_button(text, cmd, y, win_name):
            Button(
                win_name, text=text, command=cmd,
                fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                width=25, height=2, bd=0,
                cursor="hand2"
            ).place(relx=0.5, y=y, anchor="center")