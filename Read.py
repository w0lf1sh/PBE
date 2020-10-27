#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid:
    # return uid in hexa str
    def read_uid(self):
        try:
            reader = SimpleMFRC522()
            id = reader.read_id()
            return hex(id).upper().strip("0X")
        finally:
            GPIO.cleanup()

rf = Rfid()
print(rf.read_uid())