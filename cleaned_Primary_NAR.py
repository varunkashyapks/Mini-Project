#importing file and cleaning Primary net attendance ratio
import pandas as pd
def prepare_sheet():
 df = pd.ExcelFile(r"/home/varun/Desktop/Project/survey.xlsx")
 df = df.parse('Primary NAR',skiprows = 10 ,na_values = ['NA'])
 df = df.iloc[11:197,:]
 df.columns = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11',
 'S12','S13','S14','S15','S16','S17','S18','S19','S20','S21','S22','S23','S24']
 df = df.drop(['S5','S7','S9','S11','S13','S15','S17','S19','S21','S23','S24'],axis = 1)
 df = df.dropna(axis='columns',how='all')
 df = df.convert_objects(convert_numeric=True)
 df.to_excel('PrimaryNAR_cleaned',index = False)

prepare_sheet()
