import ftplib
import zipfile
import os
import time
import tkinter as tk
from tkinter import ttk

# Define FTP connection parameters
hostname = '192.168.1.111'
user = 'raushan'
password = 'raushan007'
port = 21
zip_folder = r"E:\seleniumtesting\uploader\upload"

class FTPClient:
    def __init__(self, root):
        self.root = root
        self.root.title("FTP Client")
        self.root.geometry("400x300")

        self.progress = ttk.Progressbar(
            self.root, orient="horizontal", length=200, mode="determinate")
        self.progress.pack()
        self.progress["value"] = 0

        self.upload_button = tk.Button(
            self.root, text="Upload Files", command=self.upload)
        self.upload_button.pack()

    def upload(self):
        ftp = ftplib.FTP()
        ftp.connect(hostname, port)
        ftp.login(user, password)

        files = [f for f in os.listdir(zip_folder) if f.endswith('.zip')]
        if files:
            print("Uploading", len(files), "files...")
            num_files = 0
            for file in files:
                with zipfile.ZipFile(zip_folder + '/' + file, 'r') as zip_ref:
                    num_files += len(zip_ref.namelist())
            self.progress["maximum"] = num_files
            for file in files:
                temp_file = file + ".incomplete"
                os.rename(zip_folder + '/' + file, zip_folder + '/' + temp_file)
                with zipfile.ZipFile(zip_folder + '/' + temp_file, 'r') as zip_ref:
                    for i, name in enumerate(zip_ref.namelist()):
                        with zip_ref.open(name) as f:
                            ftp.storbinary('STOR ' + name, f)
                        self.progress["value"] = i + 1
                        self.root.update()
                        time.sleep(0.1)
                os.remove(zip_folder + '/' + temp_file)

        print("Uploaded files:", files)
        ftp.quit()

if __name__ == "__main__":
    root = tk.Tk()
    client = FTPClient(root)
    root.mainloop()
