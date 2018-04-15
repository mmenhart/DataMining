

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
         
   changed_values = pd.Series((v for v in changed_values))

   print("The following " + str(len(changed_values)) + " values have been changed to: " + std_value)
   print("")
   
   print(changed_values.value_counts())
   
   std_series[indices] = std_value
   
   return std_series



ai_regexs = [r"(Msc)?.*A(rtificial)?.?( )?[Ii].*(?<!premaster)$"] #WARNING premaster to remove

standard_1 = set_to_standard(odi_df.iloc[:,1], ai_regexs, 'AI')
bio_regexs = [r".*[Bb]io"]   # Bioinformatics

standard_2 = set_to_standard(standard_1, bio_regexs, 'BI')
ba_regexs = [".*[Bb](usiness )?[Aa](nalytics)?"]

standard_3 = set_to_standard(standard_2, ba_regexs, 'BA')
bde_regexs = [r".*[Ee]ngineering"] #this is: Big Data Engineering

standard_4 = set_to_standard(standard_3, bde_regexs, 'BDE')
cls_regexs = [".*[cC]om(o)?p.*ational.*ience.*|[Cc][Ll][Ss]"]

standard_5 = set_to_standard(standard_4, cls_regexs, 'CLS') 
standard_5.value_counts()#.sort_index()

cs_regexs = [r".{0,4}(Computer Science.?|cs|CS)$"] # ^(?!.*(metrics))
standard_6 = set_to_standard(standard_5, cs_regexs, 'CS')

ec_regexs = ["^.*(EOR|[Ee]conom(e)?trics|OR|Economics).*$"]
standard_7 = set_to_standard(standard_6, ec_regexs, 'EC')

qrm_regexs = [".*([Qq]uantit.*g[ea]ment|QRM)$"]
standard_8 = set_to_standard(standard_7, qrm_regexs, 'QRM')

phd_regexs = ["^(PhD)"]
standard_9 = set_to_standard(standard_8, phd_regexs, 'PHD')

others_regexs = [r".*[^AI|BI|BA|BDE|CLS|CS|EC|QRM|PHD]$"]

standard_10 = set_to_standard(standard_9, others_regexs, 'others')

others_regexs_2 = [r"MS|MPA|CSL"]

standard_11 = set_to_standard(standard_10, others_regexs_2, 'others')

standard_11.value_counts()