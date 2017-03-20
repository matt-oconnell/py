#!/usr/bin/env python

"""Matt O'Connell -- HW 1.1: Weather Underground"""

import sys
import urllib2

id, year = sys.argv[1:3]

url = 'https://www.wunderground.com/history/airport/{0}/{1}/1/1/CustomHistory.html?dayend=31&monthend=12&yearend={1}&format=1'.format(id, year)
file = urllib2.urlopen(url).read().splitlines()

sum_averages = 0
average_arr = []
mean_index = 2

# Find Sum of Averages, Max, Min
for i in range(2, len(file)):
    line_arr = file[i].split(',')
    temp = int(line_arr[mean_index])
    average_arr.append(temp)
    sum_averages += temp

max_temp = max(average_arr)
min_temp = min(average_arr)
total_days = len(average_arr)
mean = sum_averages / float(total_days)

# Standard Deviation
squared_sum = 0
for average in average_arr:
    squared_sum += (mean - average) ** 2

variance = squared_sum / total_days
standard_dev = variance ** .5

print """
Avg: {}
Max: {}
Min: {}
Standard Deviation: {}
""".format(mean, max_temp, min_temp, standard_dev)
