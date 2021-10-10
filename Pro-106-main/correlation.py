import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    marks_in_percentage=[]
    day_present=[]
    with open(data_path) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            day_present.append(float(row["Days Present"]))
        return{"x":marks_in_percentage,"y":day_present}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation Between Student Marks vs Days Present: ", correlation[0,1])
def setup():
    data_path="e:/Python/Pro-106/Student Marks vs Days Present.csv"
    datasource=getDataSource(data_path)
    findcorrelation(datasource)
setup()
