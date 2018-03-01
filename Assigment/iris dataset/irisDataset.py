import numpy as np
from numpy import genfromtxt
from sklearn import linear_model

file = genfromtxt("iris.data", delimiter=",", dtype="str")
#print(file)


dic = {}
count = 0
for val in file:
    if val[4] not in dic:
        dic[val[4]] = count
        count += 1

for val in file:
    val[4] = dic[val[4]]


trainingSet = file[:130]
testingSet = file[130:]

#print(trainingSet.shape)
#print(testingSet.shape)

trainingX = trainingSet[:,[0,1,2,3]]    ## features
trainingY = trainingSet[:,[4]]  ## target variable

testingX = testingSet[:,[0,1,2,3]]   ## features
testingX = testingX.astype(float)
testingY = testingSet[:,[4]] ## targey variable
testingY = testingY.astype(float)

lr = linear_model.LogisticRegression()
lr.fit(trainingX, trainingY)

print("Predicted value is" + str(lr.predict([testingX[19]])))
print("real value is" + str(testingY[19]))

lr.score(testingX,testingY)*100
