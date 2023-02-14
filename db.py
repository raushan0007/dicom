import pydicom
import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect("E:\\seleniumtesting\\uploader\\db\\dicom_images.db")
cursor = conn.cursor()

# Create a table to store the information
cursor.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    patient_name TEXT,
    patient_id TEXT,
    study_description TEXT,
    series_description TEXT
)
""")

# Loop over all DICOM files in a directory
for filename in os.listdir("E:\\seleniumtesting\\uploader\\Primary_Incomming"):
    file_path = os.path.join("E:\\seleniumtesting\\uploader\\Primary_Incomming", filename)
    
    try:
        # Load the DICOM image using pydicom
        dcm = pydicom.dcmread(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        continue
    
    # Extract the relevant information
    patient_name = str(dcm.PatientName)
    patient_id = dcm.PatientID
    study_description = dcm.StudyDescription
    series_description = dcm.SeriesDescription
    
    # Insert the information into the database
    cursor.execute("""
    INSERT INTO images (filename, patient_name, patient_id, study_description, series_description)
    VALUES (?,?,?,?,?)
    """, (filename, patient_name, patient_id, study_description, series_description))

# Commit the changes and close the connection
conn.commit()
conn.close()
