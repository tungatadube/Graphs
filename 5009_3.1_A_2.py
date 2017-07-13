import matplotlib.pyplot as plt
import numpy as np

def A7(title):

    y = [8, 3, 7, 2]
    x = [2, 4, 6, 8]

    width = 1/1.5
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rext1 = ax.bar(x, y, width-1, color="blue", label='All people')
    plt.title(title, color='blue', fontsize=14)
    plt.grid(color="green", linewidth=0.15)
    #plt.legend(loc="upper left", frameon=True )
    ax.set_ylabel('Number of students x 1000', color='blue', fontsize=12)
    ax.set_xlabel('Eye colour',color='blue', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(('Blue', 'Green', 'Brown', 'Other', ), color='green')

    plt.show()

A7('Favourite colours for students in a class')