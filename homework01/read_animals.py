import json
import petname
import random

with open('animals.json','r') as f:
    ani=json.load(f)
    random_number = random.randrange(0,20,1)
    the_animal = ani['animals'][random_number]
    print(the_animal)




























