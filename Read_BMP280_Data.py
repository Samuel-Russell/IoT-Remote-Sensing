# Temperature, pressure and altitude data using a adafruit BMP280sensor
   
import time
import board

# import digitalio # For use with SPI
import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level, currently 1023 in Berlin
bmp280.sea_level_pressure = 1023 

while True:
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(5) # The method sleep() suspends execution for the given number of seconds