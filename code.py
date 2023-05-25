#importing libraries
from hx711 import HX711
import net_code
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
import adafruit_requests as requests
import adafruit_wiznet5k.adafruit_wiznet5k_wsgiserver as server
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket

driver = HX711(d_out='GP5', pd_sck='GP4')
driver.channel = HX711.CHANNEL_A_64

tareAdjustment = -61376
weightObjectInGrams = 1000
weightObjectInSensorUnits = -69742.5
ratio = weightObjectInGrams / (weightObjectInSensorUnits - tareAdjustment)

#setting up the network connection
# eth = net_code.net_conn()
# net_code.net_info(eth)

#saving the URL
# url = 'http://192.168.1.3/json-example:5000'

#making a post request
# net_code.net_send(eth, {"Date": "July 25, 2019"}, url)

max = 10
s = 0
while True:
    for i in range (0,max): #take average of 10 readings, no filtering
        s += driver.read()
    reading = s / max;
    
    adjustedReading = reading - tareAdjustment
    weight = adjustedReading * ratio;
#     print("Raw Reading Data: {} SensU | Adjusted Reading: {} SensU | Measured Weight: {} grams".format(reading, adjustedReading, weight))
    print("Measured Weight: {} grams".format(weight))
    s = 0
    
# while True:
#     reading = driver.read()
#     adjustedReading = reading - tareAdjustment
#     weight = adjustedReading * ratio;
# #     print("Raw Reading Data: {} SensU | Adjusted Reading: {} SensU | Measured Weight: {} grams".format(reading, adjustedReading, weight))
#     print("Measured Weight: {} grams".format(weight))
