import matplotlib.pyplot as plt
import numpy as np


x = []
y=[]

x,y = np.loadtxt('csv_import_example.txt', delimiter=',', unpack = True)

plt.plot(x,y,label='Loaded from File')
plt.xlabel('Plot Number')
plt.ylabel('Randomly Chosen Tutorial #')
plt.legend()
plt.title('Awesome Graph')
plt.show()
