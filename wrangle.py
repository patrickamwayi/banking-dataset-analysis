# imports
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import env
import wrangle
import env
import os
#-----------------------------------------------------------------------------------------------------------
#acquire and preparation

def prepare_bank():
    '''
    This function takes in dataframe and returns two datasets merged together into one, rows from each dataset will be aligned by columns.
    '''
    df0 = pd.read_csv('train.csv',sep=';')
    df1 = pd.read_csv('test.csv',sep=';')
    df = pd.merge(df0, df1)
    return df

#graphs and visualizations

def graph_0():
    '''
    This function returns visualization of occupation by count
    ''' 
    #visualization of occupation by count
    sns.countplot(x="job", data = df, hue ="y")
    #print(df["job"].value_counts())
    plt.title("job vs Count")
    plt.xticks(rotation=60)
    plt.show()


