import random
from time import *
from Button import *
from Lights import *
from Model import *
from Sensors import *

class DispensePi:
    def __init__(self):
        # JYY: Used hardware
        self._number = 0
        self._button1 = Button(26, "replenished", buttonhandler=self, lowActive=True)
        self._pir = PIRmotionSensor(28)
        self._sensorlight = Light(27, "green led sensor")
        self._replenishlight = Light(22, "red led replenish")
        
        # JYY: Programmed the button and model
        self._model = Model(4, self, debug=True)
        self._model.addButton(self._button1)
        
        #JYY: Declared transitions
        self._model.addTransition(0, BTN1_PRESS, 1)
        self._model.addTransition(1, BTN1_PRESS, 0)
        self._model.addTransition(2, BTN1_PRESS, 3)
        self._model.addTransition(3, BTN1_PRESS, 0)


    def run(self):
        #JYY: This initializes the model
        self._model.run()


    def stateDo(self, state):
        # JYY: This DispensePi code reflects what appears in the State Diagram
        if state == 0:
            print('State 0 entered: Off')
            self._sensorlight.off()                
            self._replenishlight.off()
            if self._pir.motionDetected():
                self._number += 1  # Increment the motion count
                if self._number >= 3:  # If the motion count is 3 or more
                    self._model.gotoState(2)  # Transition to state 2
                    self._number = self._number - 3 # This resets the internal count
                else:
                    self._model.gotoState(1)  # Transition to state 1
        elif state == 1:
            self._sensorlight.on()
            time.sleep(3)
            self._sensorlight.off()
            self._model.gotoState(0)
        elif state == 2:
            self._sensorlight.off()
            self._replenishlight.on()
        elif state == 3:
            self._replenishlight.off()
            self._model.gotoState(0)
        time.sleep(0.5)
        

    def stateEntered(self, state):
        if state == 0:
            print('State 0 entered: Off')
        elif state == 1:
            print('State 1 entered: Dispensing')
        elif state == 2:
            print('State 2 entered: Needs to be Replenished')
        elif state == 3:
            print('State 3 entered')


    def stateLeft(self, state):
        if state == 0:
            print('State 0 exited: Off')
        elif state == 1:
            print('State 1 exited: Dispensing')
        elif state == 2:
            print('State 2 exited: Needs to be Replenished')
        elif state == 3:
            print('State 3 exited: Return to State 0')


if __name__ == '__main__':
    DispensePi().run()
