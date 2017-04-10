#!/usr/bin/env python

"""Matt O'Connell -- HW 4.1: Config"""

import os
import csv
import json

"""
This is one of 3 ConfigFile class utils
Each has a read and write method accepting the same params
Since we need to include the homework in a single file, I'm using static
methods, but these probably don't need to be classes.
I think a better way might be to separate these into 3 different modules
with read / write functions
"""
class TextConfigFile(object):
    @staticmethod
    def read(file_name):
        file = open(file_name)
        lines = file.read().splitlines()
        file_dict = dict(line.split('=', 1) for line in lines)
        file.close()
        return file_dict

    @staticmethod
    def write(file, file_data):
        for key, value in file_data.items():
            file.write('{}={}\n'.format(key, value))


class CsvConfigFile(object):
    @staticmethod
    def read(file_name):
        file = open(file_name, 'rb')
        with file as f:
            rows = csv.reader(f)
            keys, values = rows
            file_dict = dict(zip(keys, values))
        file.close()
        return file_dict

    @staticmethod
    def write(file, file_data):
        keys = list(file_data.keys())
        values = list(file_data.values())
        file.write('{}\n'.format(','.join(keys)))
        file.write('{}\n'.format(','.join(values)))


class JsonConfigFile(object):
    @staticmethod
    def read(file_name):
        with open(file_name, 'r') as json_data:
            file_data = json.load(json_data)
            return dict(file_data)

    @staticmethod
    def write(file, file_data):
        json.dump(file_data, file)

class Config(object):
    def __init__(self, file_name, overwrite_keys=False):
        """
        :param file_name: String
        :param overwrite_keys: Boolean
            Allow existing keys to be overwritten

        Configures a util_class_map made up of file util classes containing
            a "read" method that reads a file and converts its contents to a dict
            a "write" method that writes the local file_data to the file

        Sets file type, name, and overwrite_keys

        Sets file_data by calling the corresponding util_class_map read method
         for a given file type
        """
        self.util_class_map = {
            'txt': TextConfigFile,
            'csv': CsvConfigFile,
            'json': JsonConfigFile
        }

        # Get file extension without "."
        self.file_type = os.path.splitext(file_name)[1].split('.')[1]
        self.file_name = file_name
        self.overwrite_keys = overwrite_keys

        if self.file_type not in self.util_class_map:
            raise ValueError('Invalid file type: {}'.format(format))

        self.util = self.util_class_map[self.file_type]

        try:
            self.file_data = self.util.read(file_name)
        except IOError as err:
            raise IOError('Unable to read file {}: {}'.format(file_name, err))

    def get(self, key):
        """
        :param key: String
        :return: String
            Value from given string
        """
        try:
            return self.file_data[key]
        except:
            raise KeyError('Key "{}" could not be found in file data'.format(key))

    def set(self, key, value):
        """
        Set a key/value
        :param key: String
        :param value: Mixed
        :return: None
        """
        if not self.overwrite_keys and key in self.file_data:
            raise ValueError('Duplicate key detected: {}'.format(key))

        try:
            value = str(value)
        except:
            raise ValueError('String or value that is convertible to a string required')

        self.file_data[key] = value

        file = open(self.file_name, 'w')
        self.util.write(file, self.file_data)
        file.close()
