import unittest
import psycopg2 as db
from psycopg2 import extensions
import sys
sys.path.append(r'\Users\cahit\Desktop\Hovedopgave')
import environment as env
import facade


class FacadeTestCase(unittest.TestCase):

    def test_database_connection(self):
        #Default value for positive connection status code is 1
        try:
            conn = db.connect(
            host=env.db_host,
            dbname=env.db_database,
            user=env.db_user,
            password=env.db_password
            )
        except Exception as err:
            raise
        expected_status = 1
        actual_status = conn.status
        
        self.assertEqual(expected_status,actual_status)
        conn.close()


    @unittest.expectedFailure
    def test_database_connection_FAIL(self):
        #Default value for positive connection status code is 1 and negative connection is 0
        try:
            conn = db.connect(
            host=env.db_host,
            dbname=env.db_database,
            user=env.db_user,
            password=env.db_password
            )
        except Exception as err:
            raise
        expected_status = 0
        actual_status = conn.status
        
        self.assertEqual(expected_status, actual_status)
        conn.close()



    def test_get_block_info_from_DB_rows(self):
        
        expected_block = '1km_6292_527'
        
        #asserting on length of returned rows for block '1km_6292_527'
        expected_list_of_returned_rows_length = 24
        actual_list_of_returned_rows = facade.get_block_info_from_DB(expected_block)
        actual_list_of_returned_rows_length = len(actual_list_of_returned_rows)
        
        self.assertEqual(expected_list_of_returned_rows_length, actual_list_of_returned_rows_length)
        
        #asserting that every row only contains info about block '1km_6292_527'
        for row in actual_list_of_returned_rows:
            actual_block = row[2]
            self.assertEqual(expected_block,actual_block)

    
    @unittest.expectedFailure
    def test_get_block_info_from_DB_rows_FAIL(self):
        
        expected_block = '1km_6292_527'
        
        #asserting on length of returned rows for block '1km_6292_527'
        expected_list_of_returned_rows_length = 10
        actual_list_of_returned_rows = facade.get_block_info_from_DB(expected_block)
        actual_list_of_returned_rows_length = len(actual_list_of_returned_rows)
        
        #asserting that there should be 10 rows returned, whereas I now that there are 24 rows returned
        self.assertEqual(expected_list_of_returned_rows_length, actual_list_of_returned_rows_length)
        
    
    def test_convert_wkb_to_UTM_grids_using_DB(self):
        
        imgid = '2019_82_19_1_0054_00090009'
        expected_UTM_grids = ('466397 6199960,467417 6199960,467419 6199190,466399 6199190,466397 6199960',)
        actual_UTM_grids = facade.convert_wkb_to_UTM_grids(imgid)

        self.assertEqual(expected_UTM_grids,actual_UTM_grids)

    
    @unittest.expectedFailure
    def test_convert_wkb_to_UTM_grids_using_DB_FAIL(self):
        
        imgid = '2019_82_19_1_0054_00090009'
        expected_UTM_grids = ('466397 6199960,467417 6199960,467419 6199190,466399 6199190,466397 6199960',)
        actual_UTM_grids = facade.convert_wkb_to_UTM_grids(imgid)

        # falsely asserting that the expected UTM_grids is not equal actual UTM_grids 
        self.assertNotEqual(expected_UTM_grids,actual_UTM_grids)



if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)