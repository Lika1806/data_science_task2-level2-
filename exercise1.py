import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

grades_math1 = {
    "Alice": 88,
    "Bob": 76,
    "Charlie": 90,
    "Diana": 85,
    "Evan": 92,
    "Fiona": 79,
    "George": 95
}
grades_math2_3 = {
    "Alice": [90,89],
    "Diana": [90,97],
    "Evan": [90,89],
    "Fiona": [72,81],
    "George": [90,72],
    "Bob": [60,67],
    "Charlie": [87,70],
}
grades_english1_2_3 = {
    "Bob": [50,69,70],
    "Charlie": [30,99,98],
    "Diana": [99,80,70],
    "Alice": [80,87,78],
    "Evan": [56,67,75],
    "Fiona": [20,32,10],
    "George": [97,88,98]
}
weight = np.array([0.2,0.3,0.5])

####
#TASK2 - Create a Pandas DataFrame manually 
#by defining a dictionary of lists, where each 
#key-value pair represents a column and its values. 
#Practice accessing and manipulating individual columns and rows.

df_math = pd.DataFrame(grades_math2_3).T.rename(columns={0:'math2',1:'math final'})
df_math1 = pd.DataFrame({'math1':grades_math1})
df_math = pd.concat([df_math,df_math1], axis=1)
#rearange columns
df_math = df_math[['math1','math2','math final']]

#creating data frame for english grades
df_english = pd.DataFrame(grades_english1_2_3).T.rename(columns={0:'eng1',1:'eng2',2:'eng final'})


#TASK7 - Add a new column to a DataFrame, calculated 
#from existing columns (e.g., a total or average). 
#Practice renaming and deleting columns.

#calculate average grade using weight of every test
df_math['avg math'] = (df_math*weight).sum(axis=1)

df_english['avg eng'] = (df_english*weight).sum(axis=1)

df_average_grades = pd.merge(df_math['avg math'],df_english['avg eng'],right_index=True,left_index=True)
print(df_average_grades)

#TASK4 - Given a DataFrame, practice selecting columns using their names and 
#filtering rows based on specific criteria 
#(e.g., select rows where a column’s value is greater than a threshold).
#TASK5 - Identify missing values in a DataFrame. 
#Practice using the isna() function to find missing values 
#and the dropna() function to remove rows with missing values.

passed_students = df_average_grades[df_average_grades>80].dropna()
failed_student = df_average_grades[(df_average_grades<=80).any(axis=1)]
print(failed_student)

#DATA VISUALIZATION

#set a style
plt.style.use('seaborn-v0_8')

bar_width = 0.3  # the width of the bars
index = np.arange(len(df_average_grades.index))  #  x-axis index

# plotting average math grades
plt.bar(index, df_average_grades['avg math'], width=bar_width, color='skyblue', label='average math grade')

# plotting average english grades with corrected offset
plt.bar(index + bar_width, df_average_grades['avg eng'], width=bar_width, color='lightgreen', label='average english grade')

# setting titles and labels
plt.title('Average Math and English grades')
plt.xlabel('Student names')
plt.ylabel('Average grades')
plt.xticks(index, df_average_grades.index)


# draqing a min needed grade
plt.plot([-1,8], [80,80], color = 'red', label = 'pass line')

# adding comments on students that passed the courses
for i, name in enumerate(df_average_grades.index):
    if name in passed_students.index:
        plt.text(i-bar_width, 96, 'passed', color ='red', fontweight = 'bold')

# extending a frame size
plt.xlim(-1, 7.25)
plt.ylim(0,110)

plt.legend()

#saving a figure into png file
plt.savefig('student_diagram.png')

plt.show()