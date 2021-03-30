# Homework 4 Midterm
---
app.py is the python file which continues the routes to access data about the moreau animals. The Dockerfile has instructions when creating the docker image and container. The data_file.json is the data file with 100 moreau animals but is not used in this assignment. The requirements.txt file tells the docker which version of Flask is needed. The docker-compose.yml file contains instructions when building both containers. The redis.conf is a configuration file for the redis container. 
---
## Downloading Files
Download the files by downloading the repository off github and navigate to the correct folder
```
[isp02]$ git clone https://github.com/keriem/kerichristian-coe332
[isp02]$ cd kerichristian-coe332
[isp02]$ cd homework04
[isp02]$ cd redis-docker
```
## How to Build Image with Dockerfile 
The docker-compose.yml file already contains all the commands needed to build your images. To do so type in the following code:
```
[isp02]$ docker-compose -p kchristi build
```
Check it has been made by using docker images
```
[isp02]$ docker ps -a
```
## How to the run the Container and use the urls
Run the containers created by the images 
```
[isp02]$ docker-compose -p kchristi up
```
Now you should be able to curl into the flask using the container that is running. Check it using the 
```
[isp02]$ curl localhost:5006/helloworld
```
First set up the redis data base with the reset url
```
[isp02]$ curl localhost:5006/reset
```
To access all animals use this route
```
[isp02]$ curl localhost:5006/animals
```
To query a range of dates use the url "localhost:5006/animals/dates?start='\<\%Y-\%M-\%D_\%H:\%M:\%S.\%f\>'end=?'\<\%Y-\%M-\%D_\%H:\%M:\%S.\%f\>'" Here are some examples:
```
[isp02]$ curl "localhost:5006/animals/dates?start='2021-03-30_04:22:08.394410'&end='2021-03-30_04:22:08.395919'"
```
It will return all animals within that date range. If there are not any animals within that date range it will return []

To select a particular creature by its unique identifier use the url localhost:5006/animals/uid?value='\<uuid\>' Here is an example:
```
[isp02]$ curl localhost:5006/animals/uid?value='27952028-4f2e-4120-97c4-78f22539ac6a'
```
To edit a particular creature by passing the UUID and providing updated “stats” use the url "localhost:5006/animals/edit?uid='\<uuid\>'&head='\<name\>'&body='\<name\>'&arms='\<number\>'&legs='\<number\>'&tails='\<number\>'". Here is an example:
```
[isp02]$ curl "localhost:5006/animals/edit?uid='27952028-4f2e-4120-97c4-78f22539ac6a'&head='bunny'&body='dog-cat'&arms='2'&legs='4'&tails='6'"
```
It will return the updated animal

To delete a selection of animals by a date rangees use the url "localhost:5006/animals/delete/dates?start='\<\%Y-\%M-\%D_\%H:\%M:\%S.\%f\>'end=?'\<\%Y-\%M-\%D_\%H:\%M:\%S.\%f\>'" Here is an example:
```
[isp02]$  curl "localhost:5006/animals/delete/dates?start='2021-03-30_04:22:08.394410'&end='2021-03-30_04:22:08.395919'"
```
It will return the deleted animals

To get the average number of legs per animal use the url localhost:5006/animals/averagelegs. 
```
[isp02]$ curl localhost:5006/animals/averagelegs
```
To get the total number of animals use the url localhost:5006/animals/total
```
[isp02]$ curl localhost:5006/animals/total
```

**Below are other routes left over from Homework03:**

To access animals with a specific head use the url localhost:5006/animals/head?name= '\<nameofhead\>'. Here are some examples.
```
# This will return all of the animals with a snake head
[isp02]$ curl localhost:5006/animals/head?name='snake' 
# This will return all of the animals with a bunny head
[isp02]$ curl localhost:5006/animals/head?name='bunny'
```
To access animals with a certain number of legs use the url localhost:5006/animals/legs?number=\<numberoflegs\>. Here are some examples.
```
# This will return all animals with 6 legs
[isp02]$ curl localhost:5006/animals/legs?number=6
# This will return all animals with 12 legs
[isp02]$ curl localhost:5006/animals/legs?number=12
```
To access a certain number of animals use the url localhost:5006/animals/number?top=\<number\> Here is an example.
```
# This will return the top 50 animals
[isp02]$ curl localhost:5006/animals/number?top=50
```
To create a random animal use the url localhost:5006/animals/createRandom
```
[isp02]$ curl localhost:5006/animals/createRandom
```
## Closing the Containers
Don't forget to close the containers once you are done. I usually just use Ctrl-Z

