# Last tare adjustment measured: 97119.54
# Tare adjustment @ 64 Gain = 98049.28
# Tare adjustment @ 128 Gain: 290507.9

# Measured aluminum block @ 64 Gain = 104495.8
# Measured aluminum block @ 128 Gain = 309776.2

from hx711_gpio import HX711

driver = HX711(dout=5, pd_sck=4)
driver.channel = HX711.CHANNEL_A_64

tareAdjustment = 98049.28
weightObjectInGrams = 580.5
weightObjectInSensorUnits = 104495.8
ratio = weightObjectInGrams / (weightObjectInSensorUnits - tareAdjustment)

while True:
    reading = driver.read()
    adjustedReading = reading - tareAdjustment
    weight = adjustedReading * ratio;
    print("Raw Reading Data: {} SensU | Adjusted Reading: {} SensU | Measured Weight: {} grams".format(reading, adjustedReading, weight))

