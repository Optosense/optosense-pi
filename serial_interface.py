#!/usr/bin/env python3
import serial
import sys
import time

SLEEP_TIME = .2 

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

    if len(sys.argv) != 3:
        print(f"Wrong number of arguments : {len(sys.argv) - 1} found but only 2 were needed")
        sys.exit(1) 

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue

        if arg == "push" and i == 1:
            time.sleep(SLEEP_TIME)
            ser.write("PUSH".encode("ascii"))
            continue

        if arg == "pull" and i == 1:
            ser.write("PULL".encode("ascii"))
            time.sleep(SLEEP_TIME)
            continue

        if arg[:5] == "--ml=" and i == 2:
            ser.write(f"{int(arg[5:])}".encode("ascii"))
            continue

        print("first argument must be push or pull")
        print("second argument should be --ml=[quantity]")