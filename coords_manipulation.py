import neighbour_blocks
import facade
import pyproj


def get_lon_lat(coords):
    """
        This method converts grid coordinates to latitude and longitude coordinates.
        param coords string representation af grid coordinates
        return list of tubles consisting of lon and lat coordinates
    """

    list_of_coords = []
    lst_coords_in_pairs = coords.split(",")
    for a in lst_coords_in_pairs:
        try:
            split_pairs = a.split()
            x,y = int(split_pairs[0]),int(split_pairs[1])
            p = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
            lon_lat_coord = p(x,y,inverse=True)
            list_of_coords.append(lon_lat_coord)
        except Exception as err:
            print('Could not convert string-grids to lat and lon', err)
    return list_of_coords


def convert_wkb_to_lat_lon(lon,lat):
    """
        This method converts the wkb_geometry to latitudes and longitudes
        param lon float
        param lat float
        return list_geom list of imageid, direction, blockinfo and lat/lon
    """
    list_geom = []
    list_id = []
    elements = neighbour_blocks.extract_info_for_all_neighbouring_blocks(lon,lat)
    for element in elements:
        try:
            for values in element:
                imgid = values[0]
                direction = values[1]
                block = values[2]
                wkb = values[3]
                result = facade.convert_wkb_to_UTM_grids(imgid)
                for grid_coords in result:
                    lat_lon_coords = get_lon_lat(grid_coords)
                    list_geom.append([imgid,direction,block,lat_lon_coords])
        except Exception as err:
            print(f"Error, not able to convert wkb coords to lon,lat for {element}", err)
    
    return list_geom
