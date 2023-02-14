import pydicom
import numpy as np
from PIL import Image

def compress_dicom_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.dcm'):
            filepath = os.path.join(input_folder, filename)
            ds = pydicom.dcmread(filepath)

            image = ds.pixel_array
            image = (image - np.min(image)) / (np.max(image) - np.min(image))
            image = (image * 255).astype(np.uint8)

            jpeg_data = Image.fromarray(image).convert("L")
            jpeg_data = jpeg_data.tobytes()

            ds.PixelData = jpeg_data
            ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

            output_filepath = os.path.join(output_folder, filename)
            ds.save_as(output_filepath)

input_folder = "E:\\seleniumtesting\\uploader\\Primary_Incomming"
output_folder = "E:\\seleniumtesting\\uploader\\output"
compress_dicom_files(input_folder, output_folder)
