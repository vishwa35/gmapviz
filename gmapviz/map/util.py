import numpy as np

# function to compute center of map to fit all data in
def center(arr):
  return (np.amax(arr) + np.amin(arr)) / 2

# TODO: need function to compute zoom of map to fit all data in
def zoom(arr1, arr2):
  zoom = max([np.amax(arr1) - np.amin(arr1), np.amax(arr2) - np.amin(arr2)])
  print zoom
  if zoom < 3:
    return 8
  if zoom < 10:
    return 5
  return zoom//25 if zoom > 25 else zoom//5
