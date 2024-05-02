#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics.
"""
from sys import stdin
import random
from time import sleep

line_count = 0
file_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}

try:
    for line in stdin:
        line_count += 1

        file_size += int(line.split()[-1])
        status_code = int(line.split()[-2])

        if status_code in status_codes:
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print(f"File size: {file_size}")
            for code, count in sorted(status_codes.items()):
                print(f"{code}: {count}")
            print()

except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")
