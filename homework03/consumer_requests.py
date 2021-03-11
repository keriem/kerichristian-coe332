import requests

#This is JOhn Matthew Mason's url to get the first five animals
response = requests.get(url="http://localhost:5018/animals?num_animals=5")

#look at the response code
print(response)
print(response.status_code)
print(response.json())
print(response.headers)
