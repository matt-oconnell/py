#!/usr/bin/env python

"""Matt O'Connell -- HW 4.1: Config"""

import os
import csv
import json

# Base Class
class ConfigFile(object):
    def __init__(self, filename, overwrite_keys):
        self.filename = filename
        self.overwrite_keys = overwrite_keys
        self.file_data = self.read()

    def get(self, key):
        try:
            return self.file_data[key]
        except:
            raise KeyError('Key "{}" could not be found in file data'.format(key))

    def set(self, key, value):
        if not self.overwrite_keys and key in self.file_data:
            raise ValueError('Duplicate key detected: {}'.format(key))

        try:
            value = str(value)
        except:
            raise ValueError('String or value that is convertible to a string required')

        self.file_data[key] = value

        file = open(self.filename, 'w')
        self.write(file)
        file.close()

    # to be overwritten
    def read(self):
        raise NotImplementedError('subclass must implement a "read" method')

    # to be overwritten
    def write(self, file):
        raise NotImplementedError('subclass must implement a "write" method')

# Child classes
class TextConfigFile(ConfigFile):
    def read(self):
        file = open(self.filename)
        lines = file.read().splitlines()
        file_dict = dict(line.split('=', 1) for line in lines)
        file.close()
        return file_dict

    def write(self, file):
        for key, value in self.file_data.items():
            file.write('{}={}\n'.format(key, value))


class CsvConfigFile(ConfigFile):
    def read(self):
        file = open(self.filename, 'rb')
        with file as f:
            rows = csv.reader(f)
            keys, values = rows
            file_dict = dict(zip(keys, values))
        file.close()
        return file_dict

    def write(self, file):
        for key, value in self.file_data.items():
            file.write('{}={}\n'.format(key, value))


class JsonConfigFile(ConfigFile):
    def read(self):
        with open(self.filename, 'r') as json_data:
            file_data = json.load(json_data)
            return dict(file_data)

    def write(self, file):
        json.dump(self.file_data, file)


class_map = {
   'txt': TextConfigFile,
   'csv': CsvConfigFile,
   'json': JsonConfigFile
}

# Factory function that returns an instance of a ConfigFile subclass
def config(filename, overwrite_keys=False):
    file_type = os.path.splitext(filename)[1].split('.')[1]
    if file_type not in class_map:
        raise ValueError('Invalid file type: {}'.format(format))

    return class_map[file_type](filename, overwrite_keys)
