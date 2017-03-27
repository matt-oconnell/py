#!/usr/bin/env python

"""Matt O'Connell -- HW 2.2: File List"""

import argparse
import os
import datetime

parser = argparse.ArgumentParser(
    description='Script retrieves schedules from a given server')

parser.add_argument(
    '-d', '--dir', type=str, help='Directory name', default='.')

parser.add_argument(
    '-b', '--by', type=str, help='Sort by', required=False, default='size')

parser.add_argument(
    '-r', '--results', type=int, help='Number of results', required=False, default=4)

parser.add_argument(
    '--direction', type=str, help='Sort direction', required=False, default='descending')

args = parser.parse_args()

dir = args.dir
by = args.by
results = args.results
direction = args.direction
reverse = direction == 'ascending'

sort_types = { 'size', 'mtime', 'name' }
direction_types = { 'descending', 'ascending' }

if direction not in direction_types:
    print 'Direction type {} is invalid'.format(direction)
    exit(1)

if by not in sort_types:
    print 'Direction type {} is invalid'.format(by)
    exit(1)

try:
    dir_list = os.listdir(dir)
except:
    print 'Cannot read dir {}'.format(dir)

dirs_arr = []
files = os.listdir(dir)

# Create arr
for name in files:
    if len(dirs_arr) == results:
        break
    stat = os.stat(name)

    dirs_arr.append({
        'name': name,
        'size': stat.st_size,
        'modified': datetime.datetime.utcfromtimestamp(os.path.getmtime(name)).strftime('%Y-%m-%dT%H:%M:%SZ')
    })


sort_funcs = {
    'size': lambda file: file['size'],
    'mtime': lambda file: file['modified'],
    'name': lambda file: file['name']
}

for item in sorted(dirs_arr, key=sort_funcs[by], reverse=reverse):
    print '{}: {} bytes. Last modified {}'.format(item['name'], item['size'], item['modified'])

