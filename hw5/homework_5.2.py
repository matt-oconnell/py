#!/usr/bin/env python

"""Matt O'Connell -- HW 5.2: AttrType"""

import json

private_keys = ['_writeonce', '_type']

class AttrType(object):
    def __init__(self, type, writeonce=False):
        self._writeonce = writeonce
        self._type = type

    def __setattr__(self, key, value):
        if key in private_keys:
            object.__setattr__(self, key, value)
            return
        if self._writeonce:
            if hasattr(self, key):
                raise ValueError('Can\'t set attribute "{}" more than once'.format(key))
        if not isinstance(value, self._type):
            raise ValueError('{} is not of required type {}'.format(value, self._type.__name__))
        object.__setattr__(self, key, value)

    def as_list(self):
        all_keys = list(self.__dict__.keys())
        return [key for key in all_keys if not key in private_keys]

    def as_dict(self):
        filtered_list = self.as_list()
        return { key: self.__dict__[key] for key in filtered_list }
