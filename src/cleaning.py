#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import plotly.express as px
import plotly.graph_objects as go
import os

##loading the dataset
attacks = pd.read_csv("/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/input/attacks.csv",encoding='latin1')

#Exploring the dataset general info
attacks.shape

#Exploring the missing values per column
##checking missing values per column
Nan_attacks= attacks.isna().sum()
missing_value_attack = pd.DataFrame({'Feature': attacks.columns,
                                 'Missing values': Nan_attacks})
missing_value_attack

##checking missing values percentages
percent_missing = attacks.isnull().sum() * 100 / len(attacks)
percent_missing
Nan_attack_percentage = pd.DataFrame({'Feature': attacks.columns,
                                 'Missing %': percent_missing})
Nan_attack_percentage 

##deleting columns with 100% missing values
attacks.pop("Unnamed: 22")
attacks.pop("Unnamed: 23")

##checking the number of columns
attacks.shape

#Deleting ignorable missing data
##poping missing values having age as reference
attacks.dropna(subset=['Age'], inplace = True)

##dataframe updated after ignorable NaN deletion
attacks.shape

##checking updated missing values percentages after poping Unnamed:22 and :23
percent_missing = attacks.isnull().sum() * 100 / len(attacks)
percent_missing
Nan_attack_percentage = pd.DataFrame({'Feature': attacks.columns,
                                 'Missing %': percent_missing})
Nan_attack_percentage 

##checking updated min, max and mean missing values percentages after poping Unnamed:22 and :23
print(Nan_attack_percentage['Missing %'].mean())
print(Nan_attack_percentage['Missing %'].max())
print(Nan_attack_percentage['Missing %'].min())

#Standardizing columns
##evaluating columns
attacks.columns

#deleting columns with info that will not be needed

def pop_column(df):

    df.pop("Investigator or Source")
    df.pop("pdf")
    df.pop("href formula")
    df.pop("href")
    df.pop("original order")
    df.pop("Case Number.1")
    df.pop("Case Number.2")
    df.pop("Case Number")
    df.pop("Time")
    df.pop("Name")

##updating evaluating columns
attacks.columns

##check the shape
attacks.shape

#Standardizing columns names
##Creating a dictionary and standardazing columns names
dict_attacks_rename = {column : column.lower().strip() for column in attacks}
attacks = attacks.rename(dict_attacks_rename, axis = 1)
attacks.columns

##checking for duplicates
attacks.duplicated().sum()

##printing types and one example of case
print(attacks.dtypes)
print(attacks.iloc[0])

#CLeaning variables
##Date
###explore data counts
attacks["date"].value_counts()

### list unique values
list(attacks["date"].unique())

###extract month from date - regex
attacks['date'] = attacks['date'].str.extract('(-\D{3}-)', expand=True)

###remove - as separator
regex_list = [r"(-\D{3}-): ", r"-"]
attacks['date'] = attacks['date'].replace(regex=regex_list, value="")

###create column month
attacks['month']=attacks['date']

###check unique values
attacks["month"].unique()

###count months
attacks["month"].value_counts()

###plot months distribution
fig, ax = plt.subplots(figsize=(12, 8))
attacks.dropna(subset=['month'], inplace = True)
sns.histplot(ax=ax,data=attacks, x="month")
fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/month.png')

##Year
###transforming year from float to integer
attacks.dropna(subset=['year'], inplace = True)
attacks.year = attacks.year.astype(int)

###plotting year distribution
fig, ax = plt.subplots(figsize=(15, 8))
sns.histplot(x=attacks.year, bins=30)
fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Year_all.png')

###Removing the data where 'Year'
attacks = attacks.loc[attacks['year'] > 1850,:]
fig, ax = plt.subplots(figsize=(15, 8))
sns.histplot(ax=ax,x=attacks.year, bins=20,color='blue')
fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Year_1850.png')

###plotting in another way - year
attacks = attacks.loc[attacks['year'] > 1850,:]
fig, ax = plt.subplots(figsize=(80, 9))
sns.countplot(ax=ax,x=attacks.year, )
fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Year.png')

##Sex
###count values to explore
attacks["sex"].value_counts()

###count unique values
attacks["sex"].unique()

###cleaning values
attacks.loc[attacks['sex'].str.contains('M ', case=False, na=False), 'sex'] = 'M'
attacks.drop(attacks[attacks["sex"] == 'lli'].index, inplace=True)
attacks.drop(attacks[attacks["sex"] == 'nan'].index, inplace=True)

###ploting gender count
fig, ax = plt.subplots(figsize=(15, 8))
sns.countplot(ax=ax,x=attacks.sex)
fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Gender.png')

###creating a dummy variable
attacks["sex_count"]=attacks["sex"].replace(['M', 'F'],[1, 0], inplace=False)

##Age
###count values to explore
attacks["age"].value_counts()

###explore unique values
list(attacks["age"].unique())

###extract age
attacks['age'] = attacks['age'].str.extract('(\d{1,2})', expand=True)

###drop missing values
attacks.dropna(subset=['age'], inplace = True)
attacks.age = attacks.age.astype(int)

###plot age
fig, ax = plt.subplots(figsize=(12, 8))
sns.histplot(ax=ax,x=attacks.age, bins=30)
fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Age.png')

###plot attacks per age per gender
attacks.groupby(["age", "sex"])["sex"].count().plot(kind="bar", color=["slategray","coral"])
sns.set(rc={'figure.figsize': (20,15)})
sns.set_style('whitegrid')




