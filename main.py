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

#print(df['人名/本名'].value_counts())
df = pd.read_excel('data/excel/japanese-people-data.xlsx')
df = df.reset_index()

# totkawa = 0
# for index, row in df.iterrows():
#     totkawa += row.str.count('三')

# print(int(totkawa))
# df["Indexes"]= df["人名/本名"].str.find('三')


# df = pd.read_csv('pokemon_data.csv')
# print(df['Type 1'].value_counts())
datastring = "人名/本名	生年月日浅田 真央	1990年9月25日荒川 静香 	1981年12月29日シェーファーアヴィ幸樹 	1998年1月28日須藤 元気 	1978年3月8日風間靖幸	1970年2月1日宇野 昌磨	1997年12月17日武田 幸三	1972年12月27日白井 健三	1996年8月24日松井 秀喜	1974年6月12日小比類巻 貴之	1977年11月7日桜井 政博	1970年8月3日岩田 聡	1959年12月6日"
enddata = {}
  
for characterindata in datastring:
    enddata[characterindata] = enddata.get(characterindata, 0) + 1

print ("Frequency of each Kanji : \n"+ str(enddata))