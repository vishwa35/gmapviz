import os
import webbrowser
from jinja2 import Template, Environment, PackageLoader

from util import *
from mapTypes import *

class gmapviz:

  def __init__(self, key):
    self.API_KEY = key
    self.colors = {}
    self.context = {}
    self.template = 'base'

  # render and save html if filename provided
  def render(self, filename):
    template = self._template()

    # render html and save file
    html = template.render(self.context)

    with open(filename, 'w') as f:
      f.write(html)

    self._open(filename)
    return

  # get corresponding html template
  def _template(self):
    # read in html template for heatmap
    env = Environment(loader=PackageLoader('gmapviz', 'templates'))
    return env.get_template('{}.html'.format(self.template))

  # open tab with rendered html doc
  def _open(self, filename):
    # open in browser!
    url = 'file://' + os.path.realpath(filename)
    webbrowser.open(url, new=2)  # open in new tab
    return

  # return iFrame
  def get_embeddable_map(self):
    return
    # need to move html to destination
    # <iframe src="<link to html>" width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>

  # style map
  def set_colors(self, style_json):
    # https://mapstyle.withgoogle.com/
    return

  # custom legend
  def legend(self, style_json):
    # https://developers.google.com/maps/documentation/javascript/adding-a-legend
    return

  def heatmap(self, latlngs, mapType=ROAD, maxIntensity=100, radius=5, opacity=0.7): # latlngs: numpy array
    # convert to LatLng objects here instead of in js
    data = ''.join(['new google.maps.LatLng({}, {}),'.format(lat, lng) for lat, lng in latlngs])

    latarr, lngarr = latlngs[:,0], latlngs[:,1]

    # provide inputs
    self.context = {
      "lat": center(latarr),
      "lng": center(lngarr),
      "zoom": zoom(latarr, lngarr),
      "mapType": mapType,
      "data": data,
      "maxIntensity": maxIntensity,
      "radius": radius,
      "opacity": opacity,
      "key": self.API_KEY,
    }
    self.template = 'heatmap'

  def heatmap_weighted(self, latlngweights):
    return

  def scatter(self, latlngs, mapType=ROAD):
    # convert to LatLng objects here instead of in js
    data = '\n'.join(['var marker{}'.format(i) +  '= new google.maps.Marker({position: {' + '{}, {}'.format(lat, lng) + '}, icon: circle, map: map});'
      for i, (lat, lng) in enumerate(latlngs)]) 

    data = ''.join(['[{}, {}],'.format(lat, lng) for (lat, lng) in latlngs]) 
    latarr, lngarr = latlngs[:,0], latlngs[:,1]

    # provide inputs
    self.context = {
      "lat": center(latarr),
      "lng": center(lngarr),
      "zoom": zoom(latarr, lngarr),
      "mapType": mapType,
      "data": data,
      "key": self.API_KEY,
    }
    self.template = 'scatter'

  def add_marker(self, custom_icon=None):
    return

  def add_info_window(self, content):
    return

  def add_shape(self, coords):
    return
