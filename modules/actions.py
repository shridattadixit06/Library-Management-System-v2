from modules.stylings import *
from tkinter import *

def menu_button(text, cmd, y, win_name):
            Button(
                win_name, text=text, command=cmd,
                fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                width=25, height=2, bd=0,
                cursor="hand2"
            ).place(relx=0.5, y=y, anchor="center")
def display_books(file_path,win_name,xc,yc,h,w):
        text_widget = Text(win_name,height=h,width=w)
        text_widget.place(x=xc,y=yc)
        text_widget.config(state="normal")
        text_widget.tag_configure("bold_tag", font=("Arial", 12, "bold"))
        fle = open(file_path,'r')
        for line in fle:
                text_widget.insert(END, line+'\n')
        text_widget.config(state="disabled")
def navbar_button(win_name,text,comm,xcoord,ycoord):
       Button(win_name,text=text,command=comm).place(x=xcoord,y=ycoord)