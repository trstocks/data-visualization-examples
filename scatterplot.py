import matplotlib.pyplot as plt

test_scores = [55,88,67,76,99,13,66,45,88,88,99,98,95,90]
time_spent =  [11,10,13,22,43,25,15,43,55,55,24,42,29,12]

plt.scatter(time_spent, test_scores)
plt.title('Test scores vs Time Spent')
plt.xlabel('time spent on test')
plt.ylabel('test scores')

plt.show()

x = [1,2,3,4,5]
y1 = [2,3,2,4,2]
y2 = [8,8,6,7,6]

plt.scatter(x,y1, marker='o', color='c')

plt.scatter(x,y2, marker='v', color='m')

plt.show()
