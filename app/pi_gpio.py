import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PINLIST = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 21, 20]

class Pi_gpio(object):
    def __init__(self):
        self.relay16 = []

        for i in PINLIST:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
            self.relay16.append(False)

    def i_toggle(self, n):
        i = int(n) -1 
        if self.relay16[i]:
            # Turning i OFF
            GPIO.output(PINLIST[i], GPIO.HIGH)
            self.relay16[i] = False
        else:
            # Turning i ON
            GPIO.output(PINLIST[i], GPIO.LOW)
            self.relay16[i] = True

    def toggle_all(self, state):
        if state:
            # turn all ON
            for i in range(0, 16):
                GPIO.output(PINLIST[i], GPIO.LOW)
                self.relay16[i] = True
        else:
            # turn all OFF
            for i in range(0, 16):
                GPIO.output(PINLIST[i], GPIO.HIGH)
                self.relay16[i] = False

    def cleanup_pi(self):
        GPIO.cleanup()

if __name__ == "__main__":
    pass
