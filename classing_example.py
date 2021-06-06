import pyproj
"""
class Block:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def convert_lon_lat_to_block_format(self):
"""
        """ The method takes longitude and latitude as params and converts them to a kilometer block, ex. '1km_XXXX_XXX'
            param lon float value
            param lat float value
            return string kilometer_block
        """
"""
        try:
            p = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
            lon_lat_coord = p(self.lon,self.lat,inverse=False)
            con_lon_to_int = int(round(lon_lat_coord[0]))/1000
            con_lat_to_int = int(round(lon_lat_coord[1]))/1000
            string_lat = str(con_lat_to_int)
            string_lon = str(con_lon_to_int)
            remove_decimals_in_lat_string = string_lat.split('.')
            remove_decimals_in_lon_string = string_lon.split('.')
            lat = remove_decimals_in_lat_string[0]
            lon = remove_decimals_in_lon_string[0]
            block = '1km_' + lat + '_' + lon
            return block
        except Exception as err:
            print('could not convert lon, lat to block-format: ',err)

block = Block(9, 55)
print(block.convert_lon_lat_to_block_format())
"""



