#!/usr/bin/python3

"""
Log parsing script
Reads log lines from stdin, parses them and computes stats based on specified
format.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C), it prints the
following statistics:
- Total file size
- Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)

The script uses the PEP 8 style and is executable.
"""

import sys
import re


def print_statistics(total_size, status_codes):
    """
    Print statistics based on the total file size and the count of each status
code.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing counts of each status code.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parse a log line according to the specified format.

    Args:
        line (str): Log line to parse.

    Returns:
        tuple: Tuple containing IP address, date, status code, and file size.
    Returns (None, None, None, None) if the line does not match the format.
    """
    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+-\s+\[(.*?)\]\s+\"GET\s+/projects/260\s+HTTP/1\.1\"\s+(\d+)\s+(\d+)"
    match = re.match(pattern, line)
    if match:
        ip_address = match.group(1)
        date = match.group(2)
        status_code = match.group(3)
        file_size = int(match.group(4))
        return ip_address, date, status_code, file_size
    else:
        return None, None, None, None


def main():
    """
    Main function to read log lines from stdin, parse them, and compute
statistics.

    Returns:
        None
    """
    total_size = 0
    status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404,
     405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, _, status_code, file_size = parse_line(line)
            if ip_address is not None:
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
