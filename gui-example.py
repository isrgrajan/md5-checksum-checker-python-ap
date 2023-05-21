# Full name: md5 Checksum Checker Python API 
# Short name: md5-checksum-checker-python-ap 
# Summary page: https://openforge.gov.in/projects/md5-checksum-checker-python-ap
# Version: 1.0
# Author: Isrg Rajan
# Company: PranjaBytes
from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)

def calculate_md5(file_path):
    with open(file_path, "rb") as file:
        md5_hash = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

@app.route("/md5", methods=["POST"])
def get_md5_checksum():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    md5_checksum = calculate_md5(file)
    return jsonify({"md5_checksum": md5_checksum})

if __name__ == "__main__":
    app.run()
