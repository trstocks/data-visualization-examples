import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[4,7,4,7,3]

x2=[4,3,6,2,7]
y2=[5,3,2,6,2]

plt.bar(x,y,label="one", color='m')
plt.bar(x2,y2, label="two", color='g')

plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Bar Chart Tutorial')

plt.legend()

plt.show()
