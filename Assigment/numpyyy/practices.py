import numpy as np
import pandas as pd
import os

my_list = [1,2,3,4,5]
x = np.array(my_list)

#print(x.shape)


n = np.arange(0,31,2)

n = n.reshape(2,8)
#print(n)

series_obj = pd.Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'] )
#print(series_obj[5])

#np.random.seed(25)
DF_obj = pd.DataFrame(np.random.rand(36).reshape((6,6)), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
columns=['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6'])
#print(DF_obj)


DF_obj2 = pd.DataFrame(np.random.rand(16).reshape((4,4)), index=['row 1', 'row 2', 'row 3', 'row 4'], columns=['Column 1', 'Column 2', 'Column 3', 'Column 4'])
#print(DF_obj2)

#print(DF_obj2)

#print(DF_obj2.duplicated())


DF_obj3 = pd.DataFrame(np.arange(36).reshape(6,6))
#print(DF_obj3)

DF_obj4 = pd.DataFrame(np.arange(36).reshape(6,6))

print(DF_obj4)
print(DF_obj4[2:3, 2:4])


