from tkinter import *
from datetime import datetime, date
from hotelbackend import BOOK
import mysql.connector as msqc
import numpy as np

db = msqc.connect(
    host="localhost",
    username="root",
    password=" ",
    database="graphic_hotel",
)
cur = db.cursor(buffered=True)
win = Tk()
win.iconbitmap("all_seeing_eye_1698551_1280_lV8_icon.ico")
win.title("HOTEL ILLUMINATI")
# Name entry
name_label = Label(win, text="First Name :-", font=("Arial bold", 10))
name_label.grid(row=0, column=0, pady=18)
first_name_entry = Entry(win, width=30, borderwidth=5)
first_name_entry.grid(row=0, column=1, columnspan=3)
# Name entry
name_label_last = Label(win, text="Last Name :-", font=("Arial bold", 10))
name_label_last.grid(row=1, column=0, pady=10)
second_name_entry = Entry(win, width=30, borderwidth=5)
second_name_entry.grid(row=1, column=1, pady=10, columnspan=3)
# Date
time_label = Label(win, text="Check in :-\nTime", font=("Arial bold", 10))
time_label.grid(row=2, column=0, pady=10, padx=10)
time_entry = Entry(win, width=8, borderwidth=5)
time_entry.grid(row=2, column=1, pady=10, padx=0)
time_entry.insert(0, datetime.now().strftime("%H:%M"))
# Date:
date_label = Label(win, text="Check in :-\nDate ", font=("Arial bold", 10))
date_label.grid(row=2, column=2, pady=10)
date_entry = Entry(win, width=12, borderwidth=5)
date_entry.grid(row=2, column=3, pady=10)
date_entry.insert(0, date.today())

# Number of members
members_label = Label(win, text=" No. of members:-", font=("Arial bold", 10))
members_label.grid(row=3, column=0, pady=4)
members_entry = Entry(win, width=3, borderwidth=5)
members_entry.grid(row=3, column=1, pady=4)

# Contact Number
contact_number_label = Label(win, text="Contact No. :-", font=("Arial bold", 10))
contact_number_label.grid(row=3, column=2, pady=6)
contact_number_entry = Entry(win, width=10, borderwidth=5)
contact_number_entry.grid(row=3, column=3, pady=6)

# no. of days
days_label = Label(win, text="No. of days :-", font=("Arial bold", 10))
days_label.grid(row=4, column=0, pady=6)
days_entry = Entry(win, width=3, borderwidth=5)
days_entry.grid(row=4, column=1, pady=6)

# amount
amount_label = Label(win, text="Total Amount:-", font=("Arial bold", 10))
amount_label.grid(row=4, column=2, pady=6)
amount_entry = Entry(win, width=10, borderwidth=5)
amount_entry.grid(row=4, column=3, pady=6)


# define button
def one_bed():
    win_one = Toplevel(relief = SUNKEN)
    win_one.iconbitmap("all_seeing_eye_1698551_1280_lV8_icon.ico")
    header = """+-----------+-------------------+
| Room-no | Available_one_bed |
+-----------+-------------------+"""
    txt = Label(win_one, borderwidth=8, text=header, relief = SUNKEN ).grid(
        row=0, column=0, columnspan=2, pady=5, padx=10
    )
    txt_lbl = Label(win_one, borderwidth=8, text=header, relief = SUNKEN ).grid(
        row=0, column=2, columnspan=2, pady=5, padx=10
    )
    ss = "SELECT one_bed ,Available_one_bed from rooms"
    cur.execute(ss)
    available_room_no = cur.fetchall()
    i = 0
    for x in available_room_no:
        stri = str(x[0]) + "       " + "    " + "    " + x[1]
        if x[1] == "N/A":
            stri = str(x[0]) + "               " + "    " + "    " + x[1]

        if i < 20:
            txt1 = Label(win_one, borderwidth=8, text=stri ).grid(
                row=i + 1, column=0, columnspan=2
            )
            i = i + 1
        else:
            txt1 = Label(win_one, borderwidth=8, text=stri ).grid(
                row=i - 19, column=2, columnspan=2
            )
            i = i + 1


def two_bed():
    win_two = Toplevel()
    win_two.iconbitmap("all_seeing_eye_1698551_1280_lV8_icon.ico")
    header = """+-----------+-------------------+
| Room-no | Available_two_beds |
+-----------+-------------------+"""
    txt = Label(win_two, borderwidth=8, text=header, relief = SUNKEN).grid(
        row=0, column=0, columnspan=2, pady=5, padx=10
    )
    txt_lbl = Label(win_two, borderwidth=8, text=header, relief = SUNKEN).grid(
        row=0, column=2, columnspan=2, pady=5, padx=10
    )
    ss = "SELECT two_beds ,Available_two_bed from rooms"
    cur.execute(ss) 
    available_room_no = cur.fetchall()
    i = 0
    for x in available_room_no:
        stri = str(x[0]) + "       " + "    " + "    " + x[1]
        if x[1] == "N/A":
            stri = str(x[0]) + "               " + "    " + "    " + x[1]

        if i < 20:
            txt1 = Label(win_two, borderwidth=8, text=stri).grid(
                row=i + 1, column=0, columnspan=2
            )
            i = i + 1
        else:
            txt1 = Label(win_two, borderwidth=8, text=stri).grid(
                row=i - 19, column=2, columnspan=2
            )
            i = i + 1


def three_bed():
    win_three = Toplevel()
    win_three.iconbitmap("all_seeing_eye_1698551_1280_lV8_icon.ico")
    header = """+-------------+-------------------+
| Room-no | Available_three_beds |
+-------------+-------------------+"""
    txt = Label(win_three, borderwidth=8, text=header, relief = SUNKEN).grid(
        row=0, column=0, columnspan=2, pady=5, padx=10
    )
    txt_lbl = Label(win_three, borderwidth=8, text=header, relief = SUNKEN ).grid(
        row=0, column=2, columnspan=2, pady=5, padx=10
    )
    ss = "SELECT three_beds ,Available_three_bed from rooms"
    cur.execute(ss)
    available_room_no = cur.fetchall()
    i = 0
    for x in available_room_no:
        stri = str(x[0]) + "       " + "    " + "    " + x[1]
        if x[1] == "N/A":
            stri = str(x[0]) + "               " + "    " + "    " + x[1]

        if i < 20:
            txt1 = Label(win_three, borderwidth=8, text=stri).grid(
                row=i + 1, column=0, columnspan=2
            )
            i = i + 1
        else:
            txt1 = Label(win_three, borderwidth=8, text=stri).grid(
                row=i - 19, column=2, columnspan=2
            )
            i = i + 1


# buttons

available_one_bed_button = Button(
    win,
    text="Available one bed",
    font=("Arial bold", 10 - 2),
    height=2,
    width=15,
    command=one_bed,
    borderwidth=5,
)
available_one_bed_button.grid(row=0, column=4, pady=13, padx=7)

available_two_bed_button = Button(
    win,
    text="Available two beds",
    font=("Arial bold", 10 - 2),
    height=2,
    width=15,
    command=two_bed,
    borderwidth=5,
)
available_two_bed_button.grid(row=1, column=4, pady=10, padx=7)

available_three_bed_button = Button(
    win,
    text="Available three beds",
    font=("Arial bold", 10 - 2),
    height=2,
    width=16,
    command=three_bed,
    borderwidth=5,
)
available_three_bed_button.grid(row=2, column=4, pady=10, padx=7)

# Bed Button
bed_label = Label(win, text="Beds :-\n[1 bed 2 people]", font=("Arial bold", 10))
bed_label.grid(row=5, column=0)
bed_entry = Entry(win, width=3, borderwidth=5)
bed_entry.grid(row=5, column=1, pady=6)

scrol = Scale(win, from_=1, to=3, orient="horizontal")
scrol.grid(row=6, column=1)

# defining bed button i
def set_bed():
    bed_size = scrol.get()
    bed_entry.delete(0, END)
    bed_entry.insert(0, str(bed_size))


# button to set bed
button_set = Button(
    win,
    text="Set Beds",
    width=7,
    borderwidth=5,
    font=("Arial bold", 8),
    command=set_bed,
)
button_set.grid(row=6, column=0)
# Defining the booking buttons


def book():
    name = first_name_entry.get() + " " + second_name_entry.get()
    time = time_entry.get()
    date = date_entry.get()
    mem = members_entry.get()
    global conctact
    conctact = contact_number_entry.get()
    day = days_entry.get()
    amount_entry.delete(0, END)
    amount_entry.insert(0, str(1200 * int(day)))
    bed = bed_entry.get()
    money = amount_entry.get()
    global operation

    def clear_button():
        lbl_confirm.destroy()
        lbl_no.destroy()
        bed_entry.delete(0, END)
        amount_entry.delete(0, END)
        days_entry.delete(0, END)
        contact_number_entry.delete(0, END)
        members_entry.delete(0, END)
        first_name_entry.delete(0, END)
        second_name_entry.delete(0, END)
        clear_buton = Button(
            win,
            text="Clear",
            font=("Arial bold", 12),
            width=7,
            height=4,
            borderwidth=5,
            command=clear_button,
            state="disable",
        )
        clear_buton.grid(row=6, column=4, columnspan=5)

    operation = BOOK(name, date, time, 0, 0, mem, conctact, bed, day, money)
    if bed == "1":
        operation.one_bed()
        ss = "SELECT Room_no from booking where Contact_no = " + str(conctact)
        cur.execute(ss)
        no = cur.fetchone()[0]
        # no = 101
        lbl_no = Label(
            win, text="Room No :\n" + str(no) + "\nBooked", font=("Arial bold", 12)
        )
        lbl_no.grid(row=6, column=1, columnspan=5)
        lbl_confirm = Label(
            win, text="Database Updated\nSuccessfully !", font=("bold", 12), fg="green"
        )
        lbl_confirm.grid(row=5, column=4, columnspan=5)
        clear_btton = Button(
            win,
            text="Clear",
            font=("Arial bold", 12),
            width=7,
            height=4,
            borderwidth=5,
            command=clear_button,
            state="active",
        )
        clear_btton.grid(row=6, column=4, columnspan=5)
    if bed == "2":
        operation.two_bed()
        ss = "SELECT Room_no from booking where Contact_no = " + str(conctact)
        cur.execute(ss)
        no = cur.fetchone()[0]
        # no = 101
        lbl_no = Label(
            win, text="Room No :\n" + str(no) + "\nBooked", font=("Arial bold", 12)
        )
        lbl_no.grid(row=6, column=1, columnspan=5)
        lbl_confirm = Label(
            win, text="Database Updated\nSuccessfully !", font=("bold", 12), fg="green"
        )
        lbl_confirm.grid(row=5, column=4, columnspan=5)
        clear_btton = Button(
            win,
            text="Clear",
            font=("Arial bold", 12),
            width=7,
            height=4,
            borderwidth=5,
            command=clear_button,
            state="active",
        )
        clear_btton.grid(row=6, column=4, columnspan=5)
    if bed == "3":
        operation.three_bed()
        ss = "SELECT Room_no from booking where Contact_no = " + str(conctact)
        cur.execute(ss)
        no = cur.fetchone()[0]
        # no = 101
        lbl_no = Label(
            win, text="Room No :\n" + str(no) + "\nBooked", font=("Arial bold", 12)
        )
        lbl_no.grid(row=6, column=1, columnspan=5)
        lbl_confirm = Label(
            win, text="Database Updated\nSuccessfully !", font=("bold", 12), fg="green"
        )
        lbl_confirm.grid(row=5, column=4, columnspan=5)
        clear_btton = Button(
            win,
            text="Clear",
            font=("Arial bold", 12),
            width=7,
            height=4,
            borderwidth=5,
            command=clear_button,
            state="active",
        )
        clear_btton.grid(row=6, column=4, columnspan=5)


# book and Check out
clear_button = Button(
    win,
    text="Clear",
    font=("Arial bold", 12),
    width=7,
    height=4,
    borderwidth=5,
    state="disable",
)
clear_button.grid(row=6, column=4, columnspan=5)
book_button = Button(
    win,
    text="Book",
    font=("Arial bold", 10),
    height=2,
    width=63,
    command=book,
    borderwidth=5,
)
book_button.grid(pady=10, columnspan=5)


def check_out():
    global rev_lbl
    global txt
    global contact_number_lbl, contact_number_en, done_button
    contact_number_lbl = Label(win, text="Contact No. :-", font=("Arial bold", 10))
    contact_number_lbl.grid(row=8, column=0, pady=10)
    contact_number_en = Entry(win, width=11, borderwidth=5)
    contact_number_en.grid(row=8, column=1, pady=10)

    rev_lbl = Label(win, text="Review", font=("Copperplate Gothic bold", 15))
    rev_lbl.grid(row=9, columnspan=5)
    txt = Text(win, height=5, width=55, borderwidth=5, font=("Constantia", 13))
    txt.grid(row=10, columnspan=5)

    def done():
        global back_button, done_button_1
        back_button = Button(
            win,
            text="Exit Review",
            font=("Arial bold", 10),
            width=11,
            borderwidth=5,
            command=ex,
        )
        back_button.grid(row=11, column=1, columnspan=5, pady=10)
        done_button.destroy()
        done_button_1 = Button(
            win,
            text=" Done >>",
            font=("Arial bold", 10),
            width=8,
            borderwidth=5,
            command=done,
            state="disable",
        )
        done_button_1.grid(row=11, column=0, columnspan=3, pady=10)
        # try
        global lbl_confirm, lbl_room_no_confirm
        ss = "SELECT Room_no , Bed_size FROM booking WHERE Contact_no = " + str(
            contact_number_en.get()
        )
        cur.execute(ss)
        a = cur.fetchone()
        if a[1] == 1:
            qry = "UPDATE Rooms SET Available_one_bed = %s WHERE one_bed = %s"
            value_update = ("Available", a[0])
            cur.execute(qry, value_update)
            db.commit()
        elif a[1] == 2:
            qry = "UPDATE Rooms SET Available_two_bed = %s WHERE two_beds = %s"
            value_update = ("Available", a[0])
            cur.execute(qry, value_update)
            db.commit()
        elif a[1] == 3:
            qry = "UPDATE Rooms SET Available_three_bed = %s WHERE three_beds = %s"
            value_update = ("Available", a[0])
            cur.execute(qry, value_update)
            db.commit()
        lbl_room_no_confirm = Label(
            win,
            text="Room No :-" + str(a[0]) + "\nChecked Out ",
            font=("Arial bold", 12),
            fg="blue",
        )
        lbl_room_no_confirm.grid(row=8, column=1, columnspan=4, padx=10)
        lbl_confirm = Label(
            win, text="Database Updated\nSuccessfully !", font=("bold", 12), fg="green"
        )
        lbl_confirm.grid(row=8, column=4, columnspan=5)

        comnd = "UPDATE booking SET check_out_time = %s WHERE Contact_no = %s"
        comnd_2 = "UPDATE booking SET Check_out_Date  =  %s WHERE Contact_no = %s"
        vals = (datetime.now().strftime("%H:%M"), contact_number_en.get())
        cur.execute(comnd, vals)
        db.commit()
        values = (date.today(), contact_number_en.get())
        cur.execute(comnd_2, values)
        db.commit()
#Getting Review
        Review = txt.get("1.0","end")
        txt_file = open("Review.txt" , "a")
        txt_file.write(Review+"\n")
        txt_file.close()

    done_button = Button(
        win,
        text=" Done >>",
        font=("Arial bold", 10),
        width=8,
        borderwidth=5,
        command=done,
    )
    done_button.grid(row=11, column=1, columnspan=3, pady=10)


check_out_button = Button(
    win,
    text="Check out",
    height=5,
    font=("Arial bold", 10 - 2),
    width=15,
    command=check_out,
    borderwidth=5,
)
check_out_button.grid(row=3, column=4, pady=5, padx=3)


def ex():
    rev_lbl.destroy()
    txt.destroy()
    contact_number_en.destroy()
    contact_number_lbl.destroy()
    back_button.destroy()
    done_button_1.destroy()
    lbl_room_no_confirm.destroy()
    lbl_confirm.destroy()


win.mainloop()
