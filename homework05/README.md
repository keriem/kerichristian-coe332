 # Homework 5
---
deployments-parta.yml is the yml file for PART A. deployments-partb.yml is the yml file for PART B. deployments.yml is the yml file for PART C.
---
## PART A
Here is the command to create the pod
```
[isp02]$ kubectl apply -f deployments-parta.yml
```
This is the command to get the pod using selector
```
[isp02]$ kubectl get pods  --selector "greeting=personalized"
```
Here is the output:
```
NAME          READY   STATUS    RESTARTS   AGE
hello         1/1     Running   313        13d
hello-hw5     1/1     Running   0          101s
hello-hw5-1   1/1     Running   0          5s
```
This is because I had a few mess ups at first doing PART A.
This is how to check the logs and the output given:
```
[isp02]$ kubectl logs hello-hw5-1
Hello, !
```
This is what I expected because NAME does not have a value.
This is the command to delete the pod
```
[isp02]$ 
kubectl delete pods hello-hw5-1
pod "hello-hw5-1" deleted
```
## PART B
This is the command to create the pod
```
[isp02]$ kubectl apply -f deployments-partb.yml
pod/hello-hw5-1 created
```
This is the command and output by checking the logs
```
[isp02]$ kubectl logs hello-hw5-1
Hello, Keri!
```
This is the command and output to delete the pod
```
[isp02]$ kubectl delete pods hello-hw5-1
pod "hello-hw5-1" deleted
```
## PART C
This is the command to create the deployment of 3 replica pods 
```
[isp02]$ kubectl apply -f deployments-partc.yml
deployment.apps/hello-hw5-1 created
```
This is the command to get all the pods' IP addresses and the output of said command:
```
[isp02]$ kubectl get pods -o wide
NAME                               READY   STATUS    RESTARTS   AGE   IP             NODE                         NOMINATED NODE   READINESS GATES
hello                              1/1     Running   313        13d   10.244.6.31    c03                          <none>           <none>
hello-deployment-55f4459bf-7kvf2   1/1     Running   1          64m   10.244.5.133   c04                          <none>           <none>
hello-deployment-55f4459bf-bql96   1/1     Running   0          51m   10.244.4.147   c02                          <none>           <none>
hello-deployment-55f4459bf-bzrfp   1/1     Running   0          51m   10.244.3.193   c01                          <none>           <none>
hello-deployment-55f4459bf-hrjqz   1/1     Running   0          51m   10.244.7.145   c05                          <none>           <none>
hello-hw5                          1/1     Running   0          16m   10.244.4.152   c02                          <none>           <none>
hello-hw5-1-c68d6bb7-g22r8         1/1     Running   0          50s   10.244.7.153   c05                          <none>           <none>
hello-hw5-1-c68d6bb7-r95n2         1/1     Running   0          50s   10.244.10.19   c009.rodeo.tacc.utexas.edu   <none>           <none>
hello-hw5-1-c68d6bb7-wbr8m         1/1     Running   0          50s   10.244.4.154   c02                          <none>           <none>
```
These are the logs and output of each pod:
```
[isp02]$ kubectl logs hello-hw5-1-c68d6bb7-g22r8
Hello, Keri from IP 10.244.7.153!

[isp02]$ kubectl logs hello-hw5-1-c68d6bb7-r95n2
Hello, Keri from IP 10.244.10.19!

[isp02]$ kubectl logs hello-hw5-1-c68d6bb7-wbr8m
Hello, Keri from IP 10.244.4.154!
```
These IP addresses match what was shown in the logs of those pods.
