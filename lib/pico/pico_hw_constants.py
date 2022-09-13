from machine import Pin

LED = Pin('LED', Pin.OUT)
#RUN = Pin(30, Pin.IN)
#ENA_3V3 = Pin(37, Pin.IN)

#UART = [tuple(Pin( 1, Pin.OUT), Pin( 2, Pin.IN)),
#        tuple(Pin( 6, Pin.OUT), Pin( 7, Pin.IN)),
#        tuple(Pin(11, Pin.OUT), Pin(12, Pin.IN)),
#        tuple(Pin(16, Pin.OUT), Pin(17, Pin.IN)),
#        ]

# Tuple in the form of (SDA, SCL)
#I2C = [tuple(Pin( 1, Pin.OUT), Pin( 2, Pin.IN)),
#        ]
# Tuple in the form of (Rx, CSn, SCK, Tx)
#SPI = [tuple(Pin( 1, Pin.OUT), Pin( 2, Pin.IN))
#        ]