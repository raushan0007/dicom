import tkinter as tk
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("E:\\seleniumtesting\\uploader\\dicom_images.db")
cursor = conn.cursor()

# Fetch all patient names from the database
cursor.execute("SELECT DISTINCT patient_name FROM images")
patient_names = [record[0] for record in cursor.fetchall()]

# Create a GUI window
root = tk.Tk()
root.title("DICOM Details")

# Add a label to display the patient name
patient_name_label = tk.Label(root, text="Patient Name:")
patient_name_label.grid(row=0, column=0)

# Add a dropdown menu to select the patient
patient_name_var = tk.StringVar()
patient_name_var.set(patient_names[0])
patient_name_menu = tk.OptionMenu(root, patient_name_var, *patient_names)
patient_name_menu.grid(row=0, column=1)

# Add labels to display the details
filename_label = tk.Label(root, text="Filename:")
filename_label.grid(row=1, column=0)
patient_id_label = tk.Label(root, text="Patient ID:")
patient_id_label.grid(row=2, column=0)
study_description_label = tk.Label(root, text="Study Description:")
study_description_label.grid(row=3, column=0)
series_description_label = tk.Label(root, text="Series Description:")
series_description_label.grid(row=4, column=0)

# Function to update the details when the patient name is changed
def update_details(*args):
    patient_name = patient_name_var.get()
    
    # Fetch the details for the selected patient
    cursor.execute("SELECT * FROM images WHERE patient_name=?", (patient_name,))
    record = cursor.fetchone()
    
    # Update the labels
    filename_label["text"] = "Filename: " + record[1]
    patient_id_label["text"] = "Patient ID: " + record[3]
    study_description_label["text"] = "Study Description: " + record[4]
    series_description_label["text"] = "Series Description: " + record[5]

# Call the update_details function whenever the patient name is changed
patient_name_var.trace("w", update_details)

# Start the GUI event loop
root.mainloop()

# Close the connection to the database
conn.close()
