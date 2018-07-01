import re
import socket

def getAddress():
    address = input('Please enter a http address and a port (example: http://httpbin.org):\n')
    parseAddress(address)

def parseAddress(address):
    urlMatch = re.compile(r'^(([^:/?#]+):(?=//))?(//)?((([^:]+)(?::([^@]+)?)?@)?([^@/?#:]*)(?::(\d+)?)?)?([^?#]*)(\?([^#]*))?(#(.*))?')
    searchResult = urlMatch.match(address)

    host = searchResult.group(8)
    port = '80'
    path = ''
    file = ''
    portTest = searchResult.group(9)
    pathTest = searchResult.group(10)

    if portTest is not None:
        port = portTest.replace(':', '')

    if pathTest is not None:
        path = pathTest

    connectToServer(host, port, path, file)

def connectToServer(host, port, path, file):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    request = 'GET ' + path + file + ' HTTP/1.1\r\nHost: ' + host + '\r\nAccept: application/json\r\n\r\n'
    print(request)
    s.sendall(str.encode(request))
    print(s.recv(4096).decode())
    s.close()
    print('socket closed')
