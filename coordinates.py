import sys
import os
import json

if len(sys.argv) < 3:
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, 'r') as f, open(outfile, 'w') as fw:
    fw.write('tweet-id\tlongitude\tlatitude\ttweet\n')
    for line in f:
        tweet = json.loads(line)

        if not tweet['coordinates'] is None and not tweet['coordinates']['coordinates'][0] is None:
            fw.write(str(tweet['id_str']) + '\t')
            fw.write(str(tweet['coordinates']['coordinates'][0]) + '\t')
            fw.write(str(tweet['coordinates']['coordinates'][1]) + '\t')
            fw.write(tweet['text'].encode('utf-8').replace('\n', '\\n') + '\n')
