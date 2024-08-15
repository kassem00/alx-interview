#!/usr/bin/python3


import sys
import signal


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


def print_stats() -> None:
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
        line_count += 1
        parts = line.split()

        if len(parts) >= 7:
            ip = parts[0]
            status_code = parts[-2]
            file_size = parts[-1]

            # Validate status code and file size
            if status_code in status_codes:
                try:
                    total_file_size += int(file_size)
                    status_codes[status_code] += 1
                except ValueError:
                    pass

        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    pass


finally:
    print_stats()
