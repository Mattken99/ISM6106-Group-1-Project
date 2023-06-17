import random
from time import *
from machine import *
from Button import *
from Displays import *
from Model import *

class OccupiSense:
    def __init__(self):
        # JYY: Used hardware
        self._display = LCDDisplay(sda=20, scl=21, i2cid=0)
        self._button1 = Button(17, "slideswitch", buttonhandler=None)
        self._slideswitch = Pin(17, Pin.IN) # This needs to be connected to button1 for the slideswitch to work

        # JYY: Programmed the slideswitch and model
        self._model = Model(2, self, debug=True)
        self._model.addButton(self._button1)

        #JYY: Declared transitions
        self._model.addTransition(0, BTN1_PRESS, 1)
        self._model.addTransition(1, BTN1_RELEASE, 0)


    def run(self):
        #JYY: Logical statement to match up slideswitch with state
        self._model.start()
        while self._model._running:
            curstate = self._model._curState
            if curstate == 0:
                self._slideswitch.value() == 0
            elif curstate == 1:
                self._slideswitch.value() == 1
            time.sleep(0.2)


    def stateDo(self, state):
        # JYY: Not used in OccupiSense
        if state == 0:
            pass
        elif state == 1:
            pass


    def stateEntered(self, state):
        # JYY: This code reflects what appears in the State Diagram. Slideswitch was hypersensitive in the simulator.
        if state == 0:
            print('State 0 entered')
            self._display.reset()
            self._display.showText(str("Available"),0,0)
            pass
        elif state == 1:
            print('State 1 entered')
            self._display.reset()
            self._display.showText(str("Occupied"),0,0)
            pass


    def stateLeft(self, state):
        # JYY: In console log, I printed when my transitions exit to the next state.
        if state == 0:
            print('State 0 exit')
            pass
        elif state == 1:
            print('State 1 exit')
            pass


# JYY: This calls the model.
if __name__ == '__main__':
    OccupiSense().run()
