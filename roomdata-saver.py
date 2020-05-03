import sqlite3
from sense_hat import SenseHat
import time


conn = sqlite3.connect('/home/pi/pi-sql/infoscreen.db')

sense = SenseHat()
sense.clear()

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE roomdata (time real,temprature real, pressure real, humidity real)''')

conn.commit()

while True:
    time.sleep(10)
    data = [(time.time(), sense.get_temperature(), sense.get_pressure(), sense.get_humidity())]
    c.executemany('INSERT INTO roomdata VALUES (?,?,?,?)', data)
    print("INSERTED: ",data)
    conn.commit()
