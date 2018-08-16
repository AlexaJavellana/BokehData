from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, Legend
from bokeh.palettes import Category20b_17
from bokeh.plotting import figure
import pandas as pd
import numpy as np

#countryPlease = pd.DataFrame(pd.read_csv('/path/to/csv'), names = ['name name'])

colnames = ['PlacetoVisit', 'YearlyVisitors']
stats = pd.read_csv('/path/to/csv', names=colnames)

places = pageViews.PlacetoVisit.tolist()
people = pageViews.Pageviewsper.tolist()
#print(country)
#print(ppm)

source = ColumnDataSource(data=dict(places=places, people=people, color=Category20b_17))

p = figure(x_range=places, y_range=(0, 100), plot_height=350, title="Let's Pick Somewhere To Go",
           toolbar_location=None, tools="")

p.vbar(x='places', top='people', width=0.8, color='color', source=source)

p.xgrid.grid_line_color = None
#Sorry I'm hard coding everything, last day of internship calls for brute force!!!!!
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

'''Creating a custom, out of plot legend
r0 = p.square(x, 3*y, fill_color=Category20b_17[0], line_color=None)

legend = Legend(items=[
    (label, renderers)
], location=(0, -28), label_text_font_size='8pt', spacing=0)

p.add_layout(legend, 'right')
'''
output_file("PageViews.html")
show(p)
