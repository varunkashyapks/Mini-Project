import pandas as pd

def prepare_sheet():
	df = pd.ExcelFile(r"/home/varun/Desktop/Project/Table-Youth-and-Adult-Literacy-Rate.xlsx")
	df = df.parse('Adult literacy rate',skiprows = 10 ,na_values = ['NA'])
	df.columns=['ISO Code','Countries','Year','Total','S5','Male','S7','Feamle','S9','S10']
	df = df.iloc[:-18,:]
	df = df.drop('S10', axis = 1)
	df = df.dropna(axis='columns',how='all')

	df = df.convert_objects(convert_numeric=True)
	df = df.dropna(axis='rows',how='any')

	df.to_excel('Adult_literacy_rate_cleaned.xlsx',index = False)
prepare_sheet()
