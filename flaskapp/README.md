# flaskapp - deployment of basic hello world flask application in a docker container 
- Create app.py with hello world code 
- Create a docker file with base image, work directory, copy path and run commands required to run flask application 
- Create a docker image using docker build 
  ```
  docker build -t <tagname> .
  ```
- Create a container out of the image and expose on port 5000 
  ```
  docker run -d -p 5000:5000 <image name>
  ```