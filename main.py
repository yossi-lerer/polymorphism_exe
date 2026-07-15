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
# step 3 - Status Reports
class Device:
    def __init__(self, name, is_on):
        self.name = name
        self.is_on = is_on
    def status(self):
        if self.is_on == True:
            print(f"{self.name}: on")
        else:
            print(f"{self.name}: off")
            
class SmartTV(Device):
    def __init__(self, name, is_on, channel):
        super().__init__(name, is_on)
        self.channel = channel
    def status(self):
        if self.is_on == True:
            print(f"{self.name}: on, watching channel {self.channel}")
        else:
            print(f"{self.name}: off")
class SmartSpeaker(Device):
    def __init__(self, name, is_on, song):
        super().__init__(name, is_on)
        self.song = song
lg = SmartTV("LG", True, 8)
alexa =  SmartSpeaker("Alexa", True, "Bohemian Rhapsody")
lg.status()
alexa.status()
# step 4 - Mixed List Activation
class Device:
    def __init__(self, name):
        self.name = name
    def activate(self):
        print("hi hello from device")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"hi hello from smart tv {self.name}")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"hi hello from smart SmartLamp {self.name}")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"hi hello from smart SmartSpeaker {self.name}")

devices = [SmartTV("LG"), SmartLamp("Desk Lamp"), SmartSpeaker("Echo")]
for device in devices:
    device.activate()
# step 5 - Volume Control Override
class Device:
    def __init__(self, name):
        self.name = name
    def set_volume(self, level):
        print(f"Device {self.name} volume set to {level}.")

class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def set_volume(self, level):
        print(f"Speaker {self.name} is now at volume {level}/10. {'Loud!' if level > 7 else ''}")

class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def set_volume(self, level):
        print(f"TV {self.name} volume: {level}. {'Muted!' if level == 0 else ''}")
bose = SmartSpeaker("Bose") 
bose.set_volume(9)
bose.set_volume(3)
# step 6 - Uniform Command Execution
class Device:
    def __init__(self, name):
        self.name = name
    def run_command(self, cmd):
        print(f"Device {self.name} received command: {cmd}.")

class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"smart tv {self.name} received command: {cmd}.")
        
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"smart lamp {self.name} received command: {cmd}.")

class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"smart speaker {self.name} received command: {cmd}.")

class Smarthome(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"smart home {self.name} received command: {cmd}.")
smart_list = [SmartTV("LG"), SmartLamp("Desk Lamp"), SmartSpeaker("Echo"), Smarthome("home ped")]
for device in smart_list:
    device.run_command("say hi")
# step 7 - Smart Home Schedule
class Device:
    def __init__(self, name):
        self.name = name
    def run_schedule(self, hour):
        print(f"{self.name} is idle.")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        if 18 <= hour <= 23:
            print(f"{self.name}: turning on")
        else:
            print("off")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        if 12 <= hour <= 20:
            print(f"{self.name}: turning on")
        else:
            print("off")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        if 20 <= hour <= 23:
            print(f"{self.name}: turning on")
        else:
            print("off")
list_device = [SmartLamp("Bedroom Lamp"), SmartAC("Living Room AC"), SmartTV("Samsung TV")]
for device in list_device:
    device.run_schedule(15)
# step 8 - Energy Usage Override
class Device:
    def __init__(self, name):
        self.name = name
    def energy_usage(self):
        print("10 (watts)")

class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        print(f"{self.name} 150 (watts)")

class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        print(f"{self.name} 900 (watts)")

class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        print(f"{self.name} 8 (watts)")

class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        print(f"{self.name} 30 (watts)")
        
devices = [SmartTV("LG"), SmartAC("AC"), SmartLamp("LAMP"), SmartSpeaker("Speaker")]
for device in devices:
    device.energy_usage()