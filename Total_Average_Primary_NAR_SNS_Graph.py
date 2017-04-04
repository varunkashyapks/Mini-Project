import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from IPython.core.display import display, HTML
import seaborn as sns 

# Importing Data Sets 

#output_file = open('PNAR_Interactive_nvd3_graph[#01].html', 'w')
NAR = pd.ExcelFile(r"/home/varun/PrimaryNAR_cleaned (another copy).xlsx")
NAR = pd.read_excel("/home/varun/PrimaryNAR_cleaned (another copy).xlsx",index_col = 1)


# Dividing of countries into region
Arabic = ['ARM','GEO','IRQ','JOR','KAZ','KGZ','OMN','PSE','SYR','TJK','TUR','TKM','UZB','YEM','UKR']

Asia_Pacific = ['AFG','AZE','BGD','BTN','CHN','KHM','IND','IDN','JPN','MDV','MNG','MMR','NPL','PAK',
'PHL','THA','VNM']
	
American_Region = ['ATG','BHS','BRB','BLZ','CAN','COL','CYM','CRI','CUB','CUW','DMA','DOM','SLV','GRL','GRD',
'GLP','GTM','HTI','HND','JAM','MTQ','MEX','SPM','MSR','ANT','KNA','NIC','PAN','PER','PRI','BES','BES','SXM',
'KNA','LCA','SPM','VCT','TTO','TCA','USA','VIR','VGB']
	
	
African_Region = ['DZA','AGO','SHN','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COG',
'COD','DJI','EGY','GNQ','ERI','ETH','GAB','GMB','GHA','GIN','GNB','CIV','KEN','LSO','LBR','LBY',
'MDG','MWI','MLI','MRT','MUS','MYT','MAR','MOZ','NAM','NER','NGA','STP','REU','RWA','STP','SEN','SYC',
'SLE','SOM','ZAF','SSD','SHN','SDN','SWZ','TZA','TGO','TUN','UGA','COD','ZMB','TZA','ZWE']

Others = Asia_Pacific+Arabic+American_Region+African_Region

# For representing the countries
Arabic_countries = NAR.loc[NAR['ISO Code'].isin(Arabic)]
Asian_countries = NAR.loc[NAR['ISO Code'].isin(Asia_Pacific)]
African_countries = NAR.loc[NAR['ISO Code'].isin(African_Region)]
American_countries = NAR.loc[NAR['ISO Code'].isin(American_Region)]
Other_countries = NAR.loc[~NAR['ISO Code'].isin(Others)]

# Taking Total Average
AV_Total_Arabic = Arabic_countries['Total'].mean()
AV_Total_Asian = Asian_countries['Total'].mean()
AV_Total_African = African_countries['Total'].mean()
AV_Total_American = American_countries['Total'].mean()
AV_Total_Other = Other_countries['Total'].mean()

Arabic_AV = {'AV_Total_Arabic':AV_Total_Arabic}
a_av1 = pd.Series(Arabic_AV)
a_av1 = pd.DataFrame(a_av1)
a_av1.columns = ['Total Average']

Asian_AV = {'AV_Total_Asian':AV_Total_Asian}
a_av2 = pd.Series(Asian_AV)
a_av2 = pd.DataFrame(a_av2)
a_av2.columns = ['Total Average']

African_AV = {'AV_Total_African':AV_Total_African}
a_av3 = pd.Series(African_AV)
a_av3 = pd.DataFrame(a_av3)
a_av3.columns = ['Total Average']

American_AV = {'AV_Total_American':AV_Total_American}
a_av4 = pd.Series(American_AV)
a_av4 = pd.DataFrame(a_av4)
a_av4.columns = ['Total Average']

Other_AV = {'AV_Total_Other':AV_Total_Other}
a_av5 = pd.Series(Other_AV)
a_av5 = pd.DataFrame(a_av5)
a_av5.columns = ['Total Average']

Total_av = [a_av1,a_av2,a_av3,a_av4,a_av5]
TotalAverage = pd.concat(Total_av)
TotalAverage = pd.DataFrame(TotalAverage)
print TotalAverage
dataset =['Arabic_countries','Asian_countries','African_countries','American_countries','Other_countries']
var = sns.barplot(x=dataset, y='Total Average',data =TotalAverage,color = 'darkblue')
var.axes.set_title('Regions vs Average NAR')
var.set(xlabel='Regions', ylabel='Average NAR')
plt.show()
