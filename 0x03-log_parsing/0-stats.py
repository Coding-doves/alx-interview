#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import sys

available_status_code = [100, 301, 400, 401, 403, 404, 405, 500]
total_file_size = 0
number_of_lines = 0
map_status_code = {}


def log_parsing():
    print(f"File Size: {total_file_size}")

    for sta, key in sorted(map_status_code.items()):
        print(f"{sta}: {key}")


try:
    for line in sys.stdin:
        try:
            line = line.split()
            file_size = int(line[-1])
            total_file_size += file_size
            status_code = int(line[-2])

            if status_code in available_status_code:
                if status_code in map_status_code:
                    map_status_code[status_code] += 1
                else:
                    map_status_code[status_code] = 1

            number_of_lines += 1

            if number_of_lines % 10 == 0:
                log_parsing()
        except ValueError:
            pass
    if number_of_lines == 0 or number_of_lines % 10 != 0:
        log_parsing()
except KeyboardInterrupt:
    log_parsing()
