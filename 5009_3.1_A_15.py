import matplotlib.pyplot as plt
import numpy as np

y = [0, 1, 1]
x = [2, 4, 6]
y2 = [1, 2, 2]
x2 = [1.5, 3.5, 5.5]
y3 = [ 4, 3, 4 ]
x3 = [2.5, 4.5, 6.5]
width = 1/1.5
fig = plt.figure()
ax = fig.add_subplot(111)
rext1 = ax.bar(x, y, width-1, color="blue",label= 'Form 1')
rect2 = ax.bar(x2, y2, width-1, color="red",label='Form 2')
rect3 = ax.bar(x3, y3, width-1, color="green",label='Graduates')
plt.title( 'Time spent on the computer', color = 'blue', fontsize = 14)
plt.grid(color= "green", linewidth= 0.15)
plt.legend(loc='upper center', frameon='True')


ax.set_ylabel('Number of People', color = 'blue', fontsize = 12)
ax.set_xlabel('Part of the day',color = 'blue', fontsize = 12)
ax.set_xticks(x)
ax.set_xticklabels( ('Morning', 'Afternoon', 'Evening'), color = 'green' )

plt.show()