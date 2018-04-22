import pandas as pd
import sklearn.datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors, datasets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

titanic = pd.read_csv('train.csv')
titanic.drop('Name',axis=1,inplace=True)

X = titanic.loc[:,['Fare','Sex','Pclass']]

for i in range(len(X['Sex'])):
    if X.iloc[i,1] == 'male':
        X.iloc[i,1] = 0
    elif X.iloc[i,1] == 'female':
        X.iloc[i,1] = 1

X = X.values

y = titanic.loc[:,'Survived']
y = y.values

skl_fare = sklearn.datasets.base.Bunch(data=X, target=y)
skl_fare.target_names = np.array(['Died', 'Survived'])
skl_fare.feature_names = np.array(['Fare', 'Sex', 'Pclass'])

knn = KNeighborsClassifier(n_neighbors=25)

knn.fit(X, y)


n_neighbors = 15
# we only take the first two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = X[:,:2]
y = y

h = .02  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))

plt.show()