import zipfile
import os
import time

def zip_dicom_folder(compression_level=9, files_per_zip=100):
    input_folder = "E:\\seleniumtesting\\uploader\\Primary_Incomming"
    output_folder = "E:\\seleniumtesting\\uploader\\upload"
    
    count = 0
    files = [f for f in os.listdir(input_folder) if f.endswith('.dcm')]
    if len(files) == 0:
        print(f"No DICOM files found in folder '{input_folder}'.")
        return
    
    for i in range(0, len(files), files_per_zip):
       batch_files = files[i:i+files_per_zip]
       output_path = os.path.join(output_folder, f"{batch_files[0][:-4]}_{i//files_per_zip}.zip")
       with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=compression_level) as myzip:
        for filename in batch_files:
            input_path = os.path.join(input_folder, filename)
            myzip.write(input_path, os.path.basename(input_path))
            os.remove(input_path)
    count += len(batch_files)
    print(f"Successfully zipped {count} DICOM files in folder '{input_folder}' to '{output_folder}' and deleted the original files.")

while True:
    zip_dicom_folder()
    input_folder = "E:\\seleniumtesting\\uploader\\Primary_Incomming"
    files = [f for f in os.listdir(input_folder) if f.endswith('.dcm')]
    if len(files) == 0:
        time.sleep(30) # wait for 1 hour (3600 seconds) if there are no files in the folder
