import block
import facade

def generate_neighbouring_blocks(block):
    """ The method takes a kilometer_block as param which constitutes the center 
        block from which all sorrounding blocks will be extracted
        param block string
        return list of blocks as string values
    """
    try:
        split_block = block.split(('_'))
        lat_middle = int(split_block[1])
        lon_middle = int(split_block[2])

        lat_lower = lat_middle-1
        lat_upper = lat_middle+1
        lon_left = lon_middle-1
        lon_right = lon_middle+1

        lat_lower_str = str(lat_lower)
        lat_upper_str = str(lat_upper)
        lat_middle_str = str(lat_middle)

        lon_left_str = str(lon_left)
        lon_middle_str = str(lon_middle)
        lon_right_str = str(lon_right)
        all_boundaries = []

        left3 = ['1km_'+lat_lower_str+'_'+lon_left_str,'1km_'+lat_middle_str+'_'+lon_left_str,'1km_'+lat_upper_str+'_'+lon_left_str]
        middle3 = ['1km_'+lat_lower_str+'_'+lon_middle_str,'1km_'+lat_middle_str+'_'+lon_middle_str,'1km_'+lat_upper_str+'_'+lon_middle_str]
        right3 = ['1km_'+lat_lower_str+'_'+lon_right_str,'1km_'+lat_middle_str+'_'+lon_right_str,'1km_'+lat_upper_str+'_'+lon_right_str]

        all_boundaries = left3 + middle3 + right3
        return all_boundaries
    except Exception as err:
        print('could not get neighbouring blocks: ',err)

block = '1km_6186_720'
aa = generate_neighbouring_blocks(block)
print(aa)

def extract_info_for_all_neighbouring_blocks(lon,lat):
    """
        The method takes longitude and latitude as params, finds all the blocks within the params.
        The data for each block is then extracted from the database.
        param lon float
        param lat float
        return list containing imageid, direction, centroid_t -->'block name' and wkb_geometry
    """
    block_ = block.convert_lon_lat_to_block_format(lon, lat)
    blocks = generate_neighbouring_blocks(block_)
    full_extraction = []
    try:
        for blk in blocks:
            block_info = facade.get_block_info_from_DB(blk)
            full_extraction.append(block_info)
    except Exception as err:
        print(err)
    return full_extraction