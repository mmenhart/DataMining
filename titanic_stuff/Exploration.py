import pandas as pd
from sklearn import tree
import graphviz
import numpy as np

titanic = pd.read_csv('train.csv')
titanic.drop('Name',axis=1,inplace=True)

###############
# Data dictionary
# survival 0 = no, 1 = yes
# pclass 1 = 1st, 2 = 2nd, 3 = 3rd
# embarked = port of embarkation; C = Cherbourg, Q = Queenstown, S = Southampton
# sibsp = # of siblings/ spouses aboard
# parch = # of parents/ children aboard
# some children travelled with nanny and so parch = 0

###############
# categorical data
# survived
# sex
# embarked
# pclass

###############
# numerical data:
# age
# fare
# discrete:
# sibsp
# parch

###############
# for women in 3rd class 72 survived, 72 died
# best predictors for splitting women in 3rd class who died from survived are Fare then age


###############
# assuming ID(0), survived(1), sex(4) and pclass(2) only important variables
# create new df with only these variables

# sex_class = pd.concat([titanic.iloc[:,0:3],titanic.iloc[:,4]], axis=1)

# this list shows that almost all women in upper class survived

# w_upper = [[sex_class.iloc[i,0],sex_class.iloc[i,1]]for i in range(len(sex_class)) if sex_class['Sex'][i] == 'female' and sex_class['Pclass'][i] == 1]


###############
# looking at ages

age_sorted = titanic.sort_values('Age')

###############
# looking at fares

fare_sorted = titanic['Fare'].sort_values()

