import logging
from pylgbst import get_connection_bleak
from pylgbst.hub import SmartHub, Hub
from pylgbst.messages import MsgHubAttachedIO

log = logging.getLogger("hub")

logging.basicConfig()
log = logging.getLogger("hub")
log.setLevel(logging.CRITICAL)

class MySmartHub(SmartHub):

    """
    Rozwinięcie klasy SmartHub z biblioteki pylgbst dostosowujące klasę 
    do współpracy z 4-portowym hubem Lego Technic.
    """

    PORT_C = 0x02
    PORT_D = 0x03

    def __init__(self, connection=None) -> None:
        self.port_C = None
        self.port_D = None
        super().__init__(connection=connection)
        

    def _handle_device_change(self, msg):
        super()._handle_device_change(msg)
        if isinstance(msg, MsgHubAttachedIO) and msg.event != MsgHubAttachedIO.EVENT_DETACHED:
            port = msg.port
            if port == self.PORT_C:
                self.port_C = self.peripherals[port]
            elif port == self.PORT_D:
                self.port_D = self.peripherals[port]


    def get_devices(self):
        print(self.peripherals)

class Hub:

    """
    Wrapper wokół funkcjonalności pylgbst, przygotowany zwiększenia 
    czytelności kodu podczas wykładu. Udostępnia jedynie niezbędne 
    API w postaci metody rotate.

    UWAGA: Zastosowano tu pewne oszustwo. Biblioteka pylgbst oraz 
    hub Lego Technic umożliwiają sterowanie pozycyjne (nie tylko 
    inkrementalne). Ta funkcjonalność została celowo sparaliżowana, 
    żeby wykład był ciekawszy. 
    """

    def __init__(self, address, active_ports=None) -> None:
        self.active_ports = active_ports
        print("Enable hub and press any key.")
        input()
        self.connection = get_connection_bleak(hub_mac=address)
        self.hub = MySmartHub(self.connection)
        self.__wait_for_devices()
        for port_letter in self.active_ports:
            port = getattr(self.hub, f'port_{port_letter}')
            port.set_dec_profile(1)

    def __wait_for_devices(self):
        for port_letter in self.active_ports:
            port = getattr(self.hub, f'port_{port_letter}')
            while(not port):
                pass
            print(f"Device {port_letter} found!")

    def rotate(self, angle, device_letter='C'):
        device = getattr(self.hub, f'port_{device_letter}')
        device.preset_encoder()
        device.angled(angle)

