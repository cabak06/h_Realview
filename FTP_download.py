import ftplib
from ftplib import FTP
from multiprocessing.pool import ThreadPool
import tqdm
import block
import neighbour_blocks
import environment as env



def get_list_of_neighbours_for_download(lon,lat):
    list_of_files_for_download = []
    blok = block.convert_lon_lat_to_block_format(lon,lat)  
    blocks = neighbour_blocks.generate_neighbouring_blocks(blok)
    for blck in blocks:
        block_format = f'skraa_{blck}_JPG_UTM32-ETRS89.zip'
        list_of_files_for_download.append(block_format)
    return list_of_files_for_download


def download_file(fil):
    try:
        ftp = FTP()
        host = 'ftp.kortforsyningen.dk' 
        ftp.connect(host,21)
        ftp.login(env.ftp_user,env.ftp_password)
        ftp.cwd('/grundlaeggende_landkortdata/skraafoto')
        path = 'skraafotos/'+fil
        print("downloading: ",fil)
        with open(path, 'wb') as f:
            ftp.retrbinary("RETR " + fil, f.write)
            print(f'succesfull download of: {fil}')
        ftp.close()
    except Exception as err:
        print('ERROR could not download file, ', err)



#def download_block_multiprocessing(fil):
#    download_file(fil)


def multi_threading_download_of_all_neighbours(lon,lat,num_workers):
    """Uses concurrency in order to speed up the download process. Multiple threads are used.
       Imap is used to make the download process more memory efficient.
       Tqdm is used for progress info purpose
    """
    list_of_files = get_list_of_neighbours_for_download(lon,lat)
    print(list_of_files)
    results = ThreadPool(num_workers).imap_unordered(download_file,list_of_files)
    for _ in tqdm.tqdm(results):
        print('done')

