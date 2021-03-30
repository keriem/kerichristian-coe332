import random, uuid, datetime, json, petname, redis

#def main():
rd = redis.StrictRedis(host = '127.0.0.1',port=6386,db=0)

#rd = redis.StrictRedis(host = '127.0.0.1',port=6379,db=0)
userdata = []
for i in range(0,100):
    animal={}
    animal['uid'] = str(rd.hget(i,'uid'))[1:]
    animal['head'] = str(rd.hget(i,'head'))[1:]
    animal['body'] = str(rd.hget(i,'body'))[1:]
    animal['arms'] = str(rd.hget(i,'arms'))[1:]
    animal['legs'] = str(rd.hget(i,'legs'))[1:]
    animal['tail'] = str(rd.hget(i,'tail'))[1:]
    animal['created_on'] = str(rd.hget(i,'created_on'))[1:]
    userdata.append(animal)

print(json.dumps(userdata))
