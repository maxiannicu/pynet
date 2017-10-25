# PyNET

## Description
PyNET is a simple python utility which reads and writes data across network connections, using TCP or UDP protocol. It also has posibility to scan for open ports.

## Usage
```bash
$ python2.7 pynet.py --help
usage: pynet.py [-h] --mode {listen,connect,scan} --protocol {tcp,udp}
                [--host HOST] [--port PORT] [--send-message MESSAGE]
                [--repeat-interval REPEAT_INTERVAL]
                [--repeat-count REPEAT_COUNT] [--scan-from SCAN_FROM]
                [--scan-to SCAN_TO] [--file FILE]

PyNET is a simple python utility which reads and writes data across network
connections, using TCP or UDP protocol. It also has posibility to scan for
open ports.

optional arguments:
  -h, --help            show this help message and exit
  --mode {listen,connect,scan}
                        Selects the mode of instance
  --protocol {tcp,udp}  Specifies used protocol.
  --host HOST           Host. Defaults to 127.0.0.1
  --port PORT           Depending on mode. Port to connect or to listen.
  --send-message MESSAGE
                        Message to send
  --repeat-interval REPEAT_INTERVAL
                        Repeat interval
  --repeat-count REPEAT_COUNT
                        Repeat count
  --scan-from SCAN_FROM
                        Scan port from number
  --scan-to SCAN_TO     Scan port to number
  --file FILE           Send a file
```
