
import os
import datetime
from openpyxl import load_workbook

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
     
token_dispositivos = ['jt9DdWAvNK','HDjYvFtfZ7','WEbn35kQRk','OuvVsF0vek' ,'eo085EanGe','hmqPNgajnY','gQVSvMsyJt','5Msyx2m8Oh','eBSXNYdrl9','K2HcV0IHY6','SBslPQTJAa','UBpnpsCWB8','UpekFmGS3w']

wb = load_workbook('Data(01).xlsx')
wb.iso_dates = True
sheet = wb['||Hoja11']

Columna=1

MAX_FILAS=sheet.max_row
print('Filas totales: '+str(MAX_FILAS))

time_now = datetime.datetime.now()
begin_time = time_now  - datetime.timedelta(hours=1)

for Fila in range(MAX_FILAS+4):
    Columna=1
    Fila=Fila+1
    FECHA=sheet.cell(row=Fila+4, column=1).value
    
    print('------------------------------------------------------')
    print('TIME PLANILLA DEBE SER >: '+str(FECHA))
    print('TIME ACTUAL MENOS 1 HORA: '+str(begin_time))
    print('------------------------------------------------------')
    
    if (FECHA > begin_time) and (str(FECHA) != 'None') :  

        for token in token_dispositivos:
            
            POT=sheet.cell(row=Fila+4, column=1+Columna).value
            IA=sheet.cell(row=Fila+4, column=2+Columna).value
            IB=sheet.cell(row=Fila+4, column=3+Columna).value
            IC=sheet.cell(row=Fila+4, column=4+Columna).value
            VAB=sheet.cell(row=Fila+4, column=5+Columna).value
            VAC=sheet.cell(row=Fila+4, column=6+Columna).value
            VBC=sheet.cell(row=Fila+4, column=7+Columna).value
            
            TIMESTAMP=datetime.datetime.strptime(str(FECHA), '%Y-%m-%d %H:%M:%S').timestamp()*1000
            
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





