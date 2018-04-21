###############
# turning data into an array for sci-kit learn models
# X = features (big X)
# y = response (little y)
# titanic_df is the name of the DataFrame for the titanic data

X = titanic_df.loc[:,['Pclass','Sex','Embarked']]
X = X.values
X = np.array(X,dtype='float')

y = titanic_df.loc[:,'Survived']
y = y.values

# this creates a test set from our training set
# change test_size parameter to choose size of test set (if 0.1, training = 0.9)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
