import matplotlib.pyplot as plt

test_scores = [55,88,67,76,99,13,66,45,88,88,99,98,95,90]

##x=[x for x in range(len(test_scores))]
###bar chart for comparison
##plt.bar(x, test_scores)
##
##plt.show()



bins=[10,20,30,40,50,60,70,80,90,100]
plt.hist(test_scores,bins,histtype='bar', rwidth=0.8)

plt.show()
