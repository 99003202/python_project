# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
global f
f = 0
# this name_movie function is used to see movie name


def m_name():
    global f
    f = f + 1
    print("Which Movie do you want to watch")
    print("1 : The Seven")
    print("2 : Karan Arjun")
    print("3 : Chemmeen")
    print("4 : Back")
    movie = int(input("Choose your movie : "))
    if movie == 4:
        theatre()
        m_screen_no()
        return 0
    if f == 1:
        m_screen_no()
# the screen_no function is used to select screen


def m_screen_no():
    print("Which Screen do you want to watch movie: ")
    print("1 : Screen 1")
    print("1 : Screen 2")
    print("3 : Screen 3")
    a = int(input("Choose your screen : "))
    ticket = int(input("Number of tickets  you want :"))
    m_timing(a)
# the timing function is used to select timing for the movie


def m_timing(a):
    time1 = {
        "1": "10.00 A.M.",
        "2": "01.10 P.M.",
        "3": "04:20 P.M.",
        "4": "07:30 P.M. "
        }
    time2 = {
        "1": "10.15 A.M.",
        "2": "01.25 P.M.",
        "3": "04:35 P.M.",
        "4": "07:45 P.M. "

        }
    time3 = {
        "1": "10.30 A.M.",
        "2": "01.40 P.M.",
        "3": "04:50 P.M.",
        "4": "07:30 P.M."
        }
    if a == 1:
        print("Choose your time: ")
        print(time1)
        t = input("Select your time :")
        x = time1[t]
        print("Booking Confirmed , Enjoy your movie at" + x)
    elif a == 2:
        print("choose your time :")
        print(time2)
        t = input("Select yout time :")
        x = time2[t]
        print("Booking Confirmed , Enjoy your movie at :" + x)
    elif a == 3:
        print("Choose your time :")
        print(time3)
        t = input("Select yout time :")
        x = time3[t]
        print("Booking Confirmed Enjoy your movie at" + x)

return 0


def movie(m_screen_no):
    if m_screen_no == 1:
        m_name()
    elif m_screen_no == 2:
        m_name()
    elif m_screen_no == 3:
        m_name()
    elif m_screen_no == 4:
        city()
    else:
        print("Invalid Entry")


def theatre():
    print("Which theatre do you want to see movie")
    print("1 : INOX")
    print("2 : IMAX")
    print("3 : PVR ")
    print("4 : Back")
    a = int(input("Choose your option :"))
    movie(a)
    return 0


def city():
    print("Hi welcome to movie ticket booking")
    print("Where you want to watch movie ?:")
    print("1 : Bangalore ")
    print("2 : Pune ")
    print("3 : Kochi ")
    place = int(input("Choose your option :"))
    if place == 1:
        theatre()
    elif place == 2:
        theatre()
    elif place == 3:
        theatre()
    else:
        print("Wrong Choice")
city()




