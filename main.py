
import final_pic_matches as fm
import FTP_download as fd

lon = 12.511865112061377
lat = 55.77061562593357 

#final_list_of_pic_ids = fm.get_final_pictures_id_within_lon_lat_polygon_match(lon, lat)
#print(final_list_of_pic_ids)



#print(len(final_list_of_pic_ids))
#print(final_list_of_pic_ids)


fd.multi_threading_download_of_all_neighbours(lon,lat, 9)




