###############
# this function will convert 0, sigma, nee to no and 1, mu, ja to yes
# the function won't change any other values
# function takes a DataFrame column as the input
# the for loop does this by inputting one column from a DataFrame at a time


def convert_yes_no(df):
    for i in range(len(df)):

        if df.values[i] == '0' or df.values[i] == 'sigma' or df.values[i] == 'nee':
            df.values[i] = 'no'

        elif df.values[i] == '1' or df.values[i] == 'mu' or df.values[i] == 'ja':
            df.values[i] = 'yes'

    return df


###############
# change df to the name of the DataFrame you are using

for i in df:
    df[i] = convert_yes_no(df[i])
    
