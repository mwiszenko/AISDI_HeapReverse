import tkinter
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('reverseHeap-results.txt', delimiter=" ", unpack=True)

plt.plot(x, y, 'o', color='black')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='red')

plt.title('Heap reverse complexity')
plt.xlabel('Heap size')
plt.ylabel('Sorting time (microseconds)')
plt.savefig('results.png')
plt.show()
