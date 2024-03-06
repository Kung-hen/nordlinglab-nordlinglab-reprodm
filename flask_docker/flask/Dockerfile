# select base image
FROM python:3.7


WORKDIR /app

# Copy the current directory contents into the container at app
ADD . /app

# Some useful packages
RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y upgrade

# RUN apt-get -y install build-essential \
#     && apt-get -y install libgl1-mesa-dev \
#     && apt-get -y install libglib2.0-0 \
#     && apt-get -y install ffmpeg x264 libx264-dev

# install dependency
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# run command to start uWSGI
CMD ["uwsgi", "app.ini"]