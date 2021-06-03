import numpy as np

a = np.arange(100).reshape(5,10,2)
a.tofile("b.dat",sep = ",",format = '%d')