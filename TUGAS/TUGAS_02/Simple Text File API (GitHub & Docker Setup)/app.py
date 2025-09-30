from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Path to your txt files folder
FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")

@app.route("/files/<filename>")
def serve_file(filename):
    try:
        return send_from_directory(FILES_DIR, filename, as_attachment=False)
    except FileNotFoundError:
        abort(404, description="File not found")

@app.route("/")
def home():
    return {
        "message": "Welcome to the Flask File API!",
        "endpoints": [
            "/files/10kb.txt",
            "/files/100kb.txt",
            "/files/1mb.txt",
            "/files/5mb.txt",
            "/files/10mb.txt"
        ]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
