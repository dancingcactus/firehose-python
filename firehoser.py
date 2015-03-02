#!/usr/bin/env python

import sys
import json
import requests
from time import sleep
import argparse
import ConfigParser
import firehoser_requests

#Handle Command Line Parameters 
parser = argparse.ArgumentParser(description="Settings to control the feed")
#pull a config file if available
parser.add_argument("-c", "--config_file", help="the config file your want to use (optional)", type=str, required=False, default="sample.conf")
args, remaining_argv = parser.parse_known_args()

config = ConfigParser.ConfigParser()
defaults = {}
if args.config_file:
    config = ConfigParser.SafeConfigParser()
    config.read([args.config_file])
    defaults = dict(config.items("Firehose"))

parser.set_defaults(**defaults)
parser.add_argument("-n", "--number", help="The number of hits to return", required=False, type=int)
parser.add_argument("-s", "--seconds", help="The number of seconds between the each hit", type=float, required=False)
parser.add_argument("-a", "--access_token", help="The access token you will use for the requests", type=str, required=False)
parser.add_argument("-u", "--firehose_url", help="The URL of your firehose stream", type=str, required=False)

args = parser.parse_args()

#Parse Config File



#Assemble the request
if args.access_token is not None:
    access_token = args.access_token
else:
    sys.exit("Error: Please Provide an Access Token (-a or --access_token)")
    
if args.firehose_url is not None:
    url = args.firehose_url;
else:
    sys.exit("Error: Please provide a Firehose URL (-u or --firehose_url)")
    
bearer = "Bearer " + access_token
headers = {"Authorization": bearer,"accept-encoding":"gzip,deflate"}
r = firehoser_requests.get(url, stream=True, headers=headers)

#Read the Stream
if r.status_code == requests.codes.ok:
    count = 0
    for line in r.iter_lines():
        if line:
            print "\r\n"
            print(json.dumps(json.loads(line),indent=2))
            
            #Break the loop if there are is a -n argument
            if args.number is not None:
                count = count + 1
                if count >= args.number:
                    break
                    
                    
            #How long to wait between writes        
            if args.seconds is not None :
                sleep(args.seconds)
else:
    print "There was a problem with the Request"
    print "Returned Status Code: " + str(r.status_code)
