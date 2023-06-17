from time import sleep
from Button import *
from Model import *
from Lights import *
from Displays import *


class LavatoryLogger:
    def __init__(self):
        self._number = 0
        print("LavatoryLogger: constructor")
        
        self._button1 = Button(10, "BlueButton", buttonhandler=self)
        self._button2 = Button(11, "RedButton", buttonhandler=self)
        self._display = LCDDisplay(sda=20, scl=21, i2cid=0)
        
        self._model = Model(4, self, debug=True)  # Instantiate model with 3 states
        
        self._model.addButton(self._button1)
        self._model.addButton(self._button2)
        
        # Adding transitions
        
        self._model.addTransition(0, BTN1_PRESS, 1)
        self._model.addTransition(0, BTN2_PRESS, 2)
        self._model.addTransition(1, BTN1_PRESS, 0)
        self._model.addTransition(2, BTN2_PRESS, 0)
        
    def run(self):
        self._model.start()
        
        while self._model._running:
            curstate = self._model._curState
            
            if curstate == 1:
                self._number += 1
                self._display.reset()
                self._display.showText(f"Flush! db ID# {self._number} created")
                self._model.gotoState(0)
            elif curstate == 2:
                self._number += 1
                self._display.reset()
                self._display.showText(f"TP Replaced! db ID# {self._number} created")
                self._model.gotoState(0)
            
            sleep(0.2)
    
    def stateEntered(self, state):
        if state == 0:
            print('State 0 entered')
        
        elif state == 1:
            print('State 1 entered: Should start the counter')
        
        elif state == 2:
            print('State 2 entered: Should decrease the counter')
    
    def stateLeft(self, state):
        if state == 0:
            print('State 0 exit')
        
        elif state == 1:
            print('State 1 exit')
        
        elif state == 2:
            print('State 2 exit')


if __name__ == '__main__':
    LavatoryLogger().run()
