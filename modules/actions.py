from modules.stylings import *
from tkinter import *
import pymsgbox
def menu_button(text, cmd, y, win_name):
            Button(
                win_name, text=text, command=cmd,
                fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                width=25, height=2, bd=0,
                cursor="hand2"
            ).place(relx=0.5, y=y, anchor="center")
def display_books(win_name,xc,yc,h,w):
        genre = pymsgbox.prompt(text="Which type of books you want?(Economics,Programming,Science)",title="Receiptionist")
        genre = genre.lower()
        genre = genre.capitalize()
        for genres in files:
            if genres==genre:
                path=files[genres]
        text_widget = Text(win_name,height=h,width=w)
        text_widget.place(x=xc,y=yc)
        text_widget.config(state="normal")
        text_widget.tag_configure("bold_tag", font=("Arial", 12, "bold"))
        fle = open(path,'r')
        for line in fle:
                text_widget.insert(END, line+'\n')
        text_widget.config(state="disabled")
def navbar_button(win_name,text,comm,xcoord,ycoord):
       Button(win_name,text=text,command=comm).place(x=xcoord,y=ycoord)