import socket
import argparse
import time


def start(args):
    type = socket.SOCK_DGRAM if args.protocol == 'udp' else socket.SOCK_STREAM
    s = socket.socket(socket.AF_INET, type)

    if args.mode == 'connect':
        count = 0
        s.connect((args.host, args.port))
        data = args.message

        if args.file is not None:
            data = args.file.read()
        while count < args.repeat_count:
            s.send(data)
            count += 1
            time.sleep(args.repeat_interval)
    elif args.mode == 'scan':
        for port in range(args.scan_from, args.scan_to + 1):
            open = True
            try:
                s.connect((args.host, port))
                s.close()
            except:
                open = False

            if open:
                print "Port", port, "is open"
    else:
        s.bind((args.host, args.port))
        print "Listening on", s.getsockname()
        if args.protocol == 'tcp':
            conn, addr = s.accept()
            while 1:
                data = conn.recv(1024)
                if not data: break
                print data
            conn.close()
        else:
            while 1:
                data, addr = s.recvfrom(1024)
                if not data: break
                print data

    s.close()


def main():
    parser = argparse.ArgumentParser(description='PyNET is a simple python utility which reads and writes data across network connections, using TCP or UDP protocol. It also has posibility to scan for open ports.')
    parser.add_argument('--mode',
                        help='Selects the mode of instance',
                        dest='mode',
                        choices=['listen', 'connect', 'scan'],
                        required=True)
    parser.add_argument('--protocol',
                        help='Specifies used protocol.',
                        dest='protocol',
                        choices=['tcp', 'udp'],
                        required=True)
    parser.add_argument('--host',
                        dest='host',
                        default='127.0.0.1',
                        help='Host. Defaults to 127.0.0.1')
    parser.add_argument('--port',
                        dest='port',
                        type=int,
                        default=0,
                        help='Depending on mode. Port to connect or to listen.')
    parser.add_argument('--send-message',
                        help='Message to send',
                        dest='message',
                        default='Hello world!')
    parser.add_argument('--repeat-interval',
                        help='Repeat interval',
                        type=int,
                        dest='repeat_interval',
                        default=0)
    parser.add_argument('--repeat-count',
                        help='Repeat count',
                        dest='repeat_count',
                        type=int,
                        default=1)
    parser.add_argument('--scan-from',
                        help='Scan port from number',
                        dest='scan_from',
                        type=int,
                        default=0)
    parser.add_argument('--scan-to',
                        help='Scan port to number',
                        dest='scan_to',
                        type=int,
                        default=65535)
    parser.add_argument('--file',
                        help='Send a file',
                        dest='file',
                        type=argparse.FileType('r'))

    start(parser.parse_args())


if __name__ == "__main__":
    main()
