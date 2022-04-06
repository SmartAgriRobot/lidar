import time
from lidar_lib import lidar
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(i):
	measures = lidar.getMeasures()
	x = []
	y = []

	for point in measures:
		if point.distance > 0:
			x.append(point.distance*np.sin(point.angle*3.1415/180))
			y.append(point.distance*np.cos(point.angle*3.1415/180))

	xmax = 0
	ymax = 0
			
	if len(x) > 0:
		xmax = max(x)
		
	if len(y) > 0:
		ymax = max(y)
		
	ax.clear()
	ax.set_xlim([-1*xmax, xmax])
	ax.set_ylim([-1*ymax, ymax])
	ax.scatter(0, 0, s=50, c='red')
	ax.scatter(x, y, s=1)

lidar = lidar("/dev/ttyUSB0")

if not lidar.open():
	print("Cannot open lidar")
	exit(1)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=2000)
plt.show()
lidar.close()