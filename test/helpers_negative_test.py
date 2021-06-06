import unittest
import sys
sys.path.append(r'\Users\cahit\Desktop\Hovedopgave')
import block
import neighbour_blocks
import FTP_download
import coords_manipulation
import polygon_manipulation


class ExpectedFailuresTestCase(unittest.TestCase):
        
    @unittest.expectedFailure
    def test_convert_lon_lat_to_block_format(self):
        lon = 9.4444
        lat = 56.7777
        expected1 = '1km_6291_527'
        actual = block.convert_lon_lat_to_block_format(lon, lat)
        print(actual)
        self.assertEqual(expected1,actual)
        self.assertEqual(expected2,actual)


    @unittest.expectedFailure
    def test_generate_neighbouring_blocks(self):
        block = '1km_6292_527'
        
        #asserting that all generated blocks are similar to expected blocks
        expected_blocks = [
                          'Wrong Block', 'Wrong Block', 'Wrong Block', 
                          'Wrong Block', 'Wrong Block', 'Wrong Block', 
                          'Wrong Block', 'Wrong Block', 'Wrong Block'
                          ]
        
        actual_blocks = neighbour_blocks.generate_neighbouring_blocks(block)
        self.assertEqual(expected_blocks,actual_blocks)

    
    @unittest.expectedFailure
    def test_get_list_of_neighbours_for_download(self):
        lon = 9.4444
        lat = 56.7777
        expected_files_to_download = ['NOT_1km_6291_526_JPG_UTM32-ETRS89.zip', 'NOT_1km_6292_526_JPG_UTM32-ETRS89.zip', 
                                      'NOT_1km_6293_526_JPG_UTM32-ETRS89.zip', 'NOT_1km_6291_527_JPG_UTM32-ETRS89.zip', 
                                      'NOT_1km_6292_527_JPG_UTM32-ETRS89.zip', 'NOT_1km_6293_527_JPG_UTM32-ETRS89.zip', 
                                      'NOT_1km_6291_528_JPG_UTM32-ETRS89.zip', 'NOT_1km_6292_528_JPG_UTM32-ETRS89.zip', 
                                      'NOT_1km_6293_528_JPG_UTM32-ETRS89.zip']

        actual_files_to_download = FTP_download.get_list_of_neighbours_for_download(lon, lat)
        
        #asserting that content of expected_files_to_download is the same as actual
        self.assertEqual(expected_files_to_download,actual_files_to_download)


    @unittest.expectedFailure
    def test_get_lon_lat(self):
        #coords is given as UTM grid coords --> converted to lat/lon coords: Representing a polygon

        UTM_coords = '466397 6199960,467417 6199960,467419 6199190,466399 6199190,466397 6199960'
        
        expected_tuple_pairs_of_lat_lon_coords_as_list = [(8, 55),(8, 55),(8, 55),(8, 55),(8, 55)]
        
        actual_tuple_pairs_of_lat_lon_coords_as_list = coords_manipulation.get_lon_lat(UTM_coords)

        #asserting contents og both lists to be the same
        self.assertEqual(expected_tuple_pairs_of_lat_lon_coords_as_list,actual_tuple_pairs_of_lat_lon_coords_as_list)  


    @unittest.expectedFailure
    def test_get_inner_box(self):
        #polygon to shrink is a list of lat/lon pair coordinates
        polygon = [(8.461989434024657, 55.943841169578555), 
                   (8.478319666246932, 55.94391138409766), 
                   (8.478444656437626, 55.93699333190399), 
                   (8.462117334169431, 55.93692313979108), 
                   (8.461989434024657, 55.943841169578555)]
        
        expected_polygon_shrinked_by_50_percent = [(8, 55),(8, 55),(8, 55),(8, 55),(8, 55)]
        
        actual_polygon_shrinked_by_50_percent = polygon_manipulation.get_inner_box(0.5,0.5, polygon)

        #asserting that expected polygon is the same as actual polygon
        self.assertEqual(expected_polygon_shrinked_by_50_percent, actual_polygon_shrinked_by_50_percent)


    
    @unittest.expectedFailure
    def test_check_if_point_is_within_polygon(self):

        polygon = [(8.461989434024657, 55.943841169578555), 
                   (8.478319666246932, 55.94391138409766), 
                   (8.478444656437626, 55.93699333190399), 
                   (8.462117334169431, 55.93692313979108), 
                   (8.461989434024657, 55.943841169578555)]
        
        lon_true = 8.47003239627898 
        lat_true = 55.94002921576146
        lon_false = 8
        lat_false = 55

        expected_result_for_lon_lat_true = False 
        expected_result_for_lon_lat_false = True

        actual_value_for_lon_lat_true = polygon_manipulation.check_pointmatch_to_innerbox(lon_true, lat_true, polygon)
        actual_value_for_lon_lat_false = polygon_manipulation.check_pointmatch_to_innerbox(lon_false, lat_false, polygon)
        
        #asserting that the point given in lat/lon is within the the polygon shrinked by 20 percent
        self.assertEqual(expected_result_for_lon_lat_true, actual_value_for_lon_lat_true)
        self.assertEqual(expected_result_for_lon_lat_false, actual_value_for_lon_lat_false)


    
    # testing the methods when args are required but None given, should raise Exception
    def test_convert_lon_lat_to_block_format_no_args_given(self):
        with self.assertRaises(TypeError):
            block.convert_lon_lat_to_block_format()

    def test_generate_neighbouring_blocks_no_arg_given(self):
        with self.assertRaises(TypeError):
            neighbour_blocks.generate_neighbouring_blocks()
    
    def test_get_list_of_neighbours_for_download_no_args_given(self):
         with self.assertRaises(TypeError):
             FTP_download.get_list_of_neighbours_for_download()
    
    def test_test_get_lon_lat_no_arg_given(self):
        with self.assertRaises(TypeError):
            coords_manipulation.get_lon_lat() 

    def test_get_inner_box_no_args_given(self):
        with self.assertRaises(TypeError):
            polygon_manipulation.get_inner_box()  
    
    def test_check_if_point_is_within_polygon_no_args_given(self):
        with self.assertRaises(TypeError):
            polygon_manipulation.check_pointmatch_to_innerbox()    




if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)