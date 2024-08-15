import signal
import sys

def signal_handler(sig, frame):
    print("Ctrl+C was pressed. Exiting gracefully...")
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

while True:
    data = input("Please enter the message:\n")
    if 'Exit' == data:
        break
    print(f'Processing Message from input() *****{data}*****')
    print("Done")
