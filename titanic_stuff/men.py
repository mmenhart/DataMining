import pandas as pd
from sklearn import tree
import graphviz
import numpy as np


titanic = pd.read_csv('train.csv')
titanic.drop('Name',axis=1,inplace=True)

men_df = titanic.sort_values('Sex')
men_df = men_df.iloc[314:891]

y = men_df.loc[:,'Survived']
y = y.values

# X = men_df.loc[:,['Pclass','Age','SibSp','Parch','Fare','Embarked']]
X = men_df.loc[:,['Pclass','SibSp','Parch','Fare','Embarked']]

for i in range(len(X['Embarked'])):
    if X.iloc[i,4] == 'S':
        X.iloc[i,4] = 0
    elif X.iloc[i,4] == 'C':
        X.iloc[i,4] = 1
    elif X.iloc[i,4] == 'Q':
        X.iloc[i,4] = 2

X = X.values

tree_men = tree.DecisionTreeClassifier()
tree_men.fit(X, y)

dot_data = tree.export_graphviz(tree_men, out_file=None)
graph = graphviz.Source(dot_data)
# graph.render('Titanic_men')


