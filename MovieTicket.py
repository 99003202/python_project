import re


from datetime import datetime
from datetime import date


import pandas as pd
pd.set_option("Display.max_columns", None)

df = pd.read_csv("movie.csv")
print("-----------------------------------------------")
print("\t\t\tWELCOME TO AJ CINEMAS")
print("-----------------------------------------------\n")
print("\t\tMovies \t \t\t\t\tShow Timings\n")
print("1.Screen 1-", df.Movies[0], "\t \t\t", df.Show_Time[0])
print("2.Screen 2-", df.Movies[1], "\t\t\t", df.Show_Time[1])
print("3.Screen 3-", df.Movies[2], "\t\t", df.Show_Time[2])


class ticket:
    def __init__(self):
        self.ticket_no = 1
        self.ticket_rate = 120

    def read_tno(self):
        self.ticket_no = int(input("Enter the number of tickets you need :"))
        self.ticket_rate = (120*(self.ticket_no))

    def t_show(self):
        print("No: of Tickets :", self.ticket_no)
        print("Total Price :", self.ticket_rate)


class movie:
    def __init__(self):
        self.m_pool = ("1. The Seven", "2. Death Race", "3.The Prestige ")
        self.m_screen = ("1.Screen 1", "2.Screen 2", "3.Screen 3 ")
        self.m_timing = ("1. 09:00 A.M.", "2. 03:00 P.M. ", "3. 09:00 P.M. ")

    def m_det(self):
        self.m_no = int(input("Enter the Preferred movie :"))
        if self.m_no == 1:
            self.screen_no = 1
            self.m_name = "The Seven"
            self.m_time = int(input("Enter the showtime :"))
        elif self.m_no == 2:
            self.screen_no = 2
            self.m_name = "Death Race"
            self.m_time = int(input("Enter the showtime :"))
        elif self.m_no == 3:
            self.screen_no = 3
            self.m_name = "The Prestige"
            self.m_time = int(input("Enter the showtime :"))
        else:
            print("Invalid Entry")

    def f_time(self):
        if self.m_time == 1:
            print("Show Time : 09.00 A.M")
        elif self.m_time == 2:
            print("Show Time : 03.00 P.M.")
        elif self.m_time == 3:
            print("Show Time : 09.00 P.M.")
        else:
            print("Invalid Entry")

    def m_show(self):
        print("Movie :", self.m_name)
        print("Screen :", self.screen_no)
        movie.f_time(self)


class Customer(ticket, movie):
    def __init__(self):
        self.cust_name = "Default"
        self.cust_no = "0000000000"

    def cust_det(self):
        regex = "91-\d{10}"
        self.cust_name = str(input("Enter Your Name :"))
        self.cust_no = str(input("Enter Your 10 digit Phone "
                                 "Number with country code(91-): "))
        if re.match(regex, self.cust_no):
            print("Valid.")
        ticket.read_tno(self)
        movie.m_det(self)

    def cust_tkt(self):
        print("***********************\n \t\tTICKET\n***********************")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        print(current_time, "\t", today)
        print("\nName :", self.cust_name)
        print("Phone Number :", self.cust_no)
        movie.m_show(self)
        ticket.t_show(self)

c1 = Customer()
c1.cust_det()
c1.cust_tkt()
