import pandas as pd
# Use pandas.head(number) to look at the top of data
# Use pandas.tail(number) to look at the bottom of data
# Use .columns to print out the all the column titles
# Use df['name_of_column'][0:10] to get a specific column and within a specific range
# df.iloc[1:4] is another way to specify rows
# You can specify exact columns like this df[['name1','name2','name3']]
# df.loc[df['column-name'] == "desired-value-in-column"] 
# is a way to print out all elements that share that same value in the same column.
# For example print((df.loc[df['HP'] == 90])) would print out all rows where the HP column has the value of 90

# There are built in pandas functions for csv(read_csv('')), excel(read_excel('')) and txt files.
# txt files uses the read_csv but with a delimiter. 

df = pd.read_csv('pokemon_data.csv')
#df_excel = pd.read_excel('pokemon_data.xlsx')

# print(df.head(4))

print((df.loc[df['HP'] == 90]))