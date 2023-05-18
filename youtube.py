from flask import Flask, render_template, request, send_file, url_for
import os
import pytube
import moviepy
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from pytube import YouTube
from moviepy.editor import *

from werkzeug.middleware.proxy_fix import ProxyFix


if "MP4PATH" in os.environ:
    mp4path = str(os.environ['MP4PATH'])
else:
    mp4path = "./mp4"

if 'MP3PATH' in os.environ:
    mp3path = str(os.environ['MP3PATH'])
else:
    mp3path = "./mp3"

def checkurl(url):
    if "https://www.youtube.com" in str(url):
        return True
    else:
        return False

app = Flask(__name__)

if os.path.exists(mp3path):
    pass
else:
    os.mkdir(mp3path)

print(Flask(__name__))

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route('/test')
def test():
    return list(request.headers)

@app.route('/')
def signup_form():

    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    cpath=request.headers.get('X-Script-Name')
    url = request.args.get('url')

    if not checkurl(url):
    
        return render_template('signup.html')
    
    filename = request.args.get('filename')
    delete = request.args.get('delete')
    giveback= request.args.get('giveback')
    
    def DownLoadStream(url,filename):
    
        try:
            video = YouTube(str(url))
            video_streams = video.streams.filter(file_extension='mp4').get_highest_resolution()
            video_streams.download(filename = str(filename + ".mp4"), output_path = mp4path)
        
        except: 
            print("Hiba",dstname)
    
    def audioconvert(filename):
        videoclip = VideoFileClip(str(mp4path + "/" + filename + ".mp4"))
        audioclip = videoclip.audio
        audioclip.write_audiofile(str(mp3path + filename + ".mp3"))

    DownLoadStream(url,filename)
    
    audioconvert(filename)
    print(giveback)
    if os.path.isfile(mp3path + "/" + filename + ".mp3"):
        if giveback == 'on':
            return send_file(mp3path + "/" + filename + ".mp3")
        else:
            pass
        
        if delete == 'on':
            os.remove(mp4path + "/" + filename + ".mp4")
    
        else:
                pass
        return render_template('/signup.html')


if __name__ == '__main__':
    app.run()
