
import os
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

wb = load_workbook('Tem42661.xlsx')
print(wb.sheetnames)
sheet = wb['||Hoja11']

deltaFila=0
Columna=1

FECHA=sheet.cell(row=4+deltaFila, column=Columna).value
for token in token_dispositivos:

    POT=sheet.cell(row=4+deltaFila, column=1+Columna).value
    IA=sheet.cell(row=4+deltaFila, column=2+Columna).value
    IB=sheet.cell(row=4+deltaFila, column=3+Columna).value
    IC=sheet.cell(row=4+deltaFila, column=4+Columna).value
    VAB=sheet.cell(row=4+deltaFila, column=5+Columna).value
    VAC=sheet.cell(row=4+deltaFila, column=6+Columna).value
    VBC=sheet.cell(row=4+deltaFila, column=7+Columna).value
    
    print('------------------------------------------------------')
    print('FECHA: '+str(FECHA))
    print('POT: '+str(POT))
    print('IA: '+str(IA))
    print('IB: '+str(IB))
    print('IC: '+str(IC))
    print('VAB: '+str(VAB))
    print('VAC: '+str(VAC))
    print('VBC: '+str(VBC))
    print('COLUMNA: '+str(Columna))
    print('------------------------------------------------------')

    Columna=Columna+7

    os.system('curl -v -X POST -d "{\"POT\":'+str(POT)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
    os.system('curl -v -X POST -d "{\"IA\":'+str(IA)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
    os.system('curl -v -X POST -d "{\"IB\":'+str(IB)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
    os.system('curl -v -X POST -d "{\"IC\":'+str(IC)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
    os.system('curl -v -X POST -d "{\"VAB\":'+str(VAB)+'}" iot.igromi.com:8080/api/v1/+'+token+'/telemetry --header "Content-Type:application/json"')
    os.system('curl -v -X POST -d "{\"VAC\":'+str(VAC)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
    os.system('curl -v -X POST -d "{\"VBC\":'+str(VBC)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')




