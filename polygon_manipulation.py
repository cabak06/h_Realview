
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def get_inner_box(x_shrink,y_shrink,polygon):
    """
        This method shrinks/enlarges the size of any given polygon keeping its prior dimensions
        param x_shrink: float  <1 = shrink, >1 = enlarge
        param y_shrink: float  <1 = shrink, >1 = enlarge
        return list of new polygon coordinates as tuble pairs
    """
    try:
        xs = [i[0] for i in polygon]
        ys = [i[1] for i in polygon]
        # calculating a center
        x_center = 0.5 * min(xs) + 0.5 * max(xs)
        y_center = 0.5 * min(ys) + 0.5 * max(ys)
        # shrink figure
        new_xs = [(i - x_center) * (1 - x_shrink) + x_center for i in xs]
        new_ys = [(i - y_center) * (1 - y_shrink) + y_center for i in ys]
        # create list of new coordinates
        new_coords = zip(new_xs, new_ys)
        new_coords_as_list = list(new_coords)
        return new_coords_as_list
    except Exception as err:
        print('Error, not able to shrink polygon: ',err)


def check_pointmatch_to_innerbox(lon,lat,polygon):
    """
        This method checks whether a point given in longitude and latitude is within any given polygon
        param lon: float value for longitude
        param lat: float value for latitude
        param box: list of tuple pair consiting of lon and lat values
        return boolean: True if point to check is within given polygon
    """
    try:
        innerbox = get_inner_box(0.2,0.2, polygon)
        #print(innerbox)
        arr_pol = np.array(innerbox)
        polygon = Polygon(arr_pol) # create polygon
        point = Point(lon,lat) # create point
    #   print(point.within(polygon))
        return polygon.contains(point)
    except Exception as err:
        print('Error, not able to check pointmatch: ',err)


