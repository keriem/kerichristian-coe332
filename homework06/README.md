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
