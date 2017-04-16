#!/usr/bin/env python

"""Matt O'Connell -- HW 5.1: PersistDict"""

import json

class PersistDict(dict):
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'r') as json_file:
            file_data = json.load(json_file)
            super(PersistDict, self).__init__(file_data)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self._write_file()

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self._write_file()

    def clear(self):
        dict.clear(self)
        self._write_file()

    def setdefault(self, key, default=None):
        dict.setdefault(self, key, default)
        self._write_file()

    def update(self, newdict):
        dict.update(self, newdict)
        self._write_file()

    def _write_file(self):
        with open(self.filename, 'w') as json_file:
            json.dump(self, json_file)
