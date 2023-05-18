# m4eo
Music for every one
* docker run -d -p 0.0.0.0:8080:8080/tcp --env MP4PATH=/opt/music/mp4/ --env CPATH=/music --env MP3PATH=/opt/music/mp3/ --mount type=bind,source="/mnt/nas/P2P/complete/zene/",target=/opt/music youtube
