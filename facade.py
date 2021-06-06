import psycopg2 as db
from psycopg2 import extensions
import environment as env


def get_block_info_from_DB(blk):
    try:
        conn = db.connect(
        host=env.db_host,
        dbname=env.db_database,
        user=env.db_user,
        password=env.db_password
        )
    except Exception as err:
        print('could not connect to DB ', err)
    if not conn.status == extensions.STATUS_READY:
        #Default value for DB connection positive is 1
        raise Exception("connection not ready for transaction")
    conn.autocommit = True
    try:
        sql = f"SELECT imageid, direction, centroid_t, wkb_geometry FROM footprints.footprints where centroid_t like '{blk}';"
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as err:
        print('could not execute query ', err)



def convert_wkb_to_UTM_grids(imgid):
    #this method takes a picture id as param and converts the wkb coords to UTM coords
    try:
        conn = db.connect(
        host=env.db_host,
        dbname=env.db_database,
        user=env.db_user,
        password=env.db_password
        )
    except Exception as err:
        print('could not connect to DB ', err)
    if not conn.status == extensions.STATUS_READY:
        #Default value for DB connection positive is 1
        raise Exception("connection not ready for transaction")
    conn.autocommit = True
    try:
        sql = f"SELECT btrim(st_astext(wkb_geometry),'POLYGON()') from footprints.footprints where imageid like '{imgid}';"
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as err:
        print('could not execute query ', err)
