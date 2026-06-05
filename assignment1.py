#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Satnam Singh"
Semester: "Fall/Winter/Summer YYYY"

The python code in this file (assignment1.py) is original work written by
"Satnam Singh". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys


def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def mon_max(month: int, year: int) -> int:
    if month == 2:
        if leap_year(year):
            return 29
        return 28

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    return 30


def after(date: str) -> str:
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month

    return f"{year}-{to_month:02}-{to_day:02}"


def usage():
    pass


def valid_date(date: str) -> bool:
    pass


def day_count(start_date: str, stop_date: str) -> int:
    pass


if __name__ == "__main__":
    pass
