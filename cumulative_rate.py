import numpy as np
import matplotlib.pyplot as plt

a = [[1, 2 ,3 ],[4,5 ,6]]
print(a)

print(np.cumsum(a))

print(np.cumsum(a , axis=0))

print(np.cumsum(a , axis=1))

# know we want to plot our rate

# assum our scores have been stored in b, step by step
b = np.random.randint(100, size=100)
plt.figure()
plt.subplot(311)
plt.title('Scores')
plt.plot(b, 'b--')


# we want to know the total sum of data as it grows with each step
cumB = np.cumsum(b)
plt.subplot(312)
plt.title('cumulative sum of scores')
plt.plot(cumB, 'r--')



# c is a vector : [1, 2, 3, 4, 5, 6, 7 , ..., 100]
c = np.arange(100)


# cumilative cumu
rate = cumB / c
plt.subplot(313)
plt.title('cumulative rate')
plt.plot(rate, 'g--')

plt.subplots_adjust(hspace=1)
plt.show()

