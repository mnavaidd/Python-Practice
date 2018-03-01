import irisDataset as iset
import matplotlib.pyplot as plot

features = iset.file[:,[0,1,2,3]]
features = features.astype(float)

featuresAll = []

targets = iset.file[:,[4]]
targets = targets.astype(int)

for observation in features:
    featuresAll.append([observation[0] + observation[1] + observation[2] + observation[3]])

plot.scatter(featuresAll, targets, color='red', alpha=1)
plot.rcParams['figure.figsize'] = [10,8]
plot.title("Iris Dataset Plot")
plot.xlabel("Features")
plot.ylabel("Class")
plot.show()


