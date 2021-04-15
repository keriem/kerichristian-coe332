# Homework 6
---
kchristi-test-redis-deployment.yml, kchristi-test-redis-pvc.yml and kchristi-test-redis-service.yml are the files used to set up redis for the kubernetes. kchristi-test-flask-deployment.yml and kchristi-test-flask-service.yml are the files for using the docker image from the midterm that uses flask. deployment-python-debug.yml is the file to open up an interactive ubuntu using python to debug
---
## STEP 1
Here is the command to create the persistent volume claim
```
[isp02]$ kubectl apply -f kchristi-test-redis-pvc.yml
persistentvolumeclaim/kchristi-test-redis-pvc-data created
```
## STEP 2 
This is the command to create the deployment
```
[isp02]$ kubectl apply -f kchristi-test-redis-deployment.yml
deployment.apps/kchristi-test-redis-deployment created
```
## STEP 3
This is the command to create the service 
```
[isp02]$ kubectl apply -f kchristi-test-redis-service.yml
service/kchristi-test-redis-service created
```
To test it out we need to use the python debug deployment
```
[isp02]$ kubectl apply -f deployment-python-debug.yml
deployment.apps/py-debug-deployment unchanged
```
Then we need the IP address of the redis service
```
[isp02]$ kubectl get pods kchristi-test-redis-deployment-5b8774f7b8-bhhm8 -o wide
NAME                                              READY   STATUS    RESTARTS   AGE   IP              NODE   NOMINATED NODE   READINESS GATES
kchristi-test-redis-deployment-5b8774f7b8-bhhm8   1/1     Running   0          23m   10.244.13.161   c11    <none>           <none>
```
Then we exec into the Python debug container
```
[isp02]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-gkwnt -- /bin/bash
```
Then we set up redis
```
root@py-debug-deployment-5cc8cdd65f-gkwnt:/# pip3 install --user redis
Collecting redis
  Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
     |████████████████████████████████| 72 kB 1.2 MB/s
Installing collected packages: redis
Successfully installed redis-3.5.3

root@py-debug-deployment-5cc8cdd65f-gkwnt:/# python3
Python 3.9.2 (default, Feb 19 2021, 17:11:58)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> rd = redis.StrictRedis(host='10.244.13.161', port=6379, db=0)
```
Then we create a key and check that it is there
```
>>> rd.set('aKey','HelloWorld')
True
>>> rd.get('aKey')
b'HelloWorld'
```
Then in another terminal we delete the redis pod and it should make another one 
```
[isp02]$ kubectl delete pod kchristi-test-redis-deployment-5b8774f7b8-bhhm8
pod "kchristi-test-redis-deployment-5b8774f7b8-bhhm8" deleted
```
We get the IP of the new redis pod
```
[isp02]$ kubectl get pods -o wide
NAME                                              READY   STATUS    RESTARTS   AGE     IP              NODE                         NOMINATED NODE   READINESS GATES
hello                                             1/1     Running   457        19d     10.244.6.31     c03                          <none>           <none>
hello-deployment-55f4459bf-7kvf2                  1/1     Running   144        6d1h    10.244.5.133    c04                          <none>           <none>
hello-deployment-55f4459bf-bql96                  1/1     Running   144        6d      10.244.4.147    c02                          <none>           <none>
hello-deployment-55f4459bf-bzrfp                  1/1     Running   145        6d      10.244.3.193    c01                          <none>           <none>
hello-deployment-55f4459bf-hrjqz                  1/1     Running   144        6d      10.244.7.145    c05                          <none>           <none>
hello-hw5-1-c68d6bb7-g22r8                        1/1     Running   143        5d23h   10.244.7.153    c05                          <none>           <none>
hello-hw5-1-c68d6bb7-r95n2                        1/1     Running   143        5d23h   10.244.10.19    c009.rodeo.tacc.utexas.edu   <none>           <none>
hello-hw5-1-c68d6bb7-wbr8m                        1/1     Running   143        5d23h   10.244.4.154    c02                          <none>           <none>
hello-pvc-deployment-64897459c8-9tvps             1/1     Running   53         2d5h    10.244.3.21     c01                          <none>           <none>
helloflask-848c4fb54f-rwz2r                       1/1     Running   0          2d5h    10.244.3.22     c01                          <none>           <none>
kchristi-test-redis-deployment-5b8774f7b8-7k64p   1/1     Running   0          11s     10.244.13.174   c11                          <none>           <none>
py-debug-deployment-5cc8cdd65f-gkwnt              1/1     Running   0          2d4h    10.244.4.206    c02   
```
Then in the other terminal we check if the persistent volume claim is working as intended
```
>>> rd = redis.StrictRedis(host='10.244.13.174', port=6379, db=0)
>>> rd.get('aKey')
b'HelloWorld'
```
## STEP 4
To create the flask deployment
```
[isp02]$ kubectl apply -f kchristi-test-flask-deployment.yml
deployment.apps/kchristi-test-flask-deployment configured
```
## STEP 5
To create the flask service
```
[isp02]$ kubectl apply -f kchristi-test-flask-service.yml
service/kchristi-test-flask created
```
To test that the flask service actually works using the midterm docker image start by getting the IP addresses
```
[isp02]$ kubectl get pods -o wide
NAME                                              READY   STATUS    RESTARTS   AGE     IP              NODE                         NOMINATED NODE   READINESS GATES
hello                                             1/1     Running   480        20d     10.244.6.31     c03                          <none>           <none>
hello-deployment-55f4459bf-7kvf2                  1/1     Running   168        7d      10.244.5.133    c04                          <none>           <none>
hello-deployment-55f4459bf-bql96                  1/1     Running   167        6d23h   10.244.4.147    c02                          <none>           <none>
hello-deployment-55f4459bf-bzrfp                  1/1     Running   168        6d23h   10.244.3.193    c01                          <none>           <none>
hello-deployment-55f4459bf-hrjqz                  1/1     Running   167        6d23h   10.244.7.145    c05                          <none>           <none>
hello-hw5-1-c68d6bb7-g22r8                        1/1     Running   167        6d23h   10.244.7.153    c05                          <none>           <none>
hello-hw5-1-c68d6bb7-r95n2                        1/1     Running   167        6d23h   10.244.10.19    c009.rodeo.tacc.utexas.edu   <none>           <none>
hello-hw5-1-c68d6bb7-wbr8m                        1/1     Running   167        6d23h   10.244.4.154    c02                          <none>           <none>
hello-pvc-deployment-64897459c8-9tvps             1/1     Running   76         3d4h    10.244.3.21     c01                          <none>           <none>
helloflask-848c4fb54f-rwz2r                       1/1     Running   0          3d4h    10.244.3.22     c01                          <none>           <none>
kchristi-test-flask-deployment-7f8895d9f8-2w8zf   1/1     Running   0          113s    10.244.12.8     c12                          <none>           <none>
kchristi-test-flask-deployment-7f8895d9f8-shqlp   1/1     Running   0          117s    10.244.13.19    c11                          <none>           <none>
kchristi-test-redis-deployment-5b8774f7b8-7k64p   1/1     Running   0          23h     10.244.13.174   c11                          <none>           <none>
py-debug-deployment-5cc8cdd65f-gkwnt              1/1     Running   0          3d4h    10.244.4.206    c02                          <none>           <none>
```
Now exec into the python debugger
```
[isp02]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-gkwnt -- /bin/bash
```
Now test the routes from the midterm flask docker image
```
root@py-debug-deployment-5cc8cdd65f-gkwnt:/# curl 10.244.13.19:5000/helloworld
Hello World!!

root@py-debug-deployment-5cc8cdd65f-gkwnt:/# curl 10.244.13.19:5000/reset
You have reset the redis database

root@py-debug-deployment-5cc8cdd65f-gkwnt:/# curl 10.244.13.19:5000/animals
[{"body": "snail-cougar", "head": "bull", "uid": "3c75efcd-d398-4317-b827-b13ae6deb15a", "arms": "8", "created_on": "2021-04-15 04:30:01.103685", "tails": "11", "legs": "3"}, 
{"body": "drum-tick", "head": "bull", "uid": "8bc0095e-9623-4c92-a7e8-12799ab76e58", "arms": "4", "created_on": "2021-04-15 04:30:01.104616", "tails": "13", "legs": "9"}, 
{"body": "bird-koi", "head": "raven", "uid": "ab941838-b9b6-4a20-83d1-a260e22008ff", "arms": "10", "created_on": "2021-04-15 04:30:01.104931", "tails": "16", "legs": "6"}, 
{"body": "swine-crab", "head": "snake", "uid": "be6560b0-a0f3-49c4-8ecc-507c7b95a7e5", "arms": "6", "created_on": "2021-04-15 04:30:01.105205", "tails": "9", "legs": "3"}, 
{"body": "koala-donkey", "head": "bunny", "uid": "f4f56c61-93f2-4884-972a-dd96e5d1ed30", "arms": "4", "created_on": "2021-04-15 04:30:01.105561", "tails": "7", "legs": "3"}, 
{"body": "kite-badger", "head": "bull", "uid": "b6c8a1ed-6a86-4744-bb00-8b8b88cd0b0e", "arms": "6", "created_on": "2021-04-15 04:30:01.105894", "tails": "12", "legs": "6"}, 
{"body": "krill-grouse", "head": "raven", "uid": "e10736e7-cdc0-436d-ac74-80ca2273b96d", "arms": "4", "created_on": "2021-04-15 04:30:01.106196", "tails": "16", "legs": "12"}, 
{"body": "weevil-gibbon", "head": "bull", "uid": "78d20207-8b6f-45c2-bf9e-cb8bf77b0d8a", "arms": "6", "created_on": "2021-04-15 04:30:01.106547", "tails": "15", "legs": "9"}, 
{"body": "muskox-cod", "head": "snake", "uid": "497a45e1-22b7-478b-8dd0-12dafa747cb5", "arms": "6", "created_on": "2021-04-15 04:30:01.106859", "tails": "9", "legs": "3"}, 
{"body": "ray-slug", "head": "bull", "uid": "8aa3e024-6b94-4f46-b056-46afde432392", "arms": "10", "created_on": "2021-04-15 04:30:01.107127", "tails": "13", "legs": "3"}, 
{"body": "orca-calf", "head": "lion", "uid": "8911ffd2-2048-444a-9c8d-a3b23dd50e9f", "arms": "8", "created_on": "2021-04-15 04:30:01.107392", "tails": "14", "legs": "6"}, 
{"body": "guinea-joey", "head": "raven", "uid": "19fcf37b-4817-48c2-b04b-07f28bc44b4d", "arms": "4", "created_on": "2021-04-15 04:30:01.107723", "tails": "7", "legs": "3"}, 
{"body": "satyr-frog", "head": "snake", "uid": "7becfb5f-f16b-4147-9abf-81e619f61a21", "arms": "8", "created_on": "2021-04-15 04:30:01.108054", "tails": "17", "legs": "9"}, 
{"body": "goblin-owl", "head": "bunny", "uid": "594a43ae-8b8d-48c8-9dbe-3637470393ba", "arms": "6", "created_on": "2021-04-15 04:30:01.109773", "tails": "12", "legs": "6"}, 
{"body": "gnu-civet", "head": "snake", "uid": "376bf06c-246e-4ee3-a40c-5b5ac592129f", "arms": "8", "created_on": "2021-04-15 04:30:01.110807", "tails": "17", "legs": "9"}, 
{"body": "dane-sloth", "head": "raven", "uid": "de704d39-b13e-45b6-b90e-2fc2e39eb162", "arms": "8", "created_on": "2021-04-15 04:30:01.111146", "tails": "17", "legs": "9"}, 
{"body": "locust-weasel", "head": "bull", "uid": "2b7e3048-d857-4fbf-9f95-64ee718d705a", "arms": "10", "created_on": "2021-04-15 04:30:01.111527", "tails": "16", "legs": "6"}, 
{"body": "hippo-swine", "head": "raven", "uid": "d33c2bbe-fcd8-452b-a882-eec45433eea0", "arms": "6", "created_on": "2021-04-15 04:30:01.111865", "tails": "12", "legs": "6"}, 
{"body": "gar-egret", "head": "snake", "uid": "45a4403d-73ac-4ab1-a83a-407d6bf0ff6f", "arms": "10", "created_on": "2021-04-15 04:30:01.112154", "tails": "13", "legs": "3"}, 
{"body": "rhino-snipe", "head": "bunny", "uid": "719bc50a-b9ea-417d-8d9d-86056672ff5a", "arms": "2", "created_on": "2021-04-15 04:30:01.112496", "tails": "5", "legs": "3"}, 
{"body": "orca-turtle", "head": "raven", "uid": "250ef073-f151-4b56-8a00-87f751c20d3a", "arms": "6", "created_on": "2021-04-15 04:30:01.112782", "tails": "15", "legs": "9"}, 
{"body": "slug-chimp", "head": "bunny", "uid": "17da8de9-d09a-4129-9943-f81fb9c040d4", "arms": "8", "created_on": "2021-04-15 04:30:01.113070", "tails": "11", "legs": "3"}, 
{"body": "cow-grouse", "head": "lion", "uid": "71c69461-501b-4aff-a98e-5f4da60e8053", "arms": "6", "created_on": "2021-04-15 04:30:01.113369", "tails": "9", "legs": "3"}, 
{"body": "piglet-mantis", "head": "snake", "uid": "7487c82e-2bd0-447c-93f3-42e4954f4be2", "arms": "2", "created_on": "2021-04-15 04:30:01.113664", "tails": "14", "legs": "12"}, 
{"body": "cat-marlin", "head": "raven", "uid": "dae048c5-f86b-4d11-9439-eb83570212e5", "arms": "6", "created_on": "2021-04-15 04:30:01.113950", "tails": "12", "legs": "6"}, 
{"body": "pigeon-baboon", "head": "raven", "uid": "77fa265d-1adc-47bd-aa25-971aca9da244", "arms": "10", "created_on": "2021-04-15 04:30:01.114229", "tails": "13", "legs": "3"}, 
{"body": "gator-oyster", "head": "bunny", "uid": "6098343d-7297-4356-a38f-4e4fcebb6479", "arms": "8", "created_on": "2021-04-15 04:30:01.114521", "tails": "11", "legs": "3"}, 
{"body": "seal-leech", "head": "bull", "uid": "93bf88a7-b933-4a4f-a18a-5149b661d546", "arms": "10", "created_on": "2021-04-15 04:30:01.114817", "tails": "13", "legs": "3"}, 
{"body": "chimp-insect", "head": "bull", "uid": "c4901bd0-8d9c-490a-8a67-38075b5b1b67", "arms": "2", "created_on": "2021-04-15 04:30:01.115098", "tails": "8", "legs": "6"}, 
{"body": "newt-hermit", "head": "snake", "uid": "13fe2986-6298-4e5d-9908-20617590a363", "arms": "2", "created_on": "2021-04-15 04:30:01.115420", "tails": "5", "legs": "3"}, 
{"body": "clam-imp", "head": "snake", "uid": "32b87bb6-2646-4072-a027-e8f5542a1b2b", "arms": "2", "created_on": "2021-04-15 04:30:01.115697", "tails": "8", "legs": "6"}, 
{"body": "camel-lab", "head": "bull", "uid": "b83794fe-2055-4346-989a-4c8a330d27c3", "arms": "8", "created_on": "2021-04-15 04:30:01.115972", "tails": "14", "legs": "6"}, 
{"body": "camel-magpie", "head": "raven", "uid": "74e2a6fd-1dee-4390-ab1b-9c7a1edb7d44", "arms": "6", "created_on": "2021-04-15 04:30:01.116241", "tails": "12", "legs": "6"}, 
{"body": "cod-mantis", "head": "bull", "uid": "43664750-4312-42e6-855c-2d2bdb9b9111", "arms": "8", "created_on": "2021-04-15 04:30:01.116524", "tails": "11", "legs": "3"}, 
{"body": "mink-tarpon", "head": "bull", "uid": "65af3f04-1451-48ff-b77f-600b21aa998e", "arms": "10", "created_on": "2021-04-15 04:30:01.116797", "tails": "16", "legs": "6"}, 
{"body": "hippo-krill", "head": "bull", "uid": "d4e82f6f-bc72-4c49-b3e5-33327eb51537", "arms": "8", "created_on": "2021-04-15 04:30:01.117065", "tails": "11", "legs": "3"}, 
{"body": "jackal-horse", "head": "raven", "uid": "514fd3c8-10bd-4159-9775-7409859b9222", "arms": "2", "created_on": "2021-04-15 04:30:01.117341", "tails": "5", "legs": "3"}, 
{"body": "lizard-drum", "head": "raven", "uid": "8b91f40b-ff14-4137-a237-1c1b66e96a91", "arms": "4", "created_on": "2021-04-15 04:30:01.117609", "tails": "7", "legs": "3"}, 
{"body": "dodo-sawfly", "head": "raven", "uid": "d5918780-6a46-4a0b-bd05-a70c610a45c2", "arms": "2", "created_on": "2021-04-15 04:30:01.117881", "tails": "8", "legs": "6"}, 
{"body": "finch-weevil", "head": "raven", "uid": "e5b66490-2dbd-4a08-9b88-1150fb06fd74", "arms": "2", "created_on": "2021-04-15 04:30:01.118159", "tails": "5", "legs": "3"}, 
{"body": "insect-locust", "head": "bunny", "uid": "7bd34679-4291-4448-96b2-eae9d9d29eb6", "arms": "2", "created_on": "2021-04-15 04:30:01.118458", "tails": "8", "legs": "6"}, 
{"body": "colt-guppy", "head": "bunny", "uid": "aaa95118-9d26-4bb0-aac6-47da9a770a01", "arms": "10", "created_on": "2021-04-15 04:30:01.118758", "tails": "13", "legs": "3"}, 
{"body": "oyster-kitten", "head": "raven", "uid": "85a79824-ffb7-4408-a5b4-35bec91307fe", "arms": "8", "created_on": "2021-04-15 04:30:01.119031", "tails": "20", "legs": "12"}, 
{"body": "bird-skink", "head": "bunny", "uid": "45cd23fb-e6f7-424b-8faf-ff228e5add74", "arms": "2", "created_on": "2021-04-15 04:30:01.119321", "tails": "11", "legs": "9"}, 
{"body": "liger-lamb", "head": "lion", "uid": "7e8014ed-8b42-4de1-9e5a-347e5e424775", "arms": "4", "created_on": "2021-04-15 04:30:01.119597", "tails": "13", "legs": "9"}, 
{"body": "poodle-grub", "head": "lion", "uid": "d12f352e-5c1f-4e45-a65c-926ddd661aa0", "arms": "2", "created_on": "2021-04-15 04:30:01.119876", "tails": "8", "legs": "6"}, 
{"body": "condor-tuna", "head": "lion", "uid": "8d763cab-8700-4f82-b0ec-b073049a493f", "arms": "2", "created_on": "2021-04-15 04:30:01.120143", "tails": "8", "legs": "6"}, 
{"body": "sponge-marlin", "head": "bunny", "uid": "0d7401a5-322d-46b8-9d15-cebc7c5768bc", "arms": "2", "created_on": "2021-04-15 04:30:01.120426", "tails": "14", "legs": "12"}, 
{"body": "hound-swift", "head": "lion", "uid": "af03f26d-5fb1-469a-ae8d-b6e53353c925", "arms": "4", "created_on": "2021-04-15 04:30:01.120701", "tails": "10", "legs": "6"}, 
{"body": "whale-horse", "head": "lion", "uid": "c98a37f9-4880-4ca0-b05b-e27b69023665", "arms": "10", "created_on": "2021-04-15 04:30:01.120961", "tails": "22", "legs": "12"}, 
{"body": "bobcat-ant", "head": "snake", "uid": "ddff6620-4607-44f2-814f-a5c8c4261d7a", "arms": "4", "created_on": "2021-04-15 04:30:01.121232", "tails": "16", "legs": "12"}, 
{"body": "skink-guppy", "head": "bunny", "uid": "0581cda4-7f59-4a95-bce4-6017722dcd43", "arms": "4", "created_on": "2021-04-15 04:30:01.121496", "tails": "7", "legs": "3"}, 
{"body": "quagga-snail", "head": "raven", "uid": "53d9465b-ab60-4408-b3f1-6b1a615c359c", "arms": "2", "created_on": "2021-04-15 04:30:01.121749", "tails": "8", "legs": "6"}, 
{"body": "stud-swan", "head": "snake", "uid": "ac1e0596-3f13-432e-9409-d2ff3aa5037d", "arms": "4", "created_on": "2021-04-15 04:30:01.122001", "tails": "10", "legs": "6"}, 
{"body": "snipe-ewe", "head": "raven", "uid": "34c0d904-d1de-443d-b6ef-c2f10477d72a", "arms": "2", "created_on": "2021-04-15 04:30:01.122270", "tails": "8", "legs": "6"}, 
{"body": "mule-newt", "head": "bull", "uid": "e4bc7325-e6c5-493f-a250-fd03a870a328", "arms": "2", "created_on": "2021-04-15 04:30:01.122524", "tails": "14", "legs": "12"}, 
{"body": "dane-pug", "head": "bull", "uid": "3a6b04eb-d9e7-42ee-89f4-f04d39b9b78c", "arms": "6", "created_on": "2021-04-15 04:30:01.122788", "tails": "18", "legs": "12"}, 
{"body": "flea-midge", "head": "lion", "uid": "7be1cbd4-39b0-4438-90ca-639a7b40e80b", "arms": "2", "created_on": "2021-04-15 04:30:01.123056", "tails": "14", "legs": "12"}, 
{"body": "feline-chimp", "head": "snake", "uid": "54fcb4f0-4c5a-44c1-be21-67e9e26bf454", "arms": "10", "created_on": "2021-04-15 04:30:01.123340", "tails": "13", "legs": "3"}, 
{"body": "heron-akita", "head": "lion", "uid": "0cfdc896-af79-4c56-b238-92770b867803", "arms": "10", "created_on": "2021-04-15 04:30:01.123608", "tails": "16", "legs": "6"}, 
{"body": "lark-boxer", "head": "bull", "uid": "f9ee95b4-2157-41c9-95ff-c0d7efa27228", "arms": "2", "created_on": "2021-04-15 04:30:01.123890", "tails": "8", "legs": "6"}, 
{"body": "fowl-tomcat", "head": "bull", "uid": "f896f1b1-9e17-47db-9cf2-b1d47c5aabd1", "arms": "8", "created_on": "2021-04-15 04:30:01.124150", "tails": "20", "legs": "12"}, 
{"body": "bear-dory", "head": "snake", "uid": "80116916-b04d-4041-b4f4-eff00fb73acb", "arms": "8", "created_on": "2021-04-15 04:30:01.124424", "tails": "20", "legs": "12"}, 
{"body": "clam-ghoul", "head": "snake", "uid": "31d04833-691e-4bfb-81ca-6f2172c75f39", "arms": "10", "created_on": "2021-04-15 04:30:01.124680", "tails": "13", "legs": "3"}, 
{"body": "gibbon-grouse", "head": "bunny", "uid": "3740b4d9-97af-4a26-9a3b-321d68fd8886", "arms": "2", "created_on": "2021-04-15 04:30:01.124935", "tails": "14", "legs": "12"}, 
{"body": "dane-satyr", "head": "bull", "uid": "bf71110e-70da-4bd1-9db3-229f13e46894", "arms": "8", "created_on": "2021-04-15 04:30:01.125194", "tails": "20", "legs": "12"}, 
{"body": "yak-crane", "head": "lion", "uid": "36b23ffa-8f50-4517-b0e0-bca1c08216d3", "arms": "6", "created_on": "2021-04-15 04:30:01.125466", "tails": "15", "legs": "9"}, 
{"body": "boa-beetle", "head": "snake", "uid": "535f1db0-b4f4-4993-a33d-52bb7b6f55d4", "arms": "4", "created_on": "2021-04-15 04:30:01.125725", "tails": "16", "legs": "12"}, 
{"body": "filly-hornet", "head": "raven", "uid": "9a95a363-2cb5-4cf8-9b6c-ce6c4d21fcfc", "arms": "8", "created_on": "2021-04-15 04:30:01.125984", "tails": "20", "legs": "12"}, 
{"body": "swan-alpaca", "head": "lion", "uid": "64359119-ff01-4e95-ab33-bfa7803abdb9", "arms": "6", "created_on": "2021-04-15 04:30:01.126237", "tails": "18", "legs": "12"}, 
{"body": "stud-kid", "head": "snake", "uid": "2d417a51-bf2a-4a97-85c4-58f21669251c", "arms": "4", "created_on": "2021-04-15 04:30:01.126529", "tails": "7", "legs": "3"}, 
{"body": "calf-earwig", "head": "bull", "uid": "b5ad2532-60eb-4796-acb3-ef2be6947943", "arms": "10", "created_on": "2021-04-15 04:30:01.126798", "tails": "13", "legs": "3"}, 
{"body": "frog-quagga", "head": "bunny", "uid": "2350a277-8cb9-4802-bfd4-5dcb3ab17200", "arms": "2", "created_on": "2021-04-15 04:30:01.127050", "tails": "5", "legs": "3"}, 
{"body": "marten-muskox", "head": "lion", "uid": "a1aef634-79a5-491f-a46f-da1c3c21a779", "arms": "4", "created_on": "2021-04-15 04:30:01.127331", "tails": "16", "legs": "12"}, 
{"body": "wren-urchin", "head": "snake", "uid": "9cb13870-25e8-434f-97db-603d9133b94f", "arms": "8", "created_on": "2021-04-15 04:30:01.127605", "tails": "14", "legs": "6"}, 
{"body": "moray-sheep", "head": "bunny", "uid": "81a41315-0634-45a2-9df7-503eee9d13cc", "arms": "6", "created_on": "2021-04-15 04:30:01.127872", "tails": "18", "legs": "12"}, 
{"body": "chimp-civet", "head": "lion", "uid": "0e22225d-a0b5-4b00-ba39-4641ef6d2045", "arms": "6", "created_on": "2021-04-15 04:30:01.128130", "tails": "12", "legs": "6"}, 
{"body": "hound-hyena", "head": "raven", "uid": "504987cb-a64f-49cf-af0d-8856c0838657", "arms": "4", "created_on": "2021-04-15 04:30:01.128394", "tails": "16", "legs": "12"}, 
{"body": "pig-stud", "head": "lion", "uid": "aa41a297-5294-4112-a7da-e0809da37579", "arms": "6", "created_on": "2021-04-15 04:30:01.128667", "tails": "9", "legs": "3"}, 
{"body": "ray-kid", "head": "bunny", "uid": "87b9ae41-0ffc-4c34-966d-dc87346453ac", "arms": "2", "created_on": "2021-04-15 04:30:01.128920", "tails": "14", "legs": "12"}, 
{"body": "mouse-mantis", "head": "bunny", "uid": "e5af17b1-88ec-43cd-bd0d-df8a943143d8", "arms": "4", "created_on": "2021-04-15 04:30:01.129172", "tails": "10", "legs": "6"}, 
{"body": "toad-bee", "head": "snake", "uid": "2c2d4861-bec3-4739-9ad8-73ae847e63d3", "arms": "4", "created_on": "2021-04-15 04:30:01.129464", "tails": "7", "legs": "3"}, 
{"body": "tahr-jennet", "head": "bull", "uid": "0726dfdd-ebe7-4cd4-bb68-7c7006a7df59", "arms": "8", "created_on": "2021-04-15 04:30:01.129719", "tails": "20", "legs": "12"}, 
{"body": "gator-tarpon", "head": "lion", "uid": "497f23f8-d439-4aa9-b959-771a18221077", "arms": "2", "created_on": "2021-04-15 04:30:01.129973", "tails": "8", "legs": "6"}, 
{"body": "beagle-beagle", "head": "raven", "uid": "49c7eea9-b4fb-4254-9196-6e4a35124b62", "arms": "10", "created_on": "2021-04-15 04:30:01.130225", "tails": "13", "legs": "3"}, 
{"body": "moose-fowl", "head": "snake", "uid": "a1ee7419-6c45-4203-9006-4466c77b4b8e", "arms": "2", "created_on": "2021-04-15 04:30:01.130506", "tails": "5", "legs": "3"}, 
{"body": "coral-egret", "head": "raven", "uid": "ac6a2cf2-44b6-41e5-aa50-20a6864de5b9", "arms": "2", "created_on": "2021-04-15 04:30:01.130769", "tails": "5", "legs": "3"}, 
{"body": "alpaca-dove", "head": "bunny", "uid": "46d3e2a3-1b82-4a99-98cc-a8ce92db945d", "arms": "8", "created_on": "2021-04-15 04:30:01.131026", "tails": "11", "legs": "3"}, 
{"body": "shiner-beagle", "head": "bull", "uid": "2a255aab-6c7c-48d0-9d0e-f23ed13222e3", "arms": "6", "created_on": "2021-04-15 04:30:01.131292", "tails": "18", "legs": "12"}, 
{"body": "sponge-dane", "head": "bull", "uid": "7a07b367-0165-46b2-91a2-724320e4a3ca", "arms": "4", "created_on": "2021-04-15 04:30:01.131543", "tails": "10", "legs": "6"}, 
{"body": "ox-sheep", "head": "snake", "uid": "7344dfbe-604c-41d6-947d-bcf6b16a52aa", "arms": "2", "created_on": "2021-04-15 04:30:01.131795", "tails": "5", "legs": "3"}, 
{"body": "bengal-trout", "head": "bull", "uid": "13e8a115-cb6b-47eb-8c3d-0241d4d86640", "arms": "6", "created_on": "2021-04-15 04:30:01.132042", "tails": "15", "legs": "9"}, 
{"body": "macaw-dragon", "head": "bull", "uid": "fd90f01e-aee9-49c1-bb71-2e385551d720", "arms": "6", "created_on": "2021-04-15 04:30:01.132322", "tails": "15", "legs": "9"}, 
{"body": "wasp-sheep", "head": "lion", "uid": "0bdb0485-9fe5-4f04-9764-4ec6e322eca3", "arms": "2", "created_on": "2021-04-15 04:30:01.132588", "tails": "14", "legs": "12"}, 
{"body": "fox-spider", "head": "bunny", "uid": "db490ec0-fa08-4ca5-b85a-abcc58757238", "arms": "8", "created_on": "2021-04-15 04:30:01.132830", "tails": "20", "legs": "12"}, 
{"body": "drake-seal", "head": "snake", "uid": "02c701d5-8752-4f28-bb5b-929347c89d71", "arms": "10", "created_on": "2021-04-15 04:30:01.133082", "tails": "13", "legs": "3"}, 
{"body": "oriole-coyote", "head": "raven", "uid": "210d74a3-3945-4707-a149-e37232bbb718", "arms": "10", "created_on": "2021-04-15 04:30:01.133345", "tails": "13", "legs": "3"}, 
{"body": "burro-akita", "head": "snake", "uid": "7fd56f33-0fc4-4a01-bd92-579bd73f044f", "arms": "10", "created_on": "2021-04-15 04:30:01.133588", "tails": "16", "legs": "6"}, 
{"body": "monkey-lemur", "head": "lion", "uid": "3cedca2a-fb06-4c3c-9a79-49bc7fe9f930", "arms": "4", "created_on": "2021-04-15 04:30:01.133833", "tails": "10", "legs": "6"}, 
{"body": "stud-ferret", "head": "bunny", "uid": "abc29904-ad86-48da-90ed-055e2ae00129", "arms": "4", "created_on": "2021-04-15 04:30:01.134082", "tails": "16", "legs": "12"}]

```
