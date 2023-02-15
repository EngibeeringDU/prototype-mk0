#requires Sergei Piskunov's hx711 library for micropython

from machine import Timer,Pin
import time
from hx711 import HX711

led = machine.Pin(25, machine.Pin.OUT)
pushButton = Pin(22, Pin.IN)

driver = HX711(d_out=5, pd_sck=4)
driver.channel = HX711.CHANNEL_A_64

#init global variables
tareAdjustment = 0
weightObjectInGrams = 580.5
weightObjectInSensorUnits = 0
ratio = 0

def waitForButtonPush(pushButton):
    while True:
        if pushButton.value() == True:
            break

def tare():
    led.value(1)
    i=0
    numReadings = 50
    sumEmpty = 0
    print("Entered tare process!")
    print("Press the button to begin tare process")
    waitForButtonPush(pushButton)
    print("Taring with EMPTY LOAD PLATE...")
    

    while i < numReadings:
        reading = driver.read()
        sumEmpty += reading
#         print("Reading #: {} | Raw Data: {} | Reading Sum: {}".format(i, reading, sumEmpty))
        i += 1
    tareAdjustment = sumEmpty/numReadings
#     print("Empty Tare complete! Tare Adjustment is {}! Please LOAD the plate now, then PRESS the BUTTON".format(sumEmpty/numReadings))
    print("Empty Tare complete! Please LOAD the plate now, then PRESS the BUTTON")
    waitForButtonPush(pushButton)

    print("Taring with LOADED LOAD PLATE...")
    sumLoaded = 0
    i=0
    while i < numReadings:
        reading = driver.read()
        sumLoaded += reading
#         print("Reading #: {} | Raw Data: {} | Reading Sum: {}".format(i, reading, sumLoaded))
        i += 1
    weightObjectInSensorUnits = sumLoaded/numReadings
    ratio = weightObjectInGrams / (weightObjectInSensorUnits - tareAdjustment)
#     print("ratio: {} g/SensU".format(ratio))
#     print("Loaded Tare complete! Tare Adjustment is {}! Please UNLOAD the plate now, then PRESS the BUTTON to finih the Tare process".format(sumLoaded/numReadings))
    print("Loaded Tare complete! PRESS the BUTTON to finih the Tare process")
    waitForButtonPush(pushButton)
    time.sleep(0.5)
    led.value(0)
    return tareAdjustment, ratio;

def readAverage(numReadings, driver):
    sum = 0
    for i in range(0,numReadings):
        rawReading = driver.read()
        sum += rawReading
    return sum / numReadings


tareAdjustment, ratio = tare()

while True:
    reading = readAverage(10, driver)
    adjustedReading = reading - tareAdjustment
    weight = adjustedReading * ratio
#     print("Raw Reading Data: {} SensU | Adjusted Reading: {} SensU | Measured Weight: {} grams".format(reading, adjustedReading, weight))
    print("Measured Weight: {} grams".format(weight))
    if pushButton.value() == True:
        tareAdjustment, ratio = tare()
        