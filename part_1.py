

import pandas as pd
import numpy as np
import re
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split


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

#FOLLOWING CODE IS IMPRECISE AND NEEDS FIX

# Here we find different ways of saying the same thing
# Let's make them uniform.
# starting from the AI master
ai_regexs = [".*A.*I.*", "Artificial.*", "Ai", "^.*premaster", r"A.I."]
ai_replaced = odi_df.iloc[:,1].replace(to_replace=ai_regexs, value="A.I.", regex=True)
ai_replaced.value_counts().sort_index()

# computational science
cs_regexs = ["Com.*ience"]
cs_ai_replaced = ai_replaced.replace(to_replace=cs_regexs, value="C.S.", regex=True)
cs_ai_replaced.value_counts().sort_index()

# Bioinformatics
bi_regexs = ["\w*ioinformatics\w*"]
bi_cs_ai_replaced = cs_ai_replaced.replace(to_replace=bi_regexs, value="Bioinformatics",
regex=True)
bi_cs_ai_replaced.value_counts().sort_index()
