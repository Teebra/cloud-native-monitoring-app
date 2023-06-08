From python:3.9-slim-buster
#Base image python:3.9-slim-buster

WORKDIR /app
# Establish a working folder

COPY requirements.txt .
# copy requirements.txt to app directory

RUN pip install --no-cache-dir -r requirements.txt
#running installation

COPY . .
# copy everything in the directory to the app directory

ENV FLASK_RUN_HOST=0.0.0.0
# environment variable

EXPOSE 5000
#container will run port 5000

CMD ["flask", "run"]
#command [executable, parameter, ...] comannd to start
#docker build -t my-flask-app .
#docker build: This is the command to build a Docker image.
#-t my-flask-app: The -t flag is used to tag the Docker image with a name. In this case, the image will be tagged as my-flask-app.
#.: The period (.) at the end specifies the build context. It tells Docker to look for a Dockerfile and other necessary files in the current directory.
