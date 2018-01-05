import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[4,7,4,7,3]

y2=[5,3,2,6,2]

plt.plot(x,y, label='initial line')
plt.plot(x,y2,label='new line')
plt.xlabel('Plot Number')
plt.ylabel('Random Number')
plt.title('Epic Graph tutorial for data viz in python with MatplotLib.\n Tutorial showing labels and titles')

if len(x)==len(y):
    plt.legend()
    plt.show()
    

print('got here')
