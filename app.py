from flask import Flask, render_template, request, send_file
from helper.mega import download_file_from_mega

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', download_status=None, download_link=None)

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    files = download_file_from_mega(url)
    file_path = files[0]  # Assuming there's only one file
    download_link = f"/download_link/{file_path}"
    return render_template('index.html', download_status='Download completed', download_link=download_link)

@app.route('/download_link/<path:file_path>')
def download_link(file_path):
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
