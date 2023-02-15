from hx711 import HX711

driver = HX711(d_out=5, pd_sck=4)

driver.channel = HX711.CHANNEL_A_64
i=0
s=0
numReadings = 300
while i < numReadings:
    reading = driver.read()
    s += reading
#     print("Reading #: {} | Raw Data: {} | Reading Sum: {}".format(i, reading, s))
    i += 1;
    
print("Tare Loop 64 Gain Completed! Tare Adjustment is {}".format(s/numReadings))

driver.channel = HX711.CHANNEL_A_128
i=0
while i < numReadings:
    reading = driver.read()
    s += reading
#     print("Reading #: {} | Raw Data: {} | Reading Sum: {}".format(i, reading, s))
    i += 1;
    
print("Tare Loop from 128 Gain Completed! Tare Adjustment is {}".format(s/numReadings))
