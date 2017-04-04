import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from IPython.core.display import display, HTML
import seaborn as sns

ALR = pd.ExcelFile(r"/home/varun/Adult_literacy_rate_cleaned.xlsx")
ALR= pd.read_excel("/home/varun/Adult_literacy_rate_cleaned.xlsx",index_col = 1)

# Dividing of countries into region
Arabic = ['ARM','ARE','GEO','IRQ','BHR','JOR','KAZ','KGZ','IRN','SAU','OMN','PSE','SYR','TJK','TUR','TKM','UZB','YEM','UKR','QAT']

Asia_Pacific = ['AFG','AZE','BGD','BTN','CHN','KHM','IND','IDN','JPN','MDV','MNG','MMR','NPL','PAK','LKA',
'PHL','THA','SGP','VNM']
  
American_Region = ['ATG','BHS','BRB','BRA','CHL','BLZ','CAN','COL','CYM','CRI','CUB','CUW','DMA','ECU','DOM','SLV','GRL','GRD',
'GLP','GTM','HTI','HND','JAM','MTQ','MEX','SPM','MSR','ANT','KNA','NIC','PAN','PER','PRI','BES','BES','SXM',
'KNA','LCA','SPM','VCT','TTO','TCA','USA','VIR','VGB','URY']
  
  
African_Region = ['DZA','AGO','SHN','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COG',
'COD','DJI','EGY','GNQ','ERI','ETH','GAB','GMB','GHA','GIN','GNB','CIV','KEN','LSO','LBR','LBY',
'MDG','MWI','MLI','MRT','MUS','MYT','MAR','MOZ','NAM','NER','NGA','STP','REU','RWA','STP','SEN','SYC',
'SLE','SOM','ZAF','SSD','SHN','SDN','SWZ','TZA','TGO','TUN','UGA','COD','ZMB','TZA','ZWE']

Others = Asia_Pacific+Arabic+American_Region+African_Region

# For representing the countries
Arabic_countries = ALR.loc[ALR['ISO Code'].isin(Arabic)]
Asian_countries = ALR.loc[ALR['ISO Code'].isin(Asia_Pacific)]
African_countries = ALR.loc[ALR['ISO Code'].isin(African_Region)]
American_countries = ALR.loc[ALR['ISO Code'].isin(American_Region)]
Others_countries = ALR.loc[~ALR['ISO Code'].isin(Others)]
# for Arabic countries
var = sns.barplot(x='ISO Code', y='Total',data =Arabic_countries)
var.set(xlabel='Countries Name', ylabel='Total literacy rate')
plt.show()
#  for asian
var = sns.barplot(x='ISO Code', y='Total',data =Asian_countries)
var.set(xlabel='Countries Name', ylabel='Total literacy rate')
plt.show()
# for African
var = sns.barplot(x='ISO Code', y='Total',data =African_countries)
var.set(xlabel='Countries Name', ylabel='Total literacy rate')
plt.show()
# for American
var = sns.barplot(x='ISO Code', y='Total',data =American_countries)
var.set(xlabel='Countries Name', ylabel='Total literacy rate')
plt.show()
# for other
var = sns.barplot(x='ISO Code', y='Total',data =Others_countries)
var.set(xlabel='Countries Name', ylabel='Total literacy rate')
plt.show()
