import os
import subprocess

output_dir = 'E:\\seleniumtesting\\uploader\\Primary_Incomming'

args = [
    'py',
    '-m',
    'pynetdicom',
    'storescp',
    '4006',
    '-aet',
    'ICARESCP',
    '-od',
    output_dir,
]

subprocess.run(args)
