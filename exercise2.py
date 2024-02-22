import pandas as pd
import datetime

###TASK3 - Load a simple CSV file into a Pandas DataFrame. 
#Use basic commands to explore the first few rows, 
#data types of each column, and summary statistic

filename = 'people-1000.csv'
info = pd.read_csv(filename)

#see what info does this data have
print(info.columns)

#TASK9 - Perform basic string operations on a DataFrame column, 
#such as converting to lowercase, stripping whitespace, 
#or splitting strings into lists.

#making all column names lowercase
info.columns = info.columns.str.lower()
#converting column with gender to lowercase
info['gender'] = info['gender'].str.lower()

#creating the column with only birth year
info['birth year'] = info['date of birth'].str.split('-',expand=True)[0].astype(int)

#creating column with decade
info['decade'] = info['birth year']//10*10

#add age column
info['age'] = datetime.date.today().year - info['birth year']

#TASK7 - Add a new column to a DataFrame, calculated 
#from existing columns (e.g., a total or average). 
#Practice renaming and deleting columns.
#delete birth year column
info.rename(columns={'birth year':'year of birth'},inplace=True)
info.drop(columns='year of birth', inplace=True)

#TASK10 - Combine the skills learned in previous tasks to clean a simple dataset. 
#Identify and fill missing values using the fillna() 
#method with a specified value (e.g., the mean of the column).

# counting number of males and females in each decade
pivot_table1 = info.pivot_table('index', index = 'decade', columns='gender',aggfunc = 'count')
pivot_table1.fillna(0, inplace=True)
pivot_table1= pivot_table1.astype(int)
print(f'#####\nHere is a list of male and female specialists divided by decade:\n{pivot_table1}')
#find and delete outliers
outliers = (info['age']>80) | (info['age']<16) 
info = info[~outliers]

#find jobs that appear more then once
pivot_table2 = info.pivot_table('index', aggfunc='count', index='job title')

#find jobs that are connected with maganement
management_specialists_info = info[info['job title'].str.contains('manage', case=False)]

#find peaople that are connected with maganement and are older then 25
management_specialists_info = management_specialists_info[management_specialists_info['age']>=25]
print(f"#####\nHere are all management specialists who are older than 25:\n{management_specialists_info[['first name','job title']]}")


#DATA VISUALIZATION
#makin some pie diagram
import matplotlib.pyplot as plt
all_styles = plt.style.available

plt.style.use(all_styles[11])

pivot_table1['total'] = pivot_table1['male']+pivot_table1['female']
count = pivot_table1['total'].values
values = pivot_table1.index
patches, texts,autotexts = plt.pie(count, labels = values, autopct='%1.1f%%')
#plt.pie(count, labels = values,autopct='%1.1f%%', textprops={'color': 'white'})
plt.setp(autotexts, color = 'white')
plt.title('Percentage of Speatialits Of Different Decades')
plt.show()