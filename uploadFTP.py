import ftplib

FTP_HOST = "igromi.com"
FTP_USER = "igromi"
FTP_PASS = "diccionarioAvanza12"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

# local file name you want to upload
filename = r"C:\Users\matias.valdes\Desktop\Registros\ultimo(02).xlsx"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR ultimo.xlsx", file)