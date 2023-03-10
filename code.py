from hx711 import HX711

driver = HX711(d_out='GP5', pd_sck='GP4')
driver.channel = HX711.CHANNEL_A_64

tareAdjustment = 97515.4
weightObjectInGrams = 580.5
weightObjectInSensorUnits = 104495.8
ratio = weightObjectInGrams / (weightObjectInSensorUnits - tareAdjustment)

while True:
    reading = driver.read()
    adjustedReading = reading - tareAdjustment
    weight = adjustedReading * ratio;
    print("Raw Reading Data: {} SensU | Adjusted Reading: {} SensU | Measured Weight: {} grams".format(reading, adjustedReading, weight))