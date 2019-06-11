import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

dataset = pd.read_csv('titanic.csv')

age_manipulated_data = dataset[pd.notnull(dataset['Age'])]

embark_manipulated_data = age_manipulated_data[pd.notnull(age_manipulated_data['Embarked'])]

survival_data = embark_manipulated_data.groupby('Survived',as_index=False)

#the below codes finds effect of age on survival


#effect of age on survival rate scatter
'''
age_data = embark_manipulated_data.groupby('Age', as_index=False)
age_mean_data = age_data.mean()
age_list = age_mean_data['Age'].tolist()
num_passengers_in_age = age_data.count()['PassengerId']

scatter_plot1 = plt.scatter(age_mean_data['Age'], age_mean_data['Survived'], s=30,alpha = 0.9, c=num_passengers_in_age, cmap='RdYlGn', edgecolors='none',vmin=0,vmax=30)
plt.title('Effect of Age on Survival Rate')
plt.colorbar(scatter_plot1,label = '# of passengers')
plt.ylabel('Survival Rate')
plt.xlabel('Age')
plt.show()
'''

#this code plots survivors age distribution
'''
survival_data['Age'].plot.hist(bins=range(100), color='blue', label='Survived')
plt.xlabel('Age')
plt.title('Survivor Age Distribution')
plt.ylabel('# of passengers')
plt.show()
'''

#plots age distribution
'''
embark_manipulated_data['Age'].plot.hist(bins=range(100), color='blue')
plt.title('Age distribution of all passengers')
plt.xlabel('Age')
plt.ylabel('# of passengers')
plt.show()
'''

#this plots survival rate comparison between children and adults
'''
survival_mean_data = survival_data.mean()
children_data = embark_manipulated_data[embark_manipulated_data['Age'] <= 18]
adult_data = embark_manipulated_data[embark_manipulated_data['Age'] > 18]

children_count = children_data['PassengerId'].count()
adult_count = adult_data['PassengerId'].count()

survive_children_count = children_data['Survived'].sum()
survive_adult_count = adult_data['Survived'].sum()

children_list = [survive_children_count,children_count]
adult_list = [survive_adult_count,adult_count]
total_list = [children_count,adult_count]

survived_list = [survive_children_count,survive_adult_count]

survival_rate = [children_data.mean()['Survived'],adult_data.mean()['Survived']]

plt.bar(range(len(survival_rate)),survival_rate, align='center',color=['green', 'blue'])
plt.title('Survival rate comparison children and adults')
plt.ylabel('Survival rate')
plt.xticks(range(len(survival_rate)), ['Children','Adult'])

def create_value_labels(list_data,decimals,x_adjust,y_adjust):
    for x,y in enumerate(list_data):
        plt.text(x+x_adjust, y+y_adjust, round(list_data[x],decimals), color='w', fontweight = 'bold')

create_value_labels(survival_rate, 4, -0.1, -0.1)
plt.show()
'''

#this plots survival comparison of children and adults
'''

df = pd.DataFrame([children_list,adult_list], columns=['Survived', 'Total'], index=['Children', 'Adult'])

df.plot.bar(color=['green', 'blue'])
plt.title('Number of survived children and adults')
plt.ylabel('# of people')
plt.xticks(range(len(df.index)),df.index)

def create_value_labels(list_data,decimals,x_adjust,y_adjust):
    for x,y in enumerate(list_data):
        plt.text(x+x_adjust, y+y_adjust, round(list_data[x],decimals), color='w', fontweight = 'bold')

create_value_labels(survived_list, 1, -0.2, -50)
create_value_labels(total_list, 1, 0.05, -50)
plt.show()
'''


#the below code finds effect of gender on survival


'''
#prints out the gender based dataset

age_manipulated_data = dataset[pd.notnull(dataset['Age'])]

embark_manipulated_data = age_manipulated_data[pd.notnull(age_manipulated_data['Embarked'])]

gender_data = embark_manipulated_data.groupby('Sex',as_index=False)
gender_mean_data = gender_data.mean()

#print(gender_mean_data)
#print('Survival Rate : '+str(embark_manipulated_data['Survived'].mean()))
#print(gender_mean_data[['Sex', 'Survived', 'Age', 'Pclass', 'SibSp', 'Parch', 'Fare']])
'''

#this provides and plots the effect of gender on rate of survival
'''
total_data = gender_data['PassengerId'].count()
total_data.columns = ['Sex', 'Total']
gender_list = total_data['Sex']
del total_data['Sex']
gender_survived = gender_data['Survived'].sum()
del gender_survived['Sex']
gender_survival_data = total_data.add(gender_survived, fill_value = 0)

gender_survival_data.plot.bar(color=['green','blue'])
plt.title('Effect of gender on Survival')
plt.xlabel('Gender')
plt.ylabel('# of people')
plt.xticks(range(len(gender_list)),gender_list)

surival_gender_list = [gender_survival_data.loc[0]['Survived'], gender_survival_data.loc[1]['Survived']]
total_gender_list = [gender_survival_data.loc[0]['Total'], gender_survival_data.loc[1]['Total']]

def create_value_labels(list_data,decimals,x_adjust,y_adjust):
    for x,y in enumerate(list_data):
        plt.text(x+x_adjust, y+y_adjust, round(list_data[x],decimals), color='w', fontweight = 'bold')

create_value_labels(surival_gender_list, 1, -0.2, -50)
create_value_labels(total_gender_list, 1, 0.05, -50)
plt.show()
'''

#embark_manipulated_data = age_manipulated_data[pd.notnull(age_manipulated_data['Embarked'])] #collects passengers without missing age and embarked values

#age_manipulated_data = dataset[pd.notnull(dataset['Age'])] #collects passengers without missing age values only

#print(dataset.isnull().sum()) #to find number of values missing in each column