import socket
class network:    
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports


    def _createSocket(self):
        self.netSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def checkPorts(self):
        netSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('[+] Checking ',self.host)
        closedPorts = []
        openPorts = []
        for port in self.ports:
            try:
                rtrn = netSocket.connect_ex((self.host, port))
                if(rtrn == 0):
                    print('[+] Open Port ', port)
                    openPorts.append(port)
                    netSocket.close()
                else:
                    closedPorts.append(port)
            except Exception as e:
                print('[-] ',e)
        print('[-] Ports closed', str(len(closedPorts)))
        return openPorts

    def getBanner(self, openPorts):
        netSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('[+] Banner Check...')
        for port in openPorts:
            try:
                rtrn = netSocket.connect((self.host, port))
                if(rtrn == 0):
                    print('[+] Open Port ', port)
                    rec = self.netSocket.recvfrom(1024)
                    netSocket.close()
                    print(rec)
                else:
                    print('[-] Faied to get Banner')
            except Exception as e:
                print('[-] ',e)
        

        
        
from nSock import network
