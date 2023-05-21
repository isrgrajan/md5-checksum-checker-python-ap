# Full name: md5 Checksum Checker Python API 
# Short name: md5-checksum-checker-python-ap 
# Summary page: https://openforge.gov.in/projects/md5-checksum-checker-python-ap
# Version: 1.0
# Author: Isrg Rajan
# Company: PranjaBytes

def calculate_md5(file_path):
    try:
        import hashlib

        with open(file_path, "rb") as file:
            md5_hash = hashlib.md5()
            for chunk in iter(lambda: file.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except ImportError:
        print("Error: hashlib module is not available.")
