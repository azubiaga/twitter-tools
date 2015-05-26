import sys
import os
import json
import collections
import operator

if len(sys.argv) < 3:
    sys.exit()

infile = sys.argv[1]

users = {}
with open(infile, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        if "retweeted_status" in tweet:
            users[tweet['retweeted_status']['user']['screen_name']] = 1 + users.get(tweet['retweeted_status']['user']['screen_name'], 0)

ousers = collections.OrderedDict(sorted(users.items(), key=lambda x: x[1]))

for user, rts in ousers.iteritems():
    print '[' + user + '] retweeted ' + str(rts) + ' times'
