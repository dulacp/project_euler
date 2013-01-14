# import numpy as np

# a = np.arange(1,1000)
# a = a[(a%3 == 0) | (a%5 == 0)]

# print a[:10]
# print a.sum()

print sum(i for i in range(1,1000) if i%3==0 or i%5==0)
