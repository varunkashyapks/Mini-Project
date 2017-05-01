import pandas as pd
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='sandeepbabgond', api_key='vcpfBduhzWqlk04B7Tc8')

df = pd.read_excel('/home/varun/project2/cleaneddata/PrimaryNAR_cleaned.xlsx')

data2 = dict(
 type = 'choropleth',
 locations = df['ISO Code'],
 z = df['Total'],
 text = df['Countries'],
 colorscale = [[0,'rgb(5, 10, 172)'],[0.35,"rgb(106, 137, 247)"],[0.5,"rgb(190,190,190)"],\
 [0.6,"rgb(220, 170, 132)"],[0.7,"rgb(230, 145, 90)"],[1,"rgb(178, 10, 28)"]],
 autocolorscale = False,
 reversescale = True,
 name = 'Total',
 marker = dict(
 line = dict (
 color = 'rgb(220,220,0)',
 width = 1.0
 ) ),
 
 )
fig = dict( data=[data2] )
py.iplot( fig, validate=False, filename='Primary_net_attendance_rate_map' )
