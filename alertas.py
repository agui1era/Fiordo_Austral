import psycopg2
import datetime
import math
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
import smtplib
from email import encoders
from pushbullet import Pushbullet

emails=["aguileraelectro@gmail.com","barbara@igromi.com","victor.ruz@igromi.com"]
horas_alarma=12

fromaddr = "news@igromi.cl"
msg = MIMEMultipart() 
# storing the senders email address 
msg['From'] = fromaddr 
msg['Subject'] ="Error carga de datos Fiordo Austral "
body=''

s = smtplib.SMTP("mail.igromi.cl", 587) 
# start TLS for security 
s.starttls() 
# Authentication 
s.login(fromaddr, "imagina12$")

sensorName="Totales_fiordo_austral"

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
begin_date = end_date  - datetime.timedelta(hours=horas_alarma)
str_begin_date=begin_date.strftime("%d/%m/%Y %H:%M:%S")
print(str_begin_date)

sql_str_det="SELECT ts FROM ts_kv WHERE ts >= " + date_to_milis(str_begin_date)+ " AND  entity_id = (select id from device where name='"+sensorName+"') order by ts desc limit 1"

print(sql_str_det)
result_det=str(getDB(sql_str_det))
print(result_det)


if (result_det=='ERROR'):

  ################  Envio de mail ###################
  # attach the body with the msg instance 
  # attach the body with the msg instance 
  msg.attach(MIMEText(body, 'plain')) 
  # instance of MIMEBase and named as p 
  p = MIMEBase("application", "octet-stream") 
  # creates SMTP session 
  
    # Converts the Multipart msg into a string 
  text = msg.as_string() 
    # sending the mail 


pb = Pushbullet('o.i9959mzkwsEWPz7gmOa13jmK9J1fpd9E')
push = pb.push_note('Alerta','Problema con carga de planilla Fiordo Austral')

for email in emails :
    msg["To"] = email,
    s.sendmail(fromaddr,email, text)
