from sense_hat import SenseHat

import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
print("collected DATA")

conn = sqlite3.connect('/home/pi/pi-sql/infoscreen.db')


c = conn.cursor()


for row in c.execute('SELECT * FROM roomdata'):
        print()


plt.axis([0, 10, 0, 1])

for row in c.execute('SELECT * FROM roomdata'):
    plt.scatter(row[0], row[1])
    plt.pause(0.05)



plt.show()