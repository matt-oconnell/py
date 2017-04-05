#!/usr/bin/env python

"""Matt O'Connell -- HW 3.1: Date Simple Module"""

import datetime as dt
from dateutil import parser
import time

# CONVERT STRINGS  TO DATETIME OBJECT
# Accepted formats:
#   2016-05-05
#   5/5/2016
#   5-May-16

def split_date_by(date_str, char):
    try:
        return [date_el for date_el in date_str.split(char)]
    except:
        print 'Error parsing arguments, please use correct formats'

def can_convert_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def parse_dashed_date(date_list):
    month = date_list[1]
    # If we can't convert to int, must be format with month as string
    if not can_convert_to_int(month):
        date_list[1] = time.strptime(month, "%b").tm_mon
        year = date_list[2]
        # We assume that < 18 for year means 20## else, 19##
        year = '20' + year if year < 18 else '19' + year
        # switch places in array to conform to expected return format
        date_list[0], date_list[2] = year, date_list[0]
    return date_list

def parse_date_str(date_str):
    if '-' in date_str:
        date_pieces = split_date_by(date_str, '-')
        date_pieces = parse_dashed_date(date_pieces)
    else:
        date_pieces = split_date_by(date_str, '/')
        year = date_pieces.pop()
        date_pieces.insert(0, year)
    return map(int, date_pieces)

def get_date(date_str = None):
    if not date_str:
        return dt.date.today()
    else:
        year, month, day = parse_date_str(date_str)
        print year, month, day
        return dt.date(year, month, day)

# ADVANCE TIME
def add_days(date, days):
    delta = dt.timedelta(days=days)
    return date + delta

def add_day(date, days = 1):
    return add_days(date, days)

def add_week(date, weeks = 1):
    days = 7 * weeks
    return add_days(date, days)


# PRINT FORMATTED DATE STRING
def format_date(date, format='YYYY-MM-DD'):


a = get_date('1987-10-20')
b = get_date('10/20/1987')
c = get_date('20-Oct-87')
d = get_date()


print add_day(a, -10)
print add_week(a, 10)