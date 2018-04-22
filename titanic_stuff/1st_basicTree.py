###############
# this tree compares sex, class, and embarked to whether they survived

import sklearn.datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import graphviz


test_data = pd.read_csv('test.csv')

original_data = pd.read_csv('train.csv')

titanic_df = pd.read_csv('train.csv')
titanic_df.drop('Name',axis=1,inplace=True)
titanic_df.drop('Ticket',axis=1,inplace=True)
titanic_df.drop('Cabin',axis=1,inplace=True)

###############
# for sci-kit learn all columns of data need to be either int or float
# for Sex column: male = 0, female = 1
# for Embarked column: S = 0, C = 1, Q = 2, NA = 3
# check .replace() for easier implementation

for i in range(len(titanic_df.iloc[:,3])):
    if titanic_df.iloc[i,3] == 'male':
        titanic_df.iloc[i,3] = 0
    elif titanic_df.iloc[i,3] == 'female':
        titanic_df.iloc[i,3] = 1

pd.to_numeric(titanic_df.iloc[:,3])

for i in range(len(titanic_df.iloc[:,8])):
    if titanic_df.iloc[i,8] == 'S':
        titanic_df.iloc[i,8] = 0
    elif titanic_df.iloc[i,8] == 'C':
        titanic_df.iloc[i,8] = 1
    elif titanic_df.iloc[i,8] == 'Q':
        titanic_df.iloc[i,8] = 2
    else:
        titanic_df.iloc[i,8] = 3

pd.to_numeric(titanic_df.iloc[:,8])

###############
# turning data into an array for sci-kit learn models
# X = features
# y = response

X = titanic_df.loc[:,['Pclass','Sex','Embarked']]
X = X.values
X = np.array(X,dtype='float')
y = titanic_df.loc[:,'Survived']
y = y.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

atree = tree.DecisionTreeClassifier()
atree.fit(X_train, y_train)
prediction = atree.predict(X_test)

###############
# practice to make a sklearn database
skdb = sklearn.datasets.base.Bunch(data=X_train, target=y_train)
skdb.target_names = np.array(['Died', 'Survived'])
skdb.feature_names = np.array(['Pclass', 'Sex', 'Embarked'])

dot_data = tree.export_graphviz(atree, out_file=None,
                         feature_names=skdb.feature_names,
                         class_names=skdb.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('Titanic_tree')

###############
# checking validation set for accuracy

total = len(y_test)
correct = 0
for i in range(total):
    if prediction[i] == y_test[i]:
        correct += 1

ratio_correct = correct/total

###############
# make a nice visual of the tree

dot_data = tree.export_graphviz(atree, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('Titanic')

###############
# print results to text file for visual comparison

out_pred = open('my_prediction.txt', 'w')
out_ans = open('my_answer.txt', 'w')
out_pred.write(str(prediction))
out_ans.write(str(y_test))
out_pred.close()
out_ans.close()
