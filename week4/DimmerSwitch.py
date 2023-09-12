class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)

def main():
    d0 = DimmerSwitch()
    d1 = DimmerSwitch()
    d0.turnOn()
    #d0.show()
    for count in range(5):
        d0.raiseLevel()
    d0.show()
    d1.show()
main()