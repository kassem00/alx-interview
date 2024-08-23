#!/usr/bin/python3
import sys
import signal
import re


total_file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

log_pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\S+ \S+\] "GET /projects/260 '
    r'HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints the statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Handles the keyboard interruption."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            line_count += 1
            status_code = match.group(1)
            file_size = int(match.group(2))

            # Update total file size and status code count
            total_file_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

except Exception as e:
    pass

finally:
    print_stats()
