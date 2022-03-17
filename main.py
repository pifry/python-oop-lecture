from hub_wrapper import Hub
from datetime import datetime, timezone, timedelta

class AbsoluteMotor:
    def __init__(self, hub, motor):
        self.position = 0
        self.hub = hub
        self.motor = motor

    def calibrate(self):
        input("Ustaw silnik w pozycji zerowej i naciśnij enter")
        self.position = 0

    def set_position(self, position):
        angle = position - self.position
        self.hub.rotate(angle, self.motor)
        self.position = position
        print(self.position)

class Clock:
    def __init__(self, delta=0):
        self.delta = delta

    def _get_time(self):
        return datetime.now(timezone(timedelta(hours=self.delta)))
    
    def __repr__(self):
        now = self._get_time()
        return f"Godzina {now.hour} minut {now.minute}"

class AnalogClock(AbsoluteMotor, Clock):
    def __init__(self, hub, motor, delta):
        Clock.__init__(self, delta)
        AbsoluteMotor.__init__(self, hub, motor)
    def update(self):
        now = self._get_time()
        pos = now.hour * 60 + now.minute
        self.set_position(pos*6)

if __name__ == "__main__":


    hub = Hub('90:84:2B:5A:B4:6B', active_ports=['C', 'A'])
    #hub.rotate(10000, 'C')


    x = AnalogClock(hub,'C', +1)
    x.calibrate()
    

    y = AnalogClock(hub,'A', -6)
    y.calibrate()



    while(True):
        x.update()
        
    y.update()