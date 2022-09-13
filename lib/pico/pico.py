import utime, sys
sys.path.append('/lib')
sys.path.append('/lib/pico')
from NetworkInterface import NetworkInterface
import pico_hw_constants as constants

class State:
    # return a dict of state and value
    def __init__(self):
        self.led = 0
    def get_state():
        pass

# this is for hardware control of the pico
class PicoBoard:
    def __init__(self):
        self.id_ = ''
        self.state_ = State()
        self.net_ = NetworkInterface(self)
        pass
    
    def listen(self, port=80):
        self.net_.listen(port)
        
    def deactivate(self, *args):
        self.net_.disconnect()
        pass
    
    def blink(self, *args):
        constants.LED.toggle()
        self.state_.led = not self.state_.led
        return 0
        
    def led_on(self, *args):
        constants.LED.value(1)
        self.state_.led = 1
        return 0
        
    def led_off(self, *args):
        constants.LED.value(0)
        return 0
    
board = PicoBoard()
board.blink()
utime.sleep_ms(250)
board.blink()
board.listen()
