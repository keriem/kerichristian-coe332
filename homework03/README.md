# Homework 3
---
app.py is the python file which continues the routes to access data about the moreau animals. The Dockerfile has instructions when creating the docker image and container. The data_file.json is the data file with 100 moreau animals which the container will access through flask. The consumer_requestor.py file is a consumer which accesses and consumes data from another student's url. The requirements.txt file tells the docker which version of Flask is needed. 
---
## Downloading Files
Download the files by getting the files off of github
```
[isp02]$ wget 
[isp02]$ wget 
[isp02]$ wget 
[isp02]$ wget 
```
## How to Build Image with Dockerfile 
The docker file already contains all the commands needed to build your image. To do so type in the following code:
```
[isp02]$ docker build -t kchristian/homework03:1.0 .
```
Check it has been made by using docker images
```
[isp02]$ docker images
```
## How to the run the Container and use the urls
Run the containr created by the image 
```
[isp02]$ docker run --name "kchristian-hw3-flask" -d -p 5006:5000 kchristian1/homework03:1.0
```
Now you should be able to curl into the flask using the container that is running. Check it using the 
```
[isp02]$ curl localhost:5006/helloworld
```
To access all animals use this route
```
[isp02]$ curl localhost:5006/animals
```
To access animals with a specific head use the url localhost:5006/animals/head?name= '<nameofhead>'. Here are some examples.
```
# This will return all of the animals with a snake head
[isp02]$ curl localhost:5006/animals/head?name='snake' 
# This will return all of the animals with a bunny head
[isp02]$ curl localhost:5006/animals/head?name='bunny'
```
To access animals with a certain number of legs use the url localhost:5006/animals/legs?number=<numberoflegs>. Here are some examples.
```
# This will return all animals with 6 legs
[isp02]$ curl localhost:5006/animals/legs?number=6
# This will return all animals with 12 legs
[isp02]$ curl localhost:5006/animals/legs?number=12
```
To access a certain number of animals use the url localhost:5006/animals/number?top=<number> Here is an example.
```
# This will return the top 50 animals
[isp02]$ curl localhost:5006/animals/number?top=50
```
## How to run the Consumer
The consumer file will be accessing Zoe Watson's urls. 

