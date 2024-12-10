from flask import Flask, request

from download import download_youtube_video
from upload import upload_file

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About'


@app.route('/youtube/download', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return 'URL is required', 400

    path = download_youtube_video(url)
    url = upload_file('./' + path)

    return url