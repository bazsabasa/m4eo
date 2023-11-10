# m4eo
Music for everyone
* sudo docker build . --tag downloader:latest
* docker run -d -p 0.0.0.0:8080:8080/tcp --env MP4PATH=/opt/music/mp4 --env CPATH={context path of your proxy} --env MP3PATH=/opt/music/mp3 --mount type=bind,source="{Target folder on your file system}",target=/opt/music downloader
