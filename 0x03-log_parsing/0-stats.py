#!/usr/bin/python3
"""Log parsing in python"""
from sys import stdin


def print_stats(file_size, status_codes):
    """Prints the tootal file size and the count of each
    sttaus code that has been encounterd"""
    print("File size: " + str(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(code + ": " + str(status_codes[code]))


line_num = 0
file_size = 0
status_code = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in stdin:
        line_num += 1
        split_line = line.split()

        if len(split_line) > 1:
            file_size += int(split_line[-1])

        if len(split_line) > 2 and split_line[-2].isnumeric():
            status_code = split_line[-2]
        else:
            status_code = 0

        if status_code in status_codes.keys():
            status_codes[status_code] += 1

        if line_num % 10 == 0:
            print_stats(file_size, status_codes)

    print_stats(file_size, status_codes)

except (KeyboardInterrupt):
    print_stats(file_size, status_codes)
    raise
