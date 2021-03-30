import requests
import json
#This is Zoe Watson's url to get all of her animals.
#response = requests.get(url="http://localhost:5037/animals")

response1 = requests.get(url="http://localhost:5006/animals")

#look at the response code
#print(response1)
print(response1.status_code)
print(response1.json())
print(response1.headers)

response2 = requests.get(url="http://localhost:5006/animals/head?name='snake'")

#look at the response code
#print(response2)
print(response2.status_code)
print(response2.json())
print(response2.headers)

response3 = requests.get(url="http://localhost:5006/animals/legs?number=6")

#look at the response code
#print(response3)
print(response3.status_code)
print(response3.json())
print(response3.headers)

response4 = requests.get(url="http://localhost:5006/animals/createRandom")

#look at the response code
#print(response4)
print(response4.status_code)
print(response4.json())
print(response4.headers)

response5 = requests.get(url="http://localhost:5006/animals/number?top=50")

#look at the response code
#print(response5)
print(response5.status_code)
print(response5.json())
print(response5.headers)

response6 = requests.get(url="http://localhost:5006/animals/breed")

#look at the response code
#print(response6)
print(response6.status_code)
print(response6.json())
print(response6.headers)


