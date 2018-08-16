#Imports for data science tools, numpy panda
#Imports for visualization, bokeh
import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.palettes import mpl
from bokeh.palettes import brewer
from bokeh.layouts import gridplot
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

############ GET #############

ajaxGET = pd.DataFrame(pd.read_csv('path/to/csv'))
#ajaxGET.index += if you would like to start your graph not at 0, select number to start at here 

#NG = y value upper  
print(ajaxGET)
def  stacked(ajaxGET): 
    ajax_main = ajaxGET.cumsum(axis=1)
    print(ajax_main)
    ajax_welcome = ajax_main.shift(axis=1).fillna({'first_column_value': 0})[::-1]
    print(ajax_welcome)
    ajax_stack = pd.concat([ajax_main, ajax_welcome], ignore_index=True)
    return ajax_stack

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

areas = stacked(ajaxGET)
colors = mpl['Viridis'][areas.shape[1]]
x2 = np.hstack((ajaxGET.index[::-1],ajaxGET.index))

getP =  figure(tools=TOOLS, title="Trends in Organic Beauty Industry", y_axis_label='Money Spent', x_axis_label='Month of 2017', x_range =(1, NG-1), y_range=(0, 10000))
getP.grid.minor_grid_line_color = '#eeeeee'

getP.patches([x2] * areas.shape[1], [areas[c].values for c in areas],
          color=colors, alpha=0.8, line_color=None)

#show(p)

############ POST #############

ajaxPOST = pd.DataFrame(pd.read_csv('path/to/csv/'))
#ajaxPOST.index += if you would like to start your graph not at 0, select number to start at here 

#NP = y upper value

def  stacked(ajaxPOST):
    ajax_main2 = ajaxPOST.cumsum(axis=1)
    ajax_welcome2 = ajax_main2.shift(axis=1).fillna({'First_column_value': 0})[::-1]
    print(ajax_welcome2)
    ajax_stack2 = pd.concat([ajax_main2, ajax_welcome2], ignore_index=True)
    return ajax_stack2

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

areas2 = stacked(ajaxPOST)
colors2 = mpl['Viridis'][areas2.shape[1]]
x3 = np.hstack((ajaxPOST.index[::-1],ajaxPOST.index))

postP = figure(tools=TOOLS, title="Amazon's Most Popular Products", y_axis_label='Amount bought in thousands', x_axis_label='Month', x_range =(1, NP-1), y_range=(0, 10000))
postP.grid.minor_grid_line_color = '#eeeeee'

postP.patches([x3] * areas2.shape[1], [areas2[c].values for c in areas2],
          color=colors2, alpha=0.8, line_color=None)

#show(p2)

############ HORIZONTAL SHOW ALL IN GRIDPLOT #############

output_file('ConsumerData.html', title='Consumption Data')

grid = gridplot([getP, postP], [None, None])
show(grid)

