import sys
import os
import json
import collections

if len(sys.argv) < 3:
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]
if len(sys.argv) >= 4:
    step = sys.argv[3]
else:
    step = 'd'

months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

histogram = {}
with open(infile, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        timestamp = tweet["created_at"]
        if step == 'd':
          time = timestamp[-4:] + '-' + months[timestamp[4:-23]] + '-' + timestamp[8:-20]
        elif step == 'h':
          time = timestamp[-4:] + '-' + months[timestamp[4:-23]] + '-' + timestamp[8:-20] + ' ' + timestamp[11:-17]
        elif step == 'm':
          time = timestamp[-4:] + '-' + months[timestamp[4:-23]] + '-' + timestamp[8:-20] + ' ' + timestamp[11:-14]
        elif step == 's':
          time = timestamp[-4:] + '-' + months[timestamp[4:-23]] + '-' + timestamp[8:-20] + ' ' + timestamp[11:-11]

        histogram[time] = 1 + histogram.get(time, 0)

ohistogram = collections.OrderedDict(sorted(histogram.items()))

with open(outfile, 'w') as fw:
    for time, count in ohistogram.iteritems():
        fw.write(time + '\t' + str(count) + '\n')
