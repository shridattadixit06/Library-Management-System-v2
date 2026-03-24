from modules.stylings import *
from tkinter import *
import pymsgbox
import sqlite3
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
        conn = sqlite3.connect("books//"+genre+"_books.db")
        cursor = conn.cursor()
        print(genre)
        cmd = "SELECT * FROM "+genre
        cursor.execute(cmd)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        text_widget = Text(win_name,height=h,width=w)
        text_widget.place(x=xc,y=yc)
        text_widget.config(state="normal")
        text_widget.tag_configure("bold_tag", font=("Arial", 12, "bold"))
        text_widget.insert(END, 'BOOK NAME'+'\t\t')
        text_widget.insert(END, 'BOOK ID'+'\n')
        for row in results:
                text_widget.insert(END, row[0]+'\t\t')
                text_widget.insert(END, row[1]+'\n')
        text_widget.config(state="disabled")
        def destroy_display():
               text_widget.destroy()
               close_display.destroy()
        close_display = Button(win_name,command=destroy_display,text="Close Display",font=FONT_BTN,bg=BTN_BG,fg=BTN_FG)
        close_display.place(x=xc+40,y=yc+420)