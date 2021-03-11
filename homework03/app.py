import json
import petname
import random
from flask import Flask, request

app = Flask(__name__)


@app.route('/helloworld',methods=['GET'])
def hello_world():
    return "Hello World!!\n"

@app.route('/animals',methods=['GET'])
def get_animals():
    return json.dumps(getdata())

def getdata():
    with open("/app/data_file.json","r") as json_file:
        userdata = json.load(json_file)
    return userdata

@app.route('/animals/head',methods=['GET'])
def get_animal_head():
    head = request.args.get('name')
    test = getdata()
    return json.dumps([x for x in test if x['head'] == head])

@app.route('/animals/legs',methods=['GET'])
def get_animal_legs():
    legs = int(request.args.get('number'))
    test = getdata()
    return json.dumps([x for x in test if x['legs'] == legs])

@app.route('/animals/number',methods=['GET'])
def get_top_animals():    
    amount = int(request.args.get('top'))
    test = getdata()
    return json.dumps( test[:amount])    

@app.route('/animals/createRandom',methods=['GET'])
def get_animal():
    animal = create_animal()
    return json.dumps( animal)

def create_animal():
    this_animal = {}
    this_animal['head'] = random.choice(['snake', 'bull', 'lion', 'raven', 'bunny'])
    this_animal['body'] = petname.name() + '-' + petname.name()
    this_animal['arms'] = random.randint(1,5) * 2
    this_animal['legs'] = random.randint(1,4) * 3
    this_animal['tail'] = this_animal['legs'] + this_animal['arms']
    return this_animal

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
