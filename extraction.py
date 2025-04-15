import zipfile

# Path to your zip file
zip_file_path = r"C:\Users\rsuma\OneDrive\Desktop\My Project\currencyclassify\dataset.zip"
extract_to = r"C:\Users\rsuma\OneDrive\Desktop\My Project\currencyclassify\dataset"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)
