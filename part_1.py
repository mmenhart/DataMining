

import pandas as pd
import numpy as np
from re import match, search
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



###########################################################

# Here we find different ways of saying the same thing
# Let's make them uniform.
# starting from the AI master
   
def set_to_standard(series, regexs, std_value):
   
   changed_values = []
   indices = []
   std_series = series.copy()
   
   for index, value in std_series.iteritems():
      for regex in regexs:
         
         if index in indices: #prevents an entry to be counted twice
            continue
         m = match(regex, value) #find match for any of the reg. expressions
         
      if m is not None: # if there's a match
         changed_values.append(value)
         indices.append(index)

   print("The following " + str(len(changed_values)) + " values have been changed to: " + std_value)
   print("")
   print(changed_values)
   
   std_series[indices] = std_value
   
   return std_series

ai_regexs = [r"(Msc )?A(rtificial|.)?.?[Ii].*"] #WARNING premaster to remove

standard_1 = set_to_standard(odi_df.iloc[:,1], ai_regexs, 'AI')

bio_regexs = [r"[Bb]io"]   # Bioinformatics

standard_2 = set_to_standard(standard_1, bio_regexs, 'BI')

ba_regexs = ["B(usiness )?A(nalytics)?"]

standard_3 = set_to_standard(standard_2, ba_regexs, 'BA')

bi_regexs = [r"[Ee]ngineering"] #this is: Big Data Engineering

standard_4 = set_to_standard(standard_3, bi_regexs, 'BDE') #NOT WORKING

