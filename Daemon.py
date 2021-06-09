
import os
import datetime
from openpyxl import load_workbook
from ftplib import FTP

#S/E 300 KVA              jt9DdWAvNK
#Desodorizado Omega 3     HDjYvFtfZ7
#WINT. VEGETALES          WEbn35kQRk
#S/E 500                  OuvVsF0vek
#REF. VEGETALES           eo085EanGe
#CALDERA                  hmqPNgajnY
#DESO. VEGETALES          gQVSvMsyJt
#REF. OMEGA 3             5Msyx2m8Oh
#S/E 1000                 eBSXNYdrl9
#CHI. TRIOMAX             K2HcV0IHY6
#PRENSAS                  SBslPQTJAa
#Extracción               UBpnpsCWB8
#TRIOMAX                  UpekFmGS3w

file='Data.xlsx'
ftp = FTP('igromi.com')
ftp.login('igromi','diccionarioAvanza12')

ftp.retrbinary("RETR /iot/Data(01).xlsx" ,open( file, 'wb').write)

ftp.quit()

token_diff='jzEVcu4ocZ'

token_dispositivos = ['jt9DdWAvNK','HDjYvFtfZ7','WEbn35kQRk','OuvVsF0vek' ,'eo085EanGe','hmqPNgajnY','gQVSvMsyJt','5Msyx2m8Oh','eBSXNYdrl9','K2HcV0IHY6','SBslPQTJAa','UBpnpsCWB8','UpekFmGS3w']

wb = load_workbook(file)
wb.iso_dates = True
sheet = wb['||Hoja11']

Columna=1

MAX_FILAS=sheet.max_row
print('Filas totales: '+str(MAX_FILAS))

time_now = datetime.datetime.now()
begin_time = time_now  - datetime.timedelta(hours=12)

for Fila in range(MAX_FILAS+4):
    Columna=1
    Fila=Fila+1
    FECHA=sheet.cell(row=Fila+4, column=1).value
    
    print('------------------------------------------------------')
    print('HORA PLANILLA : '+str(FECHA))
    print(' > HORA ACTUAL MENOS DELTA HORAS: '+str(begin_time))
    print('------------------------------------------------------')
    
    try:     
        if (FECHA > begin_time) :  

            TIMESTAMP=datetime.datetime.strptime(str(FECHA), '%Y-%m-%d %H:%M:%S').timestamp()*1000
            SE300=sheet.cell(row=Fila+4, column=2).value
            DESO_OMEGA3=sheet.cell(row=Fila+4, column=9).value
            WINT_VEGETALES=sheet.cell(row=Fila+4, column=16).value
            SE500=sheet.cell(row=Fila+4, column=23).value
            REF_VEGETALES=sheet.cell(row=Fila+4, column=30).value
            CALDERA=sheet.cell(row=Fila+4, column=37).value
            DESO_VEGETALES=sheet.cell(row=Fila+4, column=44).value
            REF_OMEGA3=sheet.cell(row=Fila+4, column=51).value
            SE1000=sheet.cell(row=Fila+4, column=58).value
            PRENSAS=sheet.cell(row=Fila+4, column=65).value
            EXTRACCION=sheet.cell(row=Fila+4, column=72).value
            TRIOMAX=sheet.cell(row=Fila+4, column=79).value
            CHI_TRIOMAX=sheet.cell(row=Fila+4, column=86).value

            DIFF_SE300 = SE300-DESO_OMEGA3-WINT_VEGETALES
            DIFF_SE500 = SE500-REF_VEGETALES-CALDERA-DESO_VEGETALES-REF_OMEGA3
            DIFF_SE1000= SE1000-PRENSAS-EXTRACCION-TRIOMAX-CHI_TRIOMAX

            os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"DIFF_SE300\":'+str(DIFF_SE300)+'}}" iot.igromi.com:8080/api/v1/'+token_diff+'/telemetry --header "Content-Type:application/json"')
            os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"DIFF_SE500\":'+str(DIFF_SE500)+'}}" iot.igromi.com:8080/api/v1/'+token_diff+'/telemetry --header "Content-Type:application/json"')
            os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"DIFF_SE1000\":'+str(DIFF_SE1000)+'}}" iot.igromi.com:8080/api/v1/'+token_diff+'/telemetry --header "Content-Type:application/json"')
                

            for token in token_dispositivos:
                
                POT=sheet.cell(row=Fila+4, column=1+Columna).value
                IA=sheet.cell(row=Fila+4, column=2+Columna).value
                IB=sheet.cell(row=Fila+4, column=3+Columna).value
                IC=sheet.cell(row=Fila+4, column=4+Columna).value
                VAB=sheet.cell(row=Fila+4, column=5+Columna).value
                VAC=sheet.cell(row=Fila+4, column=6+Columna).value
                VBC=sheet.cell(row=Fila+4, column=7+Columna).value
                  
                print('------------------------------------------------------')
                print('FILA:' +str(Fila+4))
                print('FECHA: '+str(FECHA))
                print('POT: '+str(POT))
                print('IA: '+str(IA))
                print('IB: '+str(IB))
                print('IC: '+str(IC))
                print('VAB: '+str(VAB))
                print('VAC: '+str(VAC))
                print('VBC: '+str(VBC))
                print('------------------------------------------------------')

                Columna=Columna+7

                os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"POT\":'+str(POT)+'}}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
                os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"IA\":'+str(IA)+'}}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
                os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"IB\":'+str(IB)+'}}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
                os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"IC\":'+str(IC)+'}}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
                os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"VAB\":'+str(VAB)+'}}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
                os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"VAC\":'+str(VAC)+'}}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
                os.system('curl -v -X POST -d "{\"ts\":'+str(TIMESTAMP)+',\"values\":{\"VBC\":'+str(VBC)+'}}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')

    except:
        print('error')