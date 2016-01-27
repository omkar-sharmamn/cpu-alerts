#!/usr.bin/python2.6

import ConfigParser
import sys

filename = "load_alert.conf"
parser = ConfigParser.SafeConfigParser()

parser.add_section('load_threshold')
parser.set('load_threshold', 'load_threshold', '50')


parser.add_section('email_ids')
parser.set('email_ids', 'user1', 'user1@yourdomain.com')
parser.set('email_ids', 'user2', 'user2@yourdomain.com')
parser.set('email_ids', 'user3', 'user3@yourdomain.com')
parser.set('email_ids', 'user4', 'user4@yourdomain.com')
parser.set('email_ids', 'user5', 'user5@yourdomain.com')

with open(filename, 'w') as fh:
    parser.write(fh)
