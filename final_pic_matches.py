import coords_manipulation as cm
import polygon_manipulation as pm


def get_final_pictures_id_within_lon_lat_polygon_match(lon,lat):
    list_of_matches = []
    elements = cm.convert_wkb_to_lat_lon(lon, lat)
    print(len(elements))
    for element in elements:
        polygon = element[3]
        shrinked_polygon = pm.get_inner_box(0.1, 0.1, polygon)
        match = pm.check_pointmatch_to_innerbox(lon, lat, shrinked_polygon)
        if(match):
            list_of_matches.append(element)
    return list_of_matches




