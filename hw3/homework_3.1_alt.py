#!/usr/bin/env python

"""Matt O'Connell -- HW 3.1: Date Simple Module"""

import datetime as dt
from dateutil import parser

# Error Handling
def is_datetime_type(date):
    if not isinstance(date, dt.datetime):
        raise TypeError('Please provide a valid datetime object')
    else:
        return True

def is_accepted_format(format):
    if not format in format_map:
        raise ValueError('Unacceptable format type')
    else:
        return True

def is_int(val):
    if not type(val) == int:
        raise TypeError('Not a valid integer')
    else:
        return True


# PARSE STRING AND RETURN DATETIME OBJECT
def parse_date_str(date_str):
    try:
        dt = parser.parse(date_str)
        return dt
    except:
        raise ValueError('Unacceptable format type')

def get_date(date_str = None):
    if not date_str:
        return dt.datetime.today()
    else:
        return parse_date_str(date_str)


# ADD DAYS
def add_days(date, days):
    delta = dt.timedelta(days=days)
    return date + delta

def add_day(date, days = 1):
    return add_days(date, days)

def add_week(date, weeks = 1):
    days = 7 * weeks
    if is_datetime_type(date) and is_int(weeks):
        return add_days(date, days)


# FORMATTED DATE STRING
format_map = {
    'YYYY-MM-DD': '%Y-%m-%d',
    'MM/DD/YYYY': '%m/%d/%Y',
    'DD-Mon-YY': '%d-%b-%y'
}

def format_date(date, format='YYYY-MM-DD'):
    if is_accepted_format(format) and is_datetime_type(date):
        return date.strftime(format_map[format])
