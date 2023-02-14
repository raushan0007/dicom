import ftplib
import os
import time

# Connect to the FTP server
ftp = ftplib.FTP()
import ftplib
import os

hostname = '192.168.1.111'
user = 'raushan'
password = 'raushan007'
port = 21
zip_folder = r"E:\seleniumtesting\uploader\upload"

ftp = ftplib.FTP()
ftp.connect(hostname, port)
ftp.login(user, password)

files = [f for f in os.listdir(zip_folder) if f.endswith('.zip')]

if files:
    print("Uploading", len(files), "files...")
    for file in files:
        with open(zip_folder + '/' + file, 'rb') as f:
            ftp.storbinary('STOR ' + file, f)
        os.remove(zip_folder + '/' + file)
        
print("Uploaded files:", files)
ftp.quit()

