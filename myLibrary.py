class myLibrary:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plot
    import os
    import seaborn as sns
    from sklearn.preprocessing import OneHotEncoder
    from scipy import stats
    import pylab as py
    import statsmodels.api as sm
    import statsmodels.stats.api as sms
    
    def __init__(self,data):
        self.data = data
        
    def printsummary(self): 
        print(self.data.info())
        
    def printData(self): 
        print(self.data)
        
    def headData(self, line):
        print(self.data.head(line))
        
    def describeData(self): 
        print(self.data.describe())
        
    def describe(self,x): 
        print(self.stats.describe(x))
    
    def columnType(self): 
        print(self.data.dtypes)
        #self.data.isnull().sum(axis = 0)
        
    #Data Visualiation
    def distplot(self,cloumIndex):
        f,axes = self.plot.subplots(1,1)
        sns.distplot(self.data.iloc[:,cloumIndex])
    
    def countplot(self,cloumIndex):
        f,axes = self.plot.subplots(1,1)
        sns.countplot(self.data.iloc[:,cloumIndex],data=self.data)
        
    def boxplot(self):
        sns.boxplot(data=self.data)
        
    def heatmap(self):
        fig,ax = self.plot.subplots(figsize=(8, 8))
        sns.heatmap(self.data.corr())
    
    def histogram(self,x):
        self.pd.DataFrame(x).plot.hist()
    
    def histogramData(self):
        self.pd.DataFrame(self.data['bad']).plot.hist()
    #probability plot
    def probplot(self,cName):
        self.stats.probplot(self.data[cName], dist="norm", plot = self.py) 
        self.py.show()
    #sampels queantities
    def qqplot(self,cName):
        self.sm.qqplot(self.data[cName], line="s")
        self.py.show()
    
    def shapiro(self,cName,alpha):
        stat, p = self.stats.shapiro(self.data[cName])
        print("Statistics:%3.3f, p=%.3f " % (stat,p))
        # H0: Normal dagilimdan gelmektedir
        # H1: Normal dagilimdan gelmemektedir.
        if p>alpha:
            print("Orneklem Normal (Gaussian) Dagilimdan gelmektedir (Fail to Reject H0)")
        else:
            print("Orneklem Normal (Gaussian) Dagilimdan gelmemektedir (reject H0")
        
    def ttest_1samp(self,cName,num):
        stat, p = self.stats.ttest_1samp(self.data[cName], popmean=num)
        print("Statistics:%3.3f, p=%.3f " % (stat,p))
    def ProbabilityDistribubtion(self,cName,num):
        p = self.stats.t.ppf(q=num, df=len(self.data[cName]) -1)
        print("p=%.3f " % (p))
    
    def CumulativeDistribution(self,cName,num):
        p = self.stats.t.cdf(x = num, df=len(self.data[cName])-1)*2
        print("p=%.3f " % (p))
    
    #Populasyon ve Sample ortalamasi araligini olcmek icin kullanilir.
    def DescrStatsW(self,cName):
        p =self.sms.DescrStatsW(self.data[cName]).tconfint_mean()
        print(p)
