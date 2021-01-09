# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:53:25 2021

@author: abdul
"""

from tkinter import Tk, Canvas
from datetime import date, datetime


def str_to_date(v):
    return datetime.strptime(str(v), '%d/%m/%Y').date()


def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            if line != '\n':
                line = line.rstrip('\n')
                current_event = line.split(',')
                event_date = str_to_date(current_event[1])
                current_event[1] = event_date
                list_events.append(current_event)
    return list_events


def days_between_dates(date1, date2):
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(400, 10, anchor='n', fill='orange', font='Courier 28 italic bold', text='My Countdown Calendar')
events = get_events()
today = date.today()
vertical_space = 100
events.sort(key=lambda x: x[1])
for event in events:
    event_name = event[0]
    event_date = event[1]
    days_until = days_between_dates(event_date, today)
    display = '-> It is {} days until {}'.format(days_until, event_name)
    if int(days_until) <= 7:
        text_col = 'red'
    else:
        text_col = 'orange'
    if int(days_until) <= 0:
        display = '-> This event {} has expired'.format(event_name)
    c.create_text(10, vertical_space, anchor='w', fill=text_col, font='Courier 15 bold italic', text=display)
    vertical_space += 25
root.mainloop()