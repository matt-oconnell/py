#!/usr/bin/env python

"""Matt O'Connell -- HW 2.1: Email Program"""

import sys
import select

sendmail_prog = '/usr/sbin/sendmail'

required_args = {'to', 'from'}
valid_args = {'to', 'from', 'cc', 'bcc', 'subject'}

args = sys.argv[1:]
arg_dict = {}
arg_set = {}
message_file = sys.stdin

def usage(error_message):
    print """{}

Usage:
    homework_2.1.py to=reciever@example.com from=sender@example.com < message.txt

    required arguments:
        to, from

    optional arguments:
        cc, bcc, subject

    stdin (message):
        required
    """.format(error_message)
    exit(1)

try:
    arg_dict = dict([(arg.split('=')[0], arg.split('=')[1]) for arg in args])
    arg_set = { arg.split('=')[0] for arg in args }
except Exception as ex:
    if type(ex) is IndexError:
        usage('Please format your inputs as name=value')
        exit(1)

# If our args are NOT a subset of valid args
if not arg_set <= valid_args:
    usage('Invalid argument(s) found: {}'.format(', '.join(arg_set - valid_args)))

# If our all required args are NOT a subset of our args
if not required_args <= arg_set:
    usage('Missing required field(s): {}'.format(', '.join(required_args - arg_set)))

# Could not find a nicer way to check for stdin
if not select.select([sys.stdin,],[],[],0.0)[0]:
    usage('No message detected')

print """
From: {}
To: {}
Subject: {}
Cc: {}
""".format(arg_dict.get('from'), arg_dict.get('to'), arg_dict.get('subject'), arg_dict.get('cc'))

print message_file.read()