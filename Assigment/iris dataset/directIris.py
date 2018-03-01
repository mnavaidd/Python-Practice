from sklearn.datasets import load_iris
import matplotlib.pyplot as plot
from numpy import genfromtxt

#file = genfromtxt("iris.data", delimiter=",", dtype="str")
iris = load_iris()
#type(iris)

#print(iris.data)
#print(type(iris.data))
#print(iris.data.shape)
#print(iris.target.shape)

x = iris.data
y = iris.target

print(x[:,[1]])
#print(y.shape)

get1 = x[:,[0]]
get2 = x[:,[1]]
get3 = x[:,[2]]
get4 = x[:,[3]]



plot.scatter(get1, get2, get3, get4)
plot.rcParams['figure.figsize'] = [10,10]
plot.xlabel("x Label")
plot.ylabel("y Label")
plot.show()
