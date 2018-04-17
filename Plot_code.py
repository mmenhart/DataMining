import matplotlib.pyplot as plt

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
# if you don't have a DataFrame (list, or single column of data then do it without the for loop
# just replace 'your_list' with the variable name
# don't forget the plt.show() before creating another plot

your_list.value_counts().plot(kind='bar')
plt.show()
