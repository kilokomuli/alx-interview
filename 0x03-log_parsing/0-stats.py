#!/usr/bin/python3
"""Log parsing in python"""
import sys
import signal


total_file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_stats():
    """Prints the total file size and the count of each status code."""
    global total_file_size, status_counts
    print(f"Total file size: {total_file_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")
    print()


def process_line(line):
    """Process a line from a log file."""
    global total_file_size, status_counts, line_count
    line = line.strip()
    parts = line.split()
    if len(parts) != 7:
        return
    try:
        status_code = int(parts[5])
        file_size = int(parts[6])
        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
        line_count += 1
    except ValueError:
        return
    if line_count % 10 == 0:
        print_stats()


def signal_handler(sig, frame):
    """Signal handler function that is called when a signal is received."""
    print("\nProgram interrupted. Printing final statistics:")
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line)
except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing final statistics:")
    print_stats()
    sys.exit(0)