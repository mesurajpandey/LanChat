import socket
import sys

HOST = ""
PORT = 8882
try:
    sck = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print 'Failed to create socket. Error code:' +str(msg[0])+ ', Error message: ' + msg[1]
    sys.exit()
print 'Server socket created'
    
try:
    sck.bind((HOST,PORT))
except socket.error,msg:
    print 'Bind Failed. Error code: ' + str(msg[0]) + ' message: ' + msg[1]
    sys.exit()

print 'Socket Bind Complete'
sck.listen(10)
print 'Socket now listening'
while 1:
    conn,addr = sck.accept()
    print 'Connected with ' + addr[0] + ' : ' + str(addr[1])
    data = conn.recv(1024)
    if data:
        print data
        # TODO:has to display in the chat Box
