
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import time
import smtplib 


fromaddr = "notificaciones@igromi.com"
# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the subject 
msg['Subject'] = "Alerta de carga de datos"

# string to store the body of the mail 
body = "No se han registado datos en las pasadas 3 horas."

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# creates SMTP session 
s = smtplib.SMTP('smtp.zoho.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, "imagina12") 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
msg['To'] = "aguileraelectro@gmail.com",
s.sendmail(fromaddr,"aguileraelectro@gmail.com", text)

time.sleep(10)

msg['To'] = "victor.ruz@igromi.com"
s.sendmail(fromaddr, "victor.ruz@igromi.com", text) 

time.sleep(10)

# terminating the session 
s.quit() 
