import unittest
import sys
sys.path.append(r'\Users\cahit\Desktop\Hovedopgave')
import block
import neighbour_blocks
import FTP_download
import coords_manipulation
import polygon_manipulation


class ExpectedPositiveTestCase(unittest.TestCase):

    
    def test_convert_lon_lat_to_block_format(self):
        lon = 9.4444
        lat = 56.7777
        expected = '1km_6292_527'
        actual = block.convert_lon_lat_to_block_format(lon, lat)
        self.assertEqual(expected,actual)
    

    def test_generate_neighbouring_blocks(self):
        block = '1km_6292_527'
        
        #asserting that all generated blocks are similar to expected blocks
        expected_blocks = [
                          '1km_6291_526', '1km_6292_526', '1km_6293_526', 
                          '1km_6291_527', '1km_6292_527', '1km_6293_527', 
                          '1km_6291_528', '1km_6292_528', '1km_6293_528'
                          ]
        
        actual_blocks = neighbour_blocks.generate_neighbouring_blocks(block)
        self.assertEqual(expected_blocks,actual_blocks)

        #asserting that block used as param is in the middle of generated neighbour blocks
        split_block = block.split(('_'))
        lat_middle = int(split_block[1]) # 6292
        lon_middle = int(split_block[2]) # 527
        
        lat_coords_highest = str(lat_middle +1)
        lat_coords_lowest = str(lat_middle -1)
        lon_coords_highest = str(lon_middle +1)
        lon_coords_lowest = str(lon_middle -1)

        list_to_string_all_blocks = ' '.join([str(elem) for elem in actual_blocks])

        self.assertIn(lat_coords_highest, list_to_string_all_blocks)
        self.assertIn(lat_coords_lowest, list_to_string_all_blocks)
        self.assertIn(lon_coords_highest, list_to_string_all_blocks)
        self.assertIn(lon_coords_lowest, list_to_string_all_blocks)



    def test_get_list_of_neighbours_for_download(self):
        lon = 9.4444
        lat = 56.7777
        expected_files_to_download = ['skraa_1km_6291_526_JPG_UTM32-ETRS89.zip', 'skraa_1km_6292_526_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6293_526_JPG_UTM32-ETRS89.zip', 'skraa_1km_6291_527_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6292_527_JPG_UTM32-ETRS89.zip', 'skraa_1km_6293_527_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6291_528_JPG_UTM32-ETRS89.zip', 'skraa_1km_6292_528_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6293_528_JPG_UTM32-ETRS89.zip']

        actual_files_to_download = FTP_download.get_list_of_neighbours_for_download(lon, lat)

        #asserting type of expected and actual to be same datastructure, ie. lists
        type_expected_files = type(expected_files_to_download)
        type_actual_files = type(actual_files_to_download)
        self.assertEqual(type_expected_files,type_actual_files)

        #asserting length of both lists to be the same
        self.assertEqual(len(expected_files_to_download),len(actual_files_to_download))

        #asserting that content of expected_files_to_download is the same as actual
        self.assertEqual(expected_files_to_download,actual_files_to_download)

    

    def test_get_lon_lat(self):
        #coords is given as UTM grid coords --> converted to lat/lon coords: Representing a polygon

        UTM_coords = '466397 6199960,467417 6199960,467419 6199190,466399 6199190,466397 6199960'
        
        expected_tuple_pairs_of_lat_lon_coords_as_list = [(8.461989434024657, 55.943841169578555), 
                                                          (8.478319666246932, 55.94391138409766), 
                                                          (8.478444656437626, 55.93699333190399), 
                                                          (8.462117334169431, 55.93692313979108), 
                                                          (8.461989434024657, 55.943841169578555)]
        
        actual_tuple_pairs_of_lat_lon_coords_as_list = coords_manipulation.get_lon_lat(UTM_coords)

        #asserting type of expected and actual to be same datastructure, ie. lists
        expected_list = type(expected_tuple_pairs_of_lat_lon_coords_as_list)
        actual_list = type(actual_tuple_pairs_of_lat_lon_coords_as_list)
        self.assertEqual(expected_list, actual_list)

        #asserting length of both lists to be the same
        self.assertEqual(len(expected_tuple_pairs_of_lat_lon_coords_as_list), len(actual_tuple_pairs_of_lat_lon_coords_as_list))

        #asserting contents og both lists to be the same
        self.assertEqual(expected_tuple_pairs_of_lat_lon_coords_as_list,actual_tuple_pairs_of_lat_lon_coords_as_list)



    def est_get_inner_box(self):
        #polygon to shrink is a list of lat/lon pair coordinates
        polygon = [(8.461989434024657, 55.943841169578555),(8.478319666246932, 55.94391138409766), 
                   (8.478444656437626, 55.93699333190399),(8.462117334169431, 55.93692313979108), 
                   (8.461989434024657, 55.943841169578555)]
        
        expected_polygon_shrinked_by_50_percent = [(8.466103239627898, 55.94212921576146),(8.474268355739037, 55.94216432302102), 
                                                   (8.474330850834384, 55.938705296924184),(8.466167189700286, 55.93867020086772), 
                                                   (8.466103239627898, 55.94212921576146)]
        
        actual_polygon_shrinked_by_50_percent = polygon_manipulation.get_inner_box(0.5,0.5, polygon)

        #splitting the shrinked polygon in point coords to compare them with the point coords in unshrinked polygon in order to 
        # verify that the right dimensions have shrinked as expected
        unshrinked_point_upperLeft = polygon[0], unshrinked_point_upperRight = polygon[1]
        unshrinked_point_lowerRight = polygon[2], unshrinked_point_lowerLeft = polygon[3]

        shrinked_point_upperLeft = actual_polygon_shrinked_by_50_percent[0]
        shrinked_point_upperRight = actual_polygon_shrinked_by_50_percent[1]
        shrinked_point_lowerRight = actual_polygon_shrinked_by_50_percent[2]
        shrinked_point_lowerLeft =  actual_polygon_shrinked_by_50_percent[3]

        self.assertGreater(shrinked_point_upperLeft[0],unshrinked_point_upperLeft[0])
        self.assertLess(shrinked_point_upperLeft[1], unshrinked_point_upperLeft[1])
        self.assertLess(shrinked_point_upperRight[0],unshrinked_point_upperRight[0])
        self.assertLess(shrinked_point_upperRight[1],unshrinked_point_upperRight[1])
        self.assertLess(shrinked_point_lowerRight[0], unshrinked_point_lowerRight[0])
        self.assertGreater(shrinked_point_lowerRight[1], unshrinked_point_lowerRight[1])
        self.assertGreater(shrinked_point_lowerLeft[0], unshrinked_point_lowerLeft[0])
        self.assertGreater(shrinked_point_lowerLeft[1], unshrinked_point_lowerLeft[1])
        self.assertEqual(expected_polygon_shrinked_by_50_percent, actual_polygon_shrinked_by_50_percent)

 #asserting that expected polygon is the same as actual polygon
    
    def test_check_if_point_is_within_polygon(self):

        polygon = [(8.461989434024657, 55.943841169578555), 
                   (8.478319666246932, 55.94391138409766), 
                   (8.478444656437626, 55.93699333190399), 
                   (8.462117334169431, 55.93692313979108), 
                   (8.461989434024657, 55.943841169578555)]
        
        lon = 8.47003239627898 
        lat = 55.94002921576146

        expected = True 
        
        actual = polygon_manipulation.check_pointmatch_to_innerbox(lon, lat, polygon)
        
        #asserting that the point given in lat/lon is within the the polygon shrinked by 20 percent
        self.assertEqual(expected, actual)


        


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)