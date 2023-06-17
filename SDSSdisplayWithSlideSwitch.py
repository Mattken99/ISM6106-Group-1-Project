from machine import Pin
from utime import sleep

pins = [
    Pin(2, Pin.OUT),  # A
    Pin(3, Pin.OUT),  # B
    Pin(6, Pin.OUT),  # C
    Pin(7, Pin.OUT),  # D
    Pin(8, Pin.OUT),  # E
    Pin(4, Pin.OUT),  # F
    Pin(5, Pin.OUT),  # G
    Pin(9, Pin.OUT)   # DP (not connected)
]

digits = [
    [0, 0, 0, 0, 0, 0, 1, 1], # 0
    [1, 0, 0, 1, 1, 1, 1, 1], # 1
    [0, 0, 1, 0, 0, 1, 0, 1], # 2 
    [0, 0, 0, 0, 1, 1, 0, 1], # 3
    [1, 0, 0, 1, 1, 0, 0, 1], # 4
    [0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 1, 0, 0, 0, 0, 0, 1], # 6
    [0, 0, 0, 1, 1, 1, 1, 1], # 7
    [0, 0, 0, 0, 0, 0, 0, 1], # 8
    [0, 0, 0, 1, 1, 0, 0, 1], # 9
]

class LavatoryLogger:
    def reset():
        """Turns off all segments on the 7-segment display."""
        for Pin in pins:
            Pin.value(1)
    reset()

    switch = Pin(17, Pin.IN)
    while True:
        if switch.value() == 1:
            # Ascending counter
            for i in range(len(digits)):
                if switch.value() == 0:
                    break
                for j in range(len(pins) - 1):
                    pins[j].value(digits[i][j])
                sleep(1)
        else:
            # Descending counter
            for i in range(len(digits) - 1, -1, -1):
                if switch.value() == 1:
                    break
                for j in range(len(pins)):
                    pins[j].value(digits[i][j])
                sleep(1)