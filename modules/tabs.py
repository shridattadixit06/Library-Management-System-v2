from tkinter import *
from modules.stylings import *
import pymsgbox
from modules.actions import menu_button
import modules.actions as actions
import sqlite3

def register_tab(parent_win,main_win,main_func):
            parent_win.destroy()
            registerwin = Canvas(main_win, bg=BG_MAIN, highlightthickness=0)
            registerwin.pack(fill="both", expand=True)

            categories = ['Programming', 'Economics', 'Science']
            selected_option = StringVar(value=categories[0])

            Label(registerwin, text="Register Book", font=FONT_TITLE,
                  fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=120, anchor="center")

            Label(registerwin, text="Category", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=220)

            OptionMenu(registerwin, selected_option, *categories)\
                .place(x=540, y=250)

            Label(registerwin, text="Book Name", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=300)

            booktxt = Text(registerwin, width=30, height=1,
                           font=FONT_ENTRY, bg=ENTRY_BG)
            booktxt.place(x=540, y=330)

            Label(registerwin, text="Book ID", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=370)

            bookidtxt = Text(registerwin, width=30, height=1,
                             font=FONT_ENTRY, bg=ENTRY_BG)
            bookidtxt.place(x=540, y=400)

            def registerbook():
                book = booktxt.get("1.0", "end-1c")
                bid = bookidtxt.get("1.0", "end-1c")
                if not book or not bid:
                    pymsgbox.alert("All fields are required")
                    return

                barred_id_chars = ["!","@","$","%","^","&","*","(",")","-","_","+","=","~","`","'","<",">",",",".","/","|",":",";","{","}","[","]"]
                flag=0
                for let in bid:
                     if let in barred_id_chars:
                          flag=1
                if not flag:
                    conn = sqlite3.connect("books\\"+selected_option.get())
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO "+selected_option.get().lower()+" (bookname, bookID) VALUES(?, ?)",(book,bid))
                    conn.commit()
                    pymsgbox.alert("Book Registered Successfully")
                    booktxt.delete("1.0", END)
                    bookidtxt.delete("1.0", END)
                    cursor.close()
                    conn.close()

                else:
                    pymsgbox.alert("Barred characters like !@$^&*()-_+=~`'<>,./|:'{'}'[] found in Book ID.")
            Button(registerwin, text="✔ Register", command=registerbook,
                   fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=460)

            Button(registerwin, text="⬅ Back",
                   command=lambda: (registerwin.destroy(), main_func()),
                   fg=BTN_FG, bg=BTN_EXIT, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=520)
def lend_tab(parent_win,main_win,main_func):
            parent_win.destroy()
            lendwin = Canvas(main_win, bg=BG_MAIN, highlightthickness=0)
            lendwin.pack(fill="both", expand=True)

            Label(lendwin, text="Lend Book", font=FONT_TITLE,
                  fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=120, anchor="center")

            labels = ["Student Name", "Student USN", "Book ID"]
            entries = []
            y = 260

            for text in labels:
                Label(lendwin, text=text, fg=LBL_FG,
                      bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=y)
                t = Text(lendwin, width=30, height=1,
                         font=FONT_ENTRY, bg=ENTRY_BG)
                t.place(x=540, y=y+30)
                entries.append(t)
                y += 80

            def lend():
                vals = [e.get("1.0", "end-1c") for e in entries]
                if "" in vals:
                    pymsgbox.alert("All fields are required")
                    return
                connection = sqlite3.connect("books//lent.db")
                cursor=connection.cursor()
                cmd = """CREATE TABLE IF NOT EXISTS lentbooks(name TEXT,usn INTEGER,bookID TEXT PRIMARY KEY)"""
                cursor.execute(cmd)
                cursor.execute("INSERT INTO lentbooks (name, usn, bookID) VALUES(?, ?, ?)",(vals[0],vals[1],vals[2]))
                connection.commit()
                cursor.execute("SELECT * FROM lentbooks")
                connection.commit()
                cursor.close()
                pymsgbox.alert("Book Lent Successfully")
                for e in entries:
                    e.delete("1.0", END)

            Button(lendwin, text="📤 Lend", command=lend,
                   fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=520)

            Button(lendwin, text="⬅ Back",
                   command=lambda: (lendwin.destroy(), main_func()),
                   fg=BTN_FG, bg=BTN_EXIT, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=580)
def returnbookwin(parent_win,main_win,main_func):
            parent_win.destroy()
            retwin = Canvas(main_win, bg=BG_MAIN, highlightthickness=0)
            retwin.pack(fill="both", expand=True)

            Label(retwin, text="Return Book", font=FONT_TITLE,
                  fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=120, anchor="center")

            Label(retwin, text="Student Name", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=280)
            nametxt = Text(retwin, width=30, height=1,
                           font=FONT_ENTRY, bg=ENTRY_BG)
            nametxt.place(x=540, y=310)

            Label(retwin, text="Book ID", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=360)
            bookidtxt = Text(retwin, width=30, height=1,
                             font=FONT_ENTRY, bg=ENTRY_BG)
            bookidtxt.place(x=540, y=390)

            def returnbook():
                name = nametxt.get("1.0", "end-1c")
                bid = bookidtxt.get("1.0", "end-1c")
                if not name or not bid:
                    pymsgbox.alert("All fields are required")
                    return

                found = False
                with open("lend.txt", "r") as f:
                    lines = f.readlines()

                with open("lend.txt", "w") as f:
                    for line in lines:
                        data = line.strip().split(",")
                        if bid == data[2]:
                            found = True
                        else:
                            f.write(line)

                if found:
                    pymsgbox.alert("Book Returned Successfully")
                else:
                    pymsgbox.alert("Book ID not found in lending records")

                nametxt.delete("1.0", END)
                bookidtxt.delete("1.0", END)

            Button(retwin, text="📥 Return", command=returnbook,
                   fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=460)

            Button(retwin, text="⬅ Back",
                   command=lambda: (retwin.destroy(), main_func()),
                   fg=BTN_FG, bg=BTN_EXIT, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=520)
def opencmd(parent_win,main_win,main_func,app_pass):
        pwd = pymsgbox.password(title="Password", text="Enter the password")
        if pwd != app_pass:
            pymsgbox.alert("Enter the correct password")
            return

        parent_win.destroy()
        openwin = Canvas(main_win, bg=BG_MAIN, highlightthickness=0)
        openwin.pack(fill="both", expand=True)  
        Label(openwin, text="Library Dashboard", font=FONT_TITLE,
              fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=140, anchor="center")
        
        def exttoopen(mwin,mainfunction):
             mwin.destroy()
             mainfunction()
        global display_register
        def display_register(path):
             pwd = pymsgbox.password("Enter Password","Security Verification")
             if pwd==app_pass:
                connection = sqlite3.connect(path)
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM lentbooks")
                results=cursor.fetchall()
                t = Text(openwin,height=25,width=50)
                t.place(x=810,y=50)
                t.tag_configure("bold_tag", font=("Arial", 12, "bold"))
                t.config(state='normal')
                t.insert(END, "STUDENT NAME"+'\t\t\t')
                t.insert(END, "STUDENT USN"+'\t\t')
                t.insert(END, "BOOK ID"+'\n')
                for info in results:
                     t.insert(END, info[0]+'\t\t\t')
                     t.insert(END, str(info[1])+'\t\t')
                     t.insert(END, info[2]+'\n')
                t.config(state='disabled')
                def des_display():
                    t.destroy()
                    c_display.destroy()
                c_display = Button(openwin,text="Close",command=des_display,fg=BTN_FG,bg=BTN_BG,font=FONT_BTN)
                c_display.place(x=965,y=460)
                cursor.close()
                connection.close()
             else:
                  pymsgbox.alert("Wrong password")      
        menu_button("📘 Register Book",lambda:register_tab(openwin,main_win,main_func), 220,openwin)
        menu_button("📤 Lend Book",lambda:lend_tab(openwin,main_win,main_func), 280,openwin)
        menu_button("📥 Register Return",lambda:returnbookwin(openwin,main_win,main_func), 340,openwin)
        menu_button("📘 Available Books",lambda: actions.display_books(openwin,50,50,25,25),400,openwin)
        menu_button("📘 Lent Register", lambda:display_register("books\\lent.db"),460,openwin)
        menu_button("❌ Exit", lambda: exttoopen(openwin,main_func), 520,openwin)
        