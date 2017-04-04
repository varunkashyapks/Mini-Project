import pandas as pd
# importing cleaned Primary NAR dataset
NAR = pd.ExcelFile(r"/home/varun/PrimaryNAR_cleaned.xlsx")
NAR = pd.read_excel("/home/varun/PrimaryNAR_cleaned.xlsx",index_col = 1)

# Dividing of countries into region 
# we made a list of countries according to their ISO Code

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

# For representing the countries and to get countries from dataset
Arabic_countries = NAR.loc[NAR['ISO Code'].isin(Arabic)]
Asian_countries = NAR.loc[NAR['ISO Code'].isin(Asia_Pacific)]
African_countries = NAR.loc[NAR['ISO Code'].isin(African_Region)]
American_countries = NAR.loc[NAR['ISO Code'].isin(American_Region)]
Other_countries = NAR.loc[~NAR['ISO Code'].isin(Others)]

# If Arabic countries present in dataset then it will print the

print Arabic_countries