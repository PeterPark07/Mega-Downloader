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
    # Provide the download link to the user
    return render_template('download.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
