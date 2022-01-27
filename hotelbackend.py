import mysql.connector as msqc
import numpy as np

db = msqc.connect(
    host="localhost",
    username="root",
    password=" ",
    database="graphic_hotel",
)
cur = db.cursor(buffered=True)


class BOOK:
    def __init__(
        self,
        Name,
        Check_in_Date,
        check_in_time,
        Check_out_Date,
        check_out_time,
        No_of_Members,
        Contact_no,
        Bed_size,
        No_of_days,
        Amount,
    ):
        self.Name = Name
        self.Check_in_Date = Check_in_Date
        self.check_in_time = check_in_time
        self.Check_out_Date = Check_out_Date
        self.check_out_time = check_out_time
        self.No_of_Members = No_of_Members
        self.Contact_no = Contact_no
        self.Bed_size = Bed_size
        self.No_of_days = No_of_days
        self.Amount = Amount

    def one_bed(self):
        ss = 'SELECT one_bed ,Available_one_bed from rooms where Available_one_bed = "Available"'
        cur.execute(ss)
        available_room = cur.fetchone()[0]

        s = 'UPDATE rooms SET Available_one_bed = "N/A" WHERE one_bed = ' + str(
            available_room
        )
        cur.execute(s)
        # print(available_room)
        customer_detials = (
            self.Name,
            self.Check_in_Date,
            self.check_in_time,
            self.Check_out_Date,
            self.check_out_time,
            self.No_of_Members,
            self.Contact_no,
            self.Bed_size,
            self.No_of_days,
            available_room,
            self.Amount,
        )
        data_entry = "INSERT INTO booking VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s, %s ,%s)"
        cur.execute(data_entry, customer_detials)
        db.commit()

    def two_bed(self):
        ss = 'SELECT two_beds ,Available_two_bed from rooms where Available_two_bed = "Available"'
        cur.execute(ss)
        available_room = cur.fetchone()[0]

        s = 'UPDATE rooms SET Available_two_bed = "N/A" WHERE two_beds = ' + str(
            available_room
        )
        cur.execute(s)
        # print(available_room)
        customer_detials = (
            self.Name,
            self.Check_in_Date,
            self.check_in_time,
            self.Check_out_Date,
            self.check_out_time,
            self.No_of_Members,
            self.Contact_no,
            self.Bed_size,
            self.No_of_days,
            available_room,
            self.Amount+1500,
        )
        data_entry = "INSERT INTO booking VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s, %s ,%s)"
        cur.execute(data_entry, customer_detials)
        db.commit()

    def three_bed(self):
        ss = 'SELECT three_beds ,Available_three_bed from rooms where Available_three_bed = "Available"'
        cur.execute(ss)
        available_room = cur.fetchone()[0]

        s = 'UPDATE rooms SET Available_three_bed = "N/A" WHERE three_beds = ' + str(
            available_room
        )
        cur.execute(s)
        # print(available_room)
        customer_detials = (
            self.Name,
            self.Check_in_Date,
            self.check_in_time,
            self.Check_out_Date,
            self.check_out_time,
            self.No_of_Members,
            self.Contact_no,
            self.Bed_size,
            self.No_of_days,
            available_room,
            self.Amount+3000,
        )
        data_entry = "INSERT INTO booking VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s, %s ,%s)"
        cur.execute(data_entry, customer_detials)
        db.commit()
