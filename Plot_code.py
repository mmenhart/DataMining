import matplotlib.pyplot as plt
import pandas as pd

###############
# use the for loop for a DataFrame
# the for loop with plot each column within a DataFrame seperately
# replace df with the name of your DataFrame
# the 'kind' in the code defines the chart type some options are 'bar' 'pie' 'scatter'
# information on plot types -> https://www.edureka.co/blog/python-matplotlib-tutorial/#types

for i in df:
    df[i].value_counts().plot(kind='pie')
    plt.show()

###############
# probably easier to turn you list into a DataFrame and run code above
# do this below, change your_list to name of your list and your_df to whatever you want

your_df = pd.DataFrame(data=your_list)

###############
# if you don't have a DataFrame (list, or single column of data) then do it without the for loop
# just replace 'your_list' with your lists name
# don't forget the plt.show() before creating another plot

valueCounts = [[x,your_list.count(x)] for x in set(your_list)]
plt.bar((valueCounts[0][0],valueCounts[1][0]) , (valueCounts[1][0],valueCounts[1][1]))
plt.show()

# specific to making a bar chart
# first line calculates amount of each value in your list
# in the brackets first set of valueCounts are the numbers, second set will be the corresponding name for that value
# valueCounts[0][0] is the amount of the first value, valueCounts[1][0] is the name of the first value
