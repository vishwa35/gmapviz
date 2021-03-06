from ..map.api import *
import numpy as np
import os 

# get location data from numpy arr
data = np.load("gmapviz/examples/locations_yvr.npy")

# configure API key 
m = gmapviz(os.environ['GOOG_KEY_LH'])
# feed lat lng data for scatter plot
m.scatter(data)
# render scatter plot html
m.render("gmapviz/examples/scatter.html")
