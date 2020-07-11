import seaborn.apionly as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import os 
from sklearn.preprocessing import OneHotEncoder
from scipy import stats
class Information:
    def __init__(self,data):
        print("data: " + data.info())
        self.data = data
    
    def print_data(self): 
        print("data is : " + self.data)
    
    def fill_data(self,data): 
        self.data = data;
        print("data is : " + self.data)
        
    def dataHead(self, colunm):
        print(self.data.head(colunm))
        
    def dataDescribe(self): 
        print(self.data.describe())

        
class visualize:
    def __init__(self,data):
        print("Data Visualization :")
        self.data = data
        
    def vizu(self,data):

class reprocessingStrategy:
    def __init__(self,data):
        print("Data Preprocessing: ")
    def fill_data(self,data):
        self.data = data
      
    def feature_extrating(self):
        
class gridSarchHelper: