import random, uuid, datetime, json, petname, redis

userdata = []
rd = redis.StrictRedis(host = '127.0.0.1',port=6386,db=0)

userdata =[]
def add_data_redis(num,animal):
    rd.hmset(num,animal)
def add_data(animal):
    userdata.append(animal)

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

    #print(json.dumps(animal))
  
    add_data_redis(i,animal)
    add_data(animal)


with open("data_file.json","w") as write_file:
    json.dump(userdata,write_file)

