import psycopg2
import datetime
import math 
import os

def getDB(sql_query):
    try:
        
        connection = psycopg2.connect(user = "postgres",
                                        password = "imagina12",
                                        host = "iot.igromi.com",
                                        port = "5432",
                                        database = "thingsboard")

        print("Using Python variable in PostgreSQL select Query")
        cursor = connection.cursor()
        postgreSQL_select_Query = sql_query

        cursor.execute(postgreSQL_select_Query)
        bd_records = cursor.fetchall()
        for row in bd_records:
            i=1

    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed \n")
    try:
       
       out_query=row[0]

    except (Exception, psycopg2.Error) as error:
       out_query="ERROR"

    return out_query

def date_to_milis(date_string):

    #convert date to timestamp
    obj_date = datetime.datetime.strptime(date_string,"%d/%m/%Y %H:%M:%S")

    return str(math.trunc(obj_date.timestamp() * 1000))

#veo si ha pasado un saco en 20 min

end_date = datetime.datetime.now()
str_end_date=end_date.strftime("%d/%m/%Y %H:%M:%S")
print(str_end_date)
begin_date = end_date  - datetime.timedelta(seconds=1800)
str_begin_date=begin_date.strftime("%d/%m/%Y %H:%M:%S")
print(str_begin_date)



sql_str_det="SELECT ts FROM ts_kv_latest WHERE ts >= " + date_to_milis(str_begin_date)+" AND ts <= " + date_to_milis(str_end_date) 

print(sql_str_det)
result_det=str(getDB(sql_str_det))
print(result_det)

