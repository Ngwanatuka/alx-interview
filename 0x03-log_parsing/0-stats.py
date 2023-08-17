#!/usr/bin/python3
""" log parsing """

import sys

""" a dictionary to keep track of status codes """
status_codes_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}

""" store the total size of the file """
total_size = 0

""" lines we've processed so far """
line_count = 0

try:
    """ loop that reads each line from stdin """
    for line in sys.stdin:
        """ split the lines into separate words """
        line_list = line.split()

        """ check if the line is valid """
        if len(line_list) > 4:
            """ get the status code """
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            """ check if the status code is in the dictionary """
            if status_code in status_codes_dict:
                """ increment the status code count """
                status_codes_dict[status_code] += 1

            """ add the file size to the total size """
            total_size += file_size
            line_count += 1

        """ print the status code count every 10 lines """
        if line_count == 10:
            """ print the total file size """
            print('File size:', total_size)
            """ print the status code count """
            for key in sorted(status_codes_dict.keys()):
                if status_codes_dict[key] != 0:
                    print('{}: {}'.format(key, status_codes_dict[key]))
            """ reset the line count """
            line_count = 0

except KeyboardInterrupt:
    pass

finally:
    print('File size:', total_size)
    for key in sorted(status_codes_dict.keys()):
        if status_codes_dict[key] != 0:
            print('{}: {}'.format(key, status_codes_dict[key]))
