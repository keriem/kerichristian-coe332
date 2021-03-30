import json
import petname
import random
from flask import Flask, request
import redis
import uuid
import datetime


app = Flask(__name__)


@app.route('/helloworld',methods=['GET'])
def hello_world():
    return "Hello World!!\n"

@app.route('/animals',methods=['GET'])
def get_animals():
    return json.dumps(getdata())

@app.route('/animals/uid',methods=['GET'])
def get_uid_animal():
    uuid = str(request.args.get('value'))
    test = getdata()
    return json.dumps([x for x in test if x['uid'] == uuid])
    #return uuid

@app.route('/animals/edit',methods=['GET'])
def edit_animal():
    uuid = str(request.args.get('uid'))
    head = request.args.get('head')
    body = request.args.get('body')
    arms = request.args.get('arms')
    legs = request.args.get('legs')
    tails = request.args.get('tails')
    cdate = str(datetime.datetime.now())
    test = getdata()
    rd = redis.StrictRedis(host = 'kchristi_redis_1',port=6379,db=0)
    animal = [x for x in test if "'"+(x['uid'])+"'"==uuid]
    rd.hmset(test.index(animal[0]),{'uid': uuid.replace("'",""),'head': head.replace("'",""),'body': body.replace("'",""),'arms': arms.replace("'",""),'legs': legs.replace("'",""),'tails':tails.replace("'",""),'created_on':cdate})
    test = getdata()
    return json.dumps([x for x in test if "'"+(x['uid'])+"'"==uuid])
    

@app.route('/animals/averagelegs',methods=['GET'])
def get_average_legs():
    total = 0
    count = 0
    test = getdata()
    legs = [x for x in test if x['legs']!='None']
    #average = 0
    #rd = redis.StrictRedis(host = 'kchristi_redis_1',port=6379,db=0)
    for i in range(0,len(legs)):
        animal = legs[i]
        value = str(animal['legs'])
        total = total + int(value)
        count = count +1
    average = total/float(count)
    #return str(rd.hget(0,'legs'))
    return str(average)

@app.route('/animals/total',methods=['GET'])
def get_total():
    count = 0
    test = getdata()
    animals = [x for x in test if x['legs']!='None']
    for i in range(0,len(animals)):
        count = count+1
    return str(count)


def getdata():
    rd = redis.StrictRedis(host = 'kchristi_redis_1',port=6379,db=0)
    userdata = []
    for i in range(0,100):
        animal={}
        animal['uid'] = str(rd.hget(i,'uid'))
        animal['head'] = str(rd.hget(i,'head'))
        animal['body'] = str(rd.hget(i,'body'))
        animal['arms'] = str(rd.hget(i,'arms'))
        animal['legs'] = str(rd.hget(i,'legs'))
        animal['tails'] = str(rd.hget(i,'tails'))
        animal['created_on'] = str(rd.hget(i,'created_on'))
        userdata.append(animal)
         
    #with open("/app/data_file.json","r") as json_file:
    #    userdata = json.load(json_file)
    #index = 0 
    #for i in userdata:
    #    rd.hmset(index,i)
    #    index= inex+1
  
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
    return json.dumps(animal)

def create_animal():
    heads = ["snake","raven", "lion", "bull", "bunny"]   
    uid = str(uuid.uuid4())
    head = random.choice(heads)
    body = petname.name() + '-' + petname.name()
    arms = random.randint(1,5)*2
    legs = random.randint(1,4)*3
    tails = arms+legs
    cdate = str(datetime.datetime.now())

    animal={}
    animal['uid']=uid
    animal['head']=head
    animal['body']=body
    animal['arms']=arms
    animal['legs']=legs
    animal['tails']=tails
    animal['created_on']= cdate

    return animal

@app.route('/animals/breed',methods=['GET'])
def get_breed():
    first_anim = random.choice(getdata())
    second_anim = random.choice(getdata())

    child = breed(first_anim,second_anim)
    return json.dumps(child)
    
def breed(first_anim, second_anim):
    child = {}
    child['uid'] = str(uuid.uuid4())
    child['head'] = first_anim['head']+'-'+second_anim['head']
    child['body'] = first_anim['body']+'-'+second_anim['body']
    child['arms'] = round((first_anim['arms']+second_anim['arms'])/2)
    child['legs'] = round((first_anim['legs']+second_anim['legs'])/2)
    child['tail'] = child['arms']+child['legs']
    child['created_on'] = str(datetime.datetime.now())
    return child

@app.route('/animals/dates',methods=['GET'])
def get_dates():
    start = request.args.get('start')
    end = request.args.get('end')
    print(start)
    print(end)
    startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    enddate = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
    test = getdata()
    return json.dumps([x for x in test if (x['created_on']!='None' and (datetime.datetime.strptime( x['created_on'],'%Y-%m-%d %H:%M:%S.%f') >= startdate and datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f')<= enddate )) ])    

@app.route('/animals/delete/dates',methods=['GET'])
def delete_dates():
    start = request.args.get('start')
    end = request.args.get('end')
    print(start)
    print(end)
    startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    enddate = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
    test = getdata()
    removals = []
    removals =[x for x in test if (x['created_on']!= 'None' and (datetime.datetime.strptime( x['created_on'],'%Y-%m-%d %H:%M:%S.%f') >= startdate and datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f')<= enddate )) ]   
    rd = redis.StrictRedis(host = 'kchristi_redis_1',port=6379,db=0)
    for i in range(0,len(removals)):
        indexes = test.index(removals[i])
        rd.delete(indexes)
        #rd.hdel('head',indexes)
        #rd.hdel('body',indexes)
        #rd.hdel('arms',indexes)
        #rd.hdel('legs',indexes)
        #rd.hdel('tails',indexes)
        #rd.hdel('created_on',indexes)

    return json.dumps(removals)

@app.route('/reset',methods=['GET'])
def reset_redis():

    rd = redis.StrictRedis(host = 'kchristi_redis_1',port=6379,db=0)
    heads = ["snake","raven", "lion", "bull", "bunny"]

    for i in range(0,100):
        uid = str(uuid.uuid4())
        head = random.choice(heads)
        body = petname.name() + '-' + petname.name()
        arms = random.randint(1,5)*2
        legs = random.randint(1,4)*3
        tails = arms+legs
        cdate = str(datetime.datetime.now())

        animal={}
        animal["uid"]=uid
        animal["head"]=head
        animal["body"]=body
        animal["arms"]=arms
        animal["legs"]=legs
        animal["tails"]=tails
        animal["created_on"]= cdate
        rd.hmset(i,animal)

    return "You have reset the redis database"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
