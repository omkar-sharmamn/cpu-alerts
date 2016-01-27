#!/usr/bin/python

import os
import subprocess
import re

"""
Still under Construction
"""

def get_uptime():
    """
    Gets the uptime of the machine by running 
    Unix Command - 'uptime'.
    """

    args = ["uptime"]
    op, proc = '', ''
    try:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        op, err = proc.communicate()
    except OSError as e:
        print str(e)
        return 1

    if op is not None: return op
    else:
        return 1


def get_fifteen_min_load_avg(data):
    """
    Parse uptime for last fifteen minutes.
    Return the same.
    On failure return -1.
    """

    # RE - to - Parse the uptime output - data
    if re.search('load average:.*', data):
        st = re.search('load average:.*', data)
        if st.group():
            load_average = st.group()
            if re.search("\s\d*\.\d*,\s*\d*\.\d*,\s*\d*\.\d*", load_average):
                match = re.search("\s\d*\.\d*,\s*\d*\.\d*,\s*\d*\.\d*", load_average)
                all_load_average = match.group()

                fifteen_min = all_load_average.split()[2]
                print "fifteen_min : ", fifteen_min
                return fifteen_min
            else:
                return -1

