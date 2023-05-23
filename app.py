from flask import Flask, render_template, request, redirect
from helper.mega import download_file_from_mega


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    files = download_file_from_mega(url)
    download_link = files[0]  # Assuming there's only one file
    return jsonify(download_link=download_link)

if __name__ == '__main__':
    app.run(debug=True)
