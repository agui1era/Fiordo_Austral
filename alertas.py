import psycopg2
import smtplib, ssl
import datetime
import math 
from pushbullet import Pushbullet

def getDB(sql_query):
    try:       
        connection = psycopg2.connect(user = "postgres",
                                        password = "imagina12",
                                        host = "iot.igromi.com",
                                        port = "5432",
                                        database = "thingsboard")
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
    try:
       
       out_query=row[0]

    except (Exception, psycopg2.Error) as error:
       out_query="ERROR"

    return out_query

def date_to_milis(date_string):

    #convert date to timestamp
    obj_date = datetime.datetime.strptime(date_string,"%d/%m/%Y %H:%M:%S")

    return str(math.trunc(obj_date.timestamp() * 1000))

end_date = datetime.datetime.now()
str_end_date=end_date.strftime("%d/%m/%Y %H:%M:%S")
print(str_end_date)
begin_date = end_date  - datetime.timedelta(hours=3)
str_begin_date=begin_date.strftime("%d/%m/%Y %H:%M:%S")
print(str_begin_date)

sql_str_det="SELECT ts FROM ts_kv WHERE ts >= " + date_to_milis(str_begin_date)+" AND ts <= " + date_to_milis(str_end_date)+ "AND key=74" 

print(sql_str_det)
result_det=str(getDB(sql_str_det))
print(result_det)


if (result_det == 'ERROR'):
    
   pb = Pushbullet('o.JQvSJjtVI1orpwzMOG4uG5ocdGFEvXoN')
   push = pb.push_note('Alerta','Problema con carga de planilla Fiordo Austral')

   pb = Pushbullet('o.QZXL7gik1bSbYyHMaQzNl9QMmfMB4GNa')
   push = pb.push_note('Alerta','Problema con carga de planilla Fiordo Austral')
