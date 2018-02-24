import math
import numpy as np
from scipy import stats

test_ex = [5, 9, 12, 2, 4, 18, 11]

print("Mean: ", np.mean(test_ex))

print("Median: ", np.median(test_ex))

mode = stats.mode(test_ex)

print("Mode: The modal value is {} with a count of {}".format(mode.mode[0], mode.count[0]))

print("Variance: ", np.var(test_ex))

print("Standard Deviation: ", np.std(test_ex))

