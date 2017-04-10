#!/usr/bin/env python

"""Matt O'Connell -- HW 4.2: Date Simple Class"""

import datetime as dt
from dateutil import parser

format_map = {
    'YYYY-MM-DD': '%Y-%m-%d',
    'MM/DD/YYYY': '%m/%d/%Y',
    'DD-Mon-YY': '%d-%b-%y'
}

class DatetimeSimple(object):
    def __init__(self, date_str='today'):
        self.format = 'YYYY-MM-DD'

        if date_str == 'today':
            self.datetime = dt.datetime.today()
        else:
            try:
                self.datetime = parser.parse(date_str)
            except:
                raise ValueError('Cannot parse date string. Please reformat')

    def __add__(self, other):
        delta = dt.timedelta(days=other)
        str = self._datetime_to_string(self.datetime + delta)
        return DatetimeSimple(str)

    def __sub__(self, other):
        return self + - other

    def __repr__(self):
        return self._datetime_to_string(self.datetime)

    def set_format(self, format):
        if not format in format_map:
            raise ValueError('Invalid format type')
        self.format = format

    def _datetime_to_string(self, dt):
        return dt.strftime(format_map[self.format])
