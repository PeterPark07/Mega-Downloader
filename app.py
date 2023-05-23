from flask import Flask, render_template, request, send_file
from helper.mega import download_file_from_mega


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    files = download_file_from_mega(url)
    file_path = files[0]  # Assuming there's only one file
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
