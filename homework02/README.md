# Homework 2
---
generate\_animals.py generates a json file full of 20 animal hybrids randomly generated that lists out their features: head, body, number of arms, number of legs, and number of tails. 
to run the file you will need user input of the file name to generate 
read\_animals.py prints out 1 randomly selected animal from the json file made using generate\_animals.pyIt then will choose to random parents from the list and will breed to make a child, which combines the heads and bodies of the parents and has the average number of arms and legs from the parents and the number of tails is the sum of the number of arms and legs.

---
## Downloading and Running Directly
Download the files by getting the files off of github
```
[isp02]$ wget https://raw.githubusercontent.com/keriem/kerichristian-coe332/main/homework02/generate_animals.py
[isp02]$ wget https://raw.githubusercontent.com/keriem/kerichristian-coe332/main/homework02/read_animals.py
[isp02]$ wget https://raw.githubusercontent.com/keriem/kerichristian-coe332/main/homework02/test_read_animals.py
[isp02]$ wget https://raw.githubusercontent.com/keriem/kerichristian-coe332/main/homework02/Dockerfile
```
Then make generate\_animals.py and read\_animals.py executable (and also test\_read\_animals.py if you want
```
[isp02]$ chmod +rx generate_animals.py
[isp02]$ chmod +rx read_animals.py
[isp02]$ chmod +rx test_read_animals.py
```
Then to run directly without making a container
```
[isp02]$ python3 generate_animals.py animals.json
[isp02]$ python3 read_animals.py animals.json
[isp02]$ python3 test_read_animals.py
```
## How to Build Image with Dockerfile 
The docker file already contains all the commands needed to build your image. To do so type in the following code:
```
[isp02]$ docker build -t kchristian1/homework02:1.0 .
```
Check it has been made by using docker images
```
[isp02]$ docker images
```
## How to the run the scripts in the Container
Run the containr created by the image 
```
[isp02]$ docker run --rm -it kchristian1/homework02:1.0 /bin/bash
```
The files will be in the container, run them like you would directly
```
[root@c5cf05efffdc /]# generate_animals.py animals.json
[root@c5cf05efffdc /]# read_animals.py animals.json
[root@c5cf05efffdc /]# test_read_animals.py
```
## How to run the unit test 
Leave the container and run the test\_read\_animals.py file
```
{isp02]$ python3 test_read_animals.py
```
