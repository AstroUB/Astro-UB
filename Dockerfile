# base image
FROM python:3.9-slim

# to look cool
ENV DEBIAN_FRONTEND=noninteractive

# base directory
RUN mkdir app
WORKDIR /app/

# upstream
RUN apt update && apt upgrade -y

# apt dependencies
RUN apt install --no-install-recommends -y \
    git bash ffmpeg mediainfo gcc wget \
    python3-dev procps neofetch make curl \
    zip unzip jq pv libel1 linux-headers-amd64 \
    python3-lxml postgresql musl musl-dev \
    postgresql-client

# update pip and install requirements
COPY . .
RUN pip3 install -U pip \
    && pip3 install --no-cache-dir -r requirements.txt

# cleanup, if needed
RUN apt autoremove --purge

# initialise app
CMD [ "python3", "-m", "reboot.py" ]
