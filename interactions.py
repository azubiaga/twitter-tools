import sys
import os
import json

if len(sys.argv) < 3:
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, 'r') as f, open(outfile, 'w') as fw:
    for line in f:
        tweet = json.loads(line)
        username = str(tweet['user']['screen_name'])
        username2 = ''

        if 'retweeted_status' in tweet:
            username2 = str(tweet['retweeted_status']['user']['screen_name'])
        elif not tweet['in_reply_to_screen_name'] is None:
            username2 = tweet['in_reply_to_screen_name']
            
        if username2 != '':
            fw.write(username + '\t' + username2 + '\n')
