import sys, network, socket
sys.path.append('/lib/pico')
from lib.pico.controller import Controller

class NetworkInterface:
    
    def __init__(self, board, ssid, pw):
        self.board_ = board
        self.wlan_ = self.connect(ssid, pw)
        self.controller_ = Controller(self.board_)
    
    def connect(self, ssid, pw):
        try:
            self.wlan_
            if self.wlan_.isconnected():
                return self.wlan_
        except:
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            wlan.connect(ssid, pw)
            return wlan
    
    def disconnect(self):
        if self.wlan_.isconnected():
            self.wlan_.disconnect()
        return True
    
    def _get_network_info(self, ind : int):
        retval = '0.0.0.0'
        if self.wlan_.isconnected():
            retval = self.wlan_.ifconfig()[ind]
        return retval
        
    def get_ip(self):
        return self._get_network_info(0)
    
    def get_subnet(self):
        return self._get_network_info(1)
    
    def get_gateway(self):
        return self._get_network_info(2)
        
    def get_dns(self):
        return self._get_network_info(3)
            
    def test_connection(self):
        # Wait ten secconds to try to connect to the network
        for i in range(10):
            if self.wlan_.status() < 0 or self.wlan_.status() >=3:
                break
            ch = '.'
            print(f'Connecting{ch*i}')
            time.sleep(1)

        # test for failure to connect
        if self.wlan_.status() != 3:
            print(f'Connection to {self.ssid_} failed')
            return False
        else:
            print(f'Connected to {self.ssid_}\nIP = {self.get_ip()}')
            return True
        
    def open_socket(self, port):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.get_ip(), port))
        s.listen(1)
        print(f'Pico address: {self.get_ip()}')
        print(f'Socket opened on port: {port}')
        return s
    
    def listen(self, port = 80):    
        self.sock_ = self.open_socket(port=port)
    
        while True:
            print('Listening...')
            client, client_addr = self.sock_.accept()
            request = str(client.recv(1024))
            try:
                # TODO send the request to the controller who will parse
                self.controller_.handle(client, request)
            except:
                pass