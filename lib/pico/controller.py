import sys, ure
sys.path.append('/lib/html')
from common import homepage

class Controller():   
    def __init__(self, board):
        self.board_ = board
        self.commands = {
                '/pico/led/on?' : self.board_.led_on,
                '/pico/led/off?' : self.board_.led_off,
                '/pico/led/toggle?' : self.board_.blink,
        }
    
    def handle(self, client, request):
        cmd, args = self.parse_req(request)
        
        if cmd in self.commands.keys():
            resp = self.commands[cmd](args)     
        
        client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(homepage(cmd.split('/')[-1][:-1]))
        client.close()
    
    # TODO make this parse a request for html values
    def parse_req(self, request):
        cmd = ''
        args = []
        regex = ure.compile("^(b'GET\s)(\S*)")
        match = regex.match(request)
        cmd = match.group(2)
        return cmd, args