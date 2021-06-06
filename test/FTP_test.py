import unittest
import sys
sys.path.append(r'\Users\cahit\Desktop\Hovedopgave')
import environment as env
import ftplib
from ftplib import FTP
import FTP_download
import time


class FTPTestCase(unittest.TestCase):

    def test_FTP_connection(self):
        #connecting
        ftp = FTP()
        host = 'ftp.kortforsyningen.dk' 
        ftp.connect(host,21)
        ftp.login(env.ftp_user,env.ftp_password)
        
        expected_FTP_conn_status = '220 ProFTPD 1.3.5e Server (Kortforsyningen FTP) [172.17.5.200]'
        expected_FTP_host = host
        expected_FTP_port = 21

        actual_FTP_conn_status = ftp.getwelcome()
        actual_FTP_host = ftp.host
        actual_FTP_port = ftp.port 
        
        self.assertAlmostEqual(expected_FTP_conn_status, actual_FTP_conn_status)
        self.assertEqual(expected_FTP_host, actual_FTP_host)
        self.assertEqual(expected_FTP_port, actual_FTP_port)

        ftp.close()
       


    @unittest.expectedFailure
    def test_FTP_connection_FAIL(self):
        #connecting
        ftp = FTP()
        host = 'ftp.kortforsyningen.dk' 
        ftp.connect(host,21)
        ftp.login(env.ftp_user,env.ftp_password)
        
        expected_FTP_conn_status = '220 ProFTPD 1.3.5e Server (Kortforsyningen FTP) [172.17.5.200]'
        expected_FTP_host = host
        expected_FTP_port = 21

        actual_FTP_conn_status = ftp.getwelcome()
        actual_FTP_host = ftp.host
        actual_FTP_port = ftp.port 
        
        self.assertNotEqual(expected_FTP_conn_status, actual_FTP_conn_status)
        self.assertNotEqual(expected_FTP_host, actual_FTP_host)
        self.assertNotEqual(expected_FTP_port, actual_FTP_port)
        ftp.close()  
       



   
    #IMPORTANT --> test_check_if_files_for_download_exist_in_FTP(self) and test_check_if_files_for_download_exist_in_FTP_FAIL  
    # requires approximately 40 minutes to run the test due to the request of the huge FTP folder (50.000 files). 
    # Please type test in the beginning of the def name to run them.
    def est_check_if_files_for_download_exist_in_FTP(self):

        lon = 9.4444
        lat = 56.7777
        
        expected_files_to_download = ['skraa_1km_6291_526_JPG_UTM32-ETRS89.zip', 'skraa_1km_6292_526_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6293_526_JPG_UTM32-ETRS89.zip', 'skraa_1km_6291_527_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6292_527_JPG_UTM32-ETRS89.zip', 'skraa_1km_6293_527_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6291_528_JPG_UTM32-ETRS89.zip', 'skraa_1km_6292_528_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6293_528_JPG_UTM32-ETRS89.zip']
        
        actual_files_to_download = FTP_download.get_list_of_neighbours_for_download(lon, lat)

        #asserting that expected files to be the same as actual files
        self.assertEqual(expected_files_to_download,actual_files_to_download)

        #connecting to ftp server
        ftp = FTP()
        host = 'ftp.kortforsyningen.dk' 
        ftp.connect(host,21)
        ftp.login(env.ftp_user,env.ftp_password)

        #changing the ftp directory to destination where files are located
        path = '/grundlaeggende_landkortdata/skraafoto'
        ftp.cwd(path)
        #retrieving all files in the ftp server path into a list
        actual_files_in_FTP_directory = ftp.nlst(path)

        #asserting all the actual files to be found within the ftp server
        list_to_string_all_files_in_FTP = ' '.join([str(elem) for elem in actual_files_in_FTP_directory])
        for file_to_download in actual_files_to_download:
            self.assertIn(file_to_download, list_to_string_all_files_in_FTP)

        ftp.close()


    @unittest.expectedFailure
    def est_check_if_files_for_download_exist_in_FTP_FAIL(self):

        lon = 9.4444
        lat = 56.7777
        
        expected_files_to_download = ['skraa_1km_6291_526_JPG_UTM32-ETRS89.zip', 'skraa_1km_6292_526_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6293_526_JPG_UTM32-ETRS89.zip', 'skraa_1km_6291_527_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6292_527_JPG_UTM32-ETRS89.zip', 'skraa_1km_6293_527_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6291_528_JPG_UTM32-ETRS89.zip', 'skraa_1km_6292_528_JPG_UTM32-ETRS89.zip', 
                                      'skraa_1km_6293_528_JPG_UTM32-ETRS89.zip']
        
        actual_files_to_download = newest.get_list_of_neighbours_for_download(lon, lat)

        #connecting to ftp server
        ftp = FTP()
        host = 'ftp.kortforsyningen.dk' 
        ftp.connect(host,21)
        ftp.login(env.ftp_user,env.ftp_password)

        #changing the ftp directory to destination where files are located
        path = '/grundlaeggende_landkortdata/skraafoto'
        ftp.cwd(path)
        #retrieving all files in the ftp server path into a list
        actual_files_in_FTP_directory = ftp.nlst(path)

        #asserting all the actual files to be found within the ftp server
        list_to_string_all_files_in_FTP = ' '.join([str(elem) for elem in actual_files_in_FTP_directory])
        for file_to_download in actual_files_to_download:
            assert file_to_download not in list_to_string_all_files_in_FTP

        ftp.close()
   

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)