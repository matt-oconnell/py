#!/usr/bin/env python

"""Matt O'Connell -- HW 4.1: Config"""

import csv
import json

class Config(object):
    def __init__(self, file_name, overwrite_keys=False):
        """
        :param file_name: String
        :param overwrite_keys: Boolean
            Allow existing keys to be overwritten

        Configures a format_parse_map made up of
            a "read" method that reads a file and converts its contents to a dict
            a "write" method that writes the local file_data to the file

        Sets file type, name, and overwrite_keys

        Sets file_data by calling the corresponding format_parse_map read method
         for a given file type
        """
        self.format_parse_map = {
            'txt': {
                'read': self._dict_from_key_val,
                'write': self._write_key_val,
            },
            'csv': {
                'read': self._dict_from_csv,
                'write': self._write_csv,
            },
            'json': {
                'read': self._dict_from_json,
                'write': self._write_json,
            }
        }
        self.file_type = file_name.split('.')[1]
        self.file_name = file_name
        self.overwrite_keys = overwrite_keys

        if self.file_type not in self.format_parse_map:
            raise ValueError('Invalid file type: {}'.format(format))

        try:
            self.file_data = self._read_file_to_dict()
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
        :param key: String
        :param value: Mixed
        :return: None
        """
        if not self.overwrite_keys and key in self.file_data:
            raise ValueError('Duplicate key detected: {}'.format(key))
            exit(1)
        self.file_data[key] = value
        self._write_to_file()

    def _write_to_file(self):
        """
        Write data to file using corresponding method for file type from format_parse_map
        """
        file = open(self.file_name, 'w')
        self.format_parse_map[self.file_type]['write'](file)
        file.close()

    def _read_file_to_dict(self):
        """
        Read file using corresponding method for file type from format_parse_map
        :return: Dict
            dict made up of data parsed from file
        """
        return self.format_parse_map[self.file_type]['read']()

    # Read txt file, convert to dict
    def _dict_from_key_val(self):
        file = open(self.file_name)
        lines = file.read().splitlines()
        file_dict = dict(line.split('=', 1) for line in lines)
        file.close()
        return file_dict

    # Write to file in key=value format
    def _write_key_val(self, file):
        for key, value in self.file_data.items():
            file.write('{}={}\n'.format(key, value))

    # Read csv file, convert to dict
    def _dict_from_csv(self):
        file = open(self.file_name, 'rb')
        with file as f:
            rows = csv.reader(f)
            keys, values = rows
            file_dict = dict(zip(keys, values))
        return file_dict
        file.close()

    # Write to file csv format
    def _write_csv(self, file):
        print self.file_data
        keys = list(self.file_data.keys())
        values = list(self.file_data.values())
        print keys, values
        file.write('{}\n'.format(','.join(keys)))
        file.write('{}\n'.format(','.join(values)))

    # Read json file, convert to dict
    def _dict_from_json(self):
        with open(self.file_name, 'r') as json_data:
            file_data = json.load(json_data)
            return dict(file_data)

    # Write to file in json format
    def _write_json(self, file):
        json.dump(self.file_data, file)
