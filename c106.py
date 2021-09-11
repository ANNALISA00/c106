import plotly.express as px
import csv
import numpy as np




def getdatasource(datapath):
    marksinpercentage=[]
    dayspresent=[]

    with open(datapath) as f:
        reader=csv.DictReader(f)
        for row in reader: 
            marksinpercentage.append(float(row['marksinpercentage']))
            dayspresent.append(float(row['dayspresent']))
    
    return {'x':marksinpercentage,'y':dayspresent}
def findCorrelation(datasource): 
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between marksinpercentage vs dayspresent :- \n--->",correlation[0,1])
def setup():
     datapath = "C:/Users/skind/OneDrive/Desktop/python projects/c106/Student Marks vs Days Present.csv"
     datasource = getdatasource(datapath) 
     findCorrelation(datasource) 
setup()