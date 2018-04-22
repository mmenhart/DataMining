import pandas as pd
from sklearn import tree
import numpy as np

###############
# for women in 3rd class 72 survived, 72 died
# best predictors for splitting women in 3rd class who died from survived are Fare then age

titanic = pd.read_csv('train.csv')
titanic.drop('Name',axis=1,inplace=True)

women_df = titanic.sort_values('Sex')
women_df = women_df.iloc[0:314]
women_3rd = women_df.sort_values('Pclass')
women_3rd = women_3rd.iloc[170:314]

y = women_3rd.loc[:,'Survived']
y = y.values

X = women_3rd.loc[:,['Age','SibSp','Parch','Fare','Embarked']]
for i in range(len(X['Embarked'])):
    if X.iloc[i,4] == 'S':
        X.iloc[i,4] = 0
    elif X.iloc[i,4] == 'C':
        X.iloc[i,4] = 1
    elif X.iloc[i,4] == 'Q':
        X.iloc[i,4] = 2

X.iloc[:,0] = X.iloc[:,0].fillna(0)

X = X.values

tree_f_3 = tree.DecisionTreeClassifier()
tree_f_3.fit(X, y)

dot_data = tree.export_graphviz(tree_f_3, out_file=None)
graph = graphviz.Source(dot_data)
# graph.render('Titanic_women_3c')
