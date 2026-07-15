# part 1
# step 1 - Device Activation
class Device:
    def __init__(self, name):
        self.name = name
    def activate(self):
        print(f"Device {self.name} is now on.")

class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name} is playing the home screen.")

class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"Speaker {self.name} is ready to play music.")
lg = SmartTV("LG")
google = SmartSpeaker("google")
lg.activate()
google.activate()
# step 2 - Deactivate with Override
class Device:
    def __init__(self, name):
        self.name = name
    def deactivate(self):
        print(f"Device {self.name} is now off.")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"Lamp {self.name} is dimming and turning off.")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"AC {self.name} is cooling down and switching off.")
bedroom_lamp = SmartLamp("Bedroom Lamp")
living_room_AC =  SmartAC("Living Room AC")
bedroom_lamp.deactivate()
living_room_AC.deactivate()