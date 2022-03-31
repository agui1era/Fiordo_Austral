
import os
import datetime
import math
import psycopg2
from dateutil.relativedelta import relativedelta

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
       out_query=0

    return out_query

def date_to_milis(date_string):

    #convert date to timestamp
    obj_date = datetime.datetime.strptime(date_string,"%d/%m/%Y %H:%M:%S")

    return str(math.trunc(obj_date.timestamp() * 1000))


for i in range(2,13):

    date_now = datetime.datetime.now()

    if i == 2:
        
        str_date_now=date_now.strftime("28/"+str(i)+"/%Y 23:59:59")
        str_date_ant=date_now.strftime("30/"+str(i-1)+"/%Y 23:59:59")
    if i == 3:
        
        str_date_now=date_now.strftime("30/"+str(i)+"/%Y 23:59:59")
        str_date_ant=date_now.strftime("28/"+str(i-1)+"/%Y 23:59:59")
  
    if i > 3:
   
        str_date_now=date_now.strftime("30/"+str(i)+"/%Y 23:59:59")
        str_date_ant=date_now.strftime("30/"+str(i-1)+"/%Y 23:59:59")

    print("Mes número: "+str(i))
    print("Día final: "+str_date_now)
    print("Día inicial: "+str_date_ant)


    sql_str_det="SELECT long_v FROM ts_kv WHERE ts <= "+ date_to_milis(str_date_ant)+ " AND key=74 " + "AND  entity_id='d37982b0-c220-11eb-a61d-e9bafc595a10' ORDER BY ts DESC LIMIT 1"
    ENERGIA_ANT_SE300=getDB(sql_str_det)
    print('Energia anterior mes SE300 '+str(ENERGIA_ANT_SE300))

    sql_str_det="SELECT long_v FROM ts_kv WHERE ts <= "+ date_to_milis(str_date_now)+ " AND key=74 " + "AND  entity_id='d37982b0-c220-11eb-a61d-e9bafc595a10' ORDER BY ts DESC LIMIT 1"
    ENERGIA_SE300=getDB(sql_str_det)
    print('Energia mes SE300 '+str(ENERGIA_SE300))
    
    sql_str_det="SELECT long_v FROM ts_kv WHERE ts <= "+ date_to_milis(str_date_ant)+ " AND key=74 " + "AND  entity_id='c2375400-c220-11eb-a61d-e9bafc595a10' ORDER BY ts DESC LIMIT 1"
    ENERGIA_ANT_SE500=getDB(sql_str_det)
    print('Energia mes anterior SE500 '+str(ENERGIA_ANT_SE500))

    sql_str_det="SELECT long_v FROM ts_kv WHERE ts <= "+ date_to_milis(str_date_now)+ " AND key=74 " + "AND  entity_id='c2375400-c220-11eb-a61d-e9bafc595a10' ORDER BY ts DESC LIMIT 1"
    ENERGIA_SE500=getDB(sql_str_det)
    print('Energia mes  SE500 '+str(ENERGIA_SE500))

    sql_str_det="SELECT long_v FROM ts_kv WHERE ts <= "+ date_to_milis(str_date_ant)+ " AND key=74 " + "AND  entity_id='b3a243f0-c220-11eb-a61d-e9bafc595a10' ORDER BY ts DESC LIMIT 1"
    ENERGIA_ANT_SE1000=getDB(sql_str_det)
    print('Energia mes anterior SE1000 '+str(ENERGIA_ANT_SE1000))

    sql_str_det="SELECT long_v FROM ts_kv WHERE ts <= "+ date_to_milis(str_date_now)+ " AND key=74 " + "AND  entity_id='b3a243f0-c220-11eb-a61d-e9bafc595a10' ORDER BY ts DESC LIMIT 1"
    ENERGIA_SE1000=getDB(sql_str_det)
    print('Energia mes  SE1000 '+str(ENERGIA_SE1000))
    
    print("------------------------------------------------------------")
    print("Energía  SE300 mes "+str(i)+"  "+str((ENERGIA_SE300-ENERGIA_ANT_SE300)))
    os.system('curl -v -X POST -d "{\"SE300_'+str(i)+'\":'+str((ENERGIA_SE300-ENERGIA_ANT_SE300))+'}" iot.igromi.com:8080/api/v1/fiordo_imagina12/telemetry --header "Content-Type:application/json"')
    print("Energía  SE500 mes "+str(i)+"  "+str((ENERGIA_SE500-ENERGIA_ANT_SE500)))
    os.system('curl -v -X POST -d "{\"SE500_'+str(i)+'\":'+str((ENERGIA_SE500-ENERGIA_ANT_SE500))+'}" iot.igromi.com:8080/api/v1/fiordo_imagina12/telemetry --header "Content-Type:application/json"')
    print("Energía SE1000 mes "+str(i)+"  "+str((ENERGIA_SE1000-ENERGIA_ANT_SE1000)))
    os.system('curl -v -X POST -d "{\"SE1000_'+str(i)+'\":'+str((ENERGIA_SE1000-ENERGIA_ANT_SE1000))+'}" iot.igromi.com:8080/api/v1/fiordo_imagina12/telemetry --header "Content-Type:application/json"')
    print("------------------------------------------------------------")