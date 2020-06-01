#!usr/bin/env python

"""hay que hacer andar el ads1115"""

import time

# import sensor de humedad
import Adafruit_DHT
 
# Import the ADS1x15 module.
import Adafruit_ADS1x15 

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115() #.ADS1015 para elegir el otro

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

#ahora voy a configurar el DHT
DHT_Sensor = Adafruit_DHT.DHT22 # le decimos q es un DHT22
DHT_PIN = 17 # este es el pin de GPIO (es el 11 de pero a estos muchachos les gusta mezclar los numeros)



print('Reading ADS1x15 values')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
sleepvalue = 2
# Main loop.
for veces in range(20):

    time.sleep(sleepvalue*2) #el DHT necesita tiempo para prepararse, se lo damos
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) #controlar DHT_PIN
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

# ------------------ terminado el DHT vamos a imprimir el ads ---------------------------
 
        
    # Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        #values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
    # Print the ADC values.
    print(str(veces)+'| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    # Pause for half a second.
    time.sleep(sleepvalue)
    veces += 1
