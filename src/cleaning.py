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



#Exploring the missing values per column
##checking missing values per column
def print_missing():
    Nan_attacks= attacks.isna().sum()
    missing_value_attack = pd.DataFrame({'Feature': attacks.columns,
                                 'Missing values': Nan_attacks})
    missing_value_attack




##checking updated missing values percentages after poping Unnamed:22 and :23
def print_missing_percentage():
    percent_missing = attacks.isnull().sum() * 100 / len(attacks)
    percent_missing
    Nan_attack_percentage = pd.DataFrame({'Feature': attacks.columns,
                                 'Missing %': percent_missing})
    Nan_attack_percentage 


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
    df.pop("Unnamed: 22")
    df.pop("Unnamed: 23")



#Standardizing columns names
##Creating a dictionary and standardazing columns names
def stand_colum_name():  
    dict_attacks_rename = {column : column.lower().strip() for column in attacks}
    attacks = attacks.rename(dict_attacks_rename, axis = 1)
    attacks.columns


###extract month from date - regex
def regex_date_month():
    attacks['date'] = attacks['date'].str.extract('(-\D{3}-)', expand=True)

###remove - as separator
def regex_separator_month():
    regex_list = [r"(-\D{3}-): ", r"-"]
    attacks['date'] = attacks['date'].replace(regex=regex_list, value="")



###plot months distribution
def plot_month():
    fig, ax = plt.subplots(figsize=(12, 8))
    attacks.dropna(subset=['month'], inplace = True)
    sns.histplot(ax=ax,data=attacks, x="month")
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/month.png')

##Year

###plotting year distribution
def plot_year():
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.histplot(x=attacks.year, bins=30)
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Year_all.png')

###Removing the data where 'Year'
def plot_year_1850():
    attacks = attacks.loc[attacks['year'] > 1850,:]
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.histplot(ax=ax,x=attacks.year, bins=20,color='blue')
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Year_1850.png')

###plotting in another way - year
def plot_year_colored():
    attacks = attacks.loc[attacks['year'] > 1850,:]
    fig, ax = plt.subplots(figsize=(80, 9))
    sns.countplot(ax=ax,x=attacks.year, )
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Year.png')

##Sex

###cleaning values
def clean_sex():
    attacks.loc[attacks['sex'].str.contains('M ', case=False, na=False), 'sex'] = 'M'
    attacks.drop(attacks[attacks["sex"] == 'lli'].index, inplace=True)
    attacks.drop(attacks[attacks["sex"] == 'nan'].index, inplace=True)

###ploting gender count
def plot_sex():
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.countplot(ax=ax,x=attacks.sex)
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Gender.png')

###creating a dummy variable
def transf_sex_count():
    attacks["sex_count"]=attacks["sex"].replace(['M', 'F'],[1, 0], inplace=False)

##Age

###extract age
def age_regex_digits():
    attacks['age'] = attacks['age'].str.extract('(\d{1,2})', expand=True)



###plot age
def plot_age():
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.histplot(ax=ax,x=attacks.age, bins=30)
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/EDA/Age.png')

###plot attacks per age per gender
def plot_sex_age():
    attacks.groupby(["age", "sex"])["sex"].count().plot(kind="bar", color=["slategray","coral"])
    sns.set(rc={'figure.figsize': (20,15)})
    sns.set_style('whitegrid')




