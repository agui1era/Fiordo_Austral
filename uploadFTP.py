import ftplib
import os
import glob

FTP_HOST = "igromi.com"
FTP_USER = "igromi"
FTP_PASS = "diccionarioAvanza12"

folder_path =r"C:\Users\Desktop\Desktop\Fiordo_Austral"

ffolder_path = r'path where your files are located'
file_type = r'\*.xlsx'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)

print(max_file)

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"


# local file name you want to upload
filename = max_file
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR ultimo.xlsx", file)