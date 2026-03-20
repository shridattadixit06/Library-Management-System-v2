from tkinter import *
import pymsgbox
from modules.stylings import *
from modules.actions import menu_button
import modules.tabs as tabs
APP_PASSWORD = "123"

win = Tk()
win.title("Library Management System")
win.configure(background=BG_MAIN)
win.state("zoomed")

def main():
    mainwin = Canvas(win, bg=BG_MAIN, highlightthickness=0)
    mainwin.pack(fill="both", expand=True)
    Button(mainwin, text="OPEN LIBRARY", command=lambda:tabs.opencmd(mainwin,win,main,APP_PASSWORD),
           fg=BTN_FG, bg=BTN_BG, font=FONT_TITLE,
           width=20, height=2, bd=0).place(relx=0.5, rely=0.5, anchor="center")

main()
win.mainloop()