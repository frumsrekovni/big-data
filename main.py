import pandas as pd
# import matplotlib.pyplot as plt
# Use pandas.head(number) to look at the top of data
# Use pandas.tail(number) to look at the bottom of data
# Use .columns to print out the all the column titles
# Use df['name_of_column'][0:10] to get a specific column and within a specific range
# df.iloc[1:4] is another way to specify rows
# You can specify exact columns like this df[['name1','name2','name3']]
# df.loc[df['column-name'] == "desired-value-in-column"] 
# is a way to print out all elements that share that same value in the same column.
# For example print((df.loc[df['HP'] == 90])) would print out all rows where the HP column has the value of 90
# df.sort_values('name-of-column') sorts everything by given column. 
# df.sort_values('name-of-column', ascending=False) would be reverse.
# df['Attack + Defense'] = df['Attack'] + df['Defense'] is a way to create a new column that is the total of other columns.
# another way of adding a column: df['name-of-new-column'] = df.iloc[:,1:2].sum(axis=1)
# drop a specific column df.drop(columns=['name-of-column'])
# df.loc[~df['column-name'].str.contains('given-string')] is a way to remove all rows in the column-name that contain the given string.

# df.loc[df['column-name'].str.contains('given1|given2', flags=re.I, regex=True)] 
# give all rows that contain given1 or given2 in column-name. The re.I ignores capitalization.

# df.loc[df['column-name'].str.contains('^given-string[a-z]*', flags=re.I, regex=True)]
# give all rows that starts with given-string in column-name.

# There are built in pandas functions for csv(read_csv('')), excel(read_excel('')) and txt files.
# txt files uses the read_csv but with a delimiter. 

df = pd.read_csv('pokemon_data.csv')
#df_excel = pd.read_excel('pokemon_data.xlsx')

print(df[0:10])
