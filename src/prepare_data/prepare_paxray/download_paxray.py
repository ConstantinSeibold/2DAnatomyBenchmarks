import os
import zipfile
import gdown

DATASET_ROOT_PATH = os.getenv("PAXRAY_ROOT_PATH")

# Define the Google Drive file URL or ID
file_id = '19HPPhKf9TDv4sO3UV-nI3Jhi4nCv_Zyc'  # Replace with your file ID
destination = 'paxray.zip'  # Destination path for the downloaded ZIP file

# Download the file from Google Drive
gdown.download(f'https://drive.google.com/uc?id={file_id}', destination, quiet=False)

# Unzip the file
with zipfile.ZipFile(destination, 'r') as zip_ref:
    zip_ref.extractall(DATASET_ROOT_PATH)  # Destination folder for unzipped contents

# Delete the downloaded ZIP file
if os.path.exists(destination):
    os.remove(destination)
    print("ZIP file deleted.")

print("Download, extraction, and deletion completed successfully.")
