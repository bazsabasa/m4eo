FROM python
WORKDIR /opt/
RUN apt-get update && apt-get install -y ffmpeg
COPY requirements.txt ./
COPY templates ./templates
COPY static ./static
COPY wsgi.py ./
COPY youtube.py ./
COPY .env ./
COPY startup.sh ./
#RUN apt-get update && apt-get install -y python3 ffmpeg && apt-get install -y python3-pip && python3 -m pip install --upgrade pip && pip install -r /opt/requirements.txt && mkdir /opt/mp4 /opt/mp3 && . /opt/.env
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /opt/requirements.txt --no-cache-dir
EXPOSE 8080
#ENTRYPOINT SCRIPT_NAME=/music FLASK_APP=/opt/wsgi.py gunicorn --workers 4 --bind=0.0.0.0:8080 wsgi:app
CMD ["/bin/bash","./startup.sh" ]