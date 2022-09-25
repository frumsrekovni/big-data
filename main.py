import pandas as pd
# Use pandas.head(number) to look at the top of data
# Use pandas.tail(number) to look at the bottom of data
# Use .columns to print out the all the column titles
# Use pandas['name_of_column'][0:10] to get a specific column and within a specific range

# There are built in pandas functions for csv(read_csv('')), excel(read_excel('')) and txt files.
# txt files uses the read_csv but with a delimiter. 

df = pd.read_csv('pokemon_data.csv')
#df_excel = pd.read_excel('pokemon_data.xlsx')

print(df['HP'][0:10])