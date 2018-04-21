###############
# practice to make a sklearn database

import sklearn.datasets

skdb = sklearn.datasets.base.Bunch(data=X_train, target=y_train)
skdb.target_names = np.array(['Died', 'Survived'])
skdb.feature_names = np.array(['Pclass', 'Sex', 'Embarked'])

###############
# then to turn it into a graph (use jupyter notebook, it works better)

import graphviz

dot_data = tree.export_graphviz(atree, out_file=None,
                         feature_names=skdb.feature_names,
                         class_names=skdb.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
                         
                         
graph = graphviz.Source(dot_data)
graph.render('Titanic_tree')
