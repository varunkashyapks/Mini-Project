import nvd3
from nvd3 import multiBarChart
from IPython.core.display import display, HTML
# saving a file into HTML file
output_file = open('Adult_literacy_rate_nvd3.html', 'w')
chart = multiBarChart(width=1000, height=400, x_axis_format=None,color = 'green')
xdata = ['Poorest','Second','Middle','Fourth','Richest']
Arabic_countries =[91.18,94.90,96.11,96.81,97.69]
Asian_countries = [78.31,84.17,88.07,90.02,91.58]
African_countries = [62.07,69.21,75.00,81.53,88.79]
American_countries = [91.33,93.55,94.59,95.42,96.72]
Other_countries = [87.01,89.64,90.65,91.52,93.34]

chart.add_serie(name="Arabic_countries", y=Arabic_countries, x=xdata)
chart.add_serie(name="Asian_countries", y=Asian_countries, x=xdata)
chart.add_serie(name="African_countries", y=African_countries, x=xdata)
chart.add_serie(name="American_countries", y=American_countries, x=xdata)
chart.add_serie(name="Other_countries", y=Other_countries, x=xdata)
chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)

# close HTML file
output_file.close()
