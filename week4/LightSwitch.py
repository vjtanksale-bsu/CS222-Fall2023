class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on 
        self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
        self.switchIsOn = False

def main():
    l0 = LightSwitch()
    print(l0.switchIsOn)
    l0.turnOn()
    print(l0.switchIsOn)
    l0.turnOff()
    print(l0.switchIsOn)

main()