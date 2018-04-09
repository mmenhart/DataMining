

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# import csv dataset as pandas dataframe
odi_dataframe = pd.read_csv("data/ODI-2018.csv", sep=',')

#check header
print(odi_dataframe.head())

#copy to working dataframe
odi_df = odi_dataframe.copy()

#visualise header
print(odi_df.head())

#We an irrelevant first row with NaN values: let's remove it
odi_df = odi_df.iloc[1:]

#Now, let's print only the column headers
print(odi_df.columns)

#how does the timestamp look like? 
print(odi_df.iloc[:, 0])
#as it seems to be standardized (probably handled by the polling platform) we'll leave it that way

#next, let's handle the second header. Which is:
print(odi_df.columns[1])
# what is the frequency of such programs?
odi_df.iloc[:, 1].value_counts().sort_index()

#TO BE CONTINUED...