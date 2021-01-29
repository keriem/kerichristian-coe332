import json
import petname
import random

ani = {}
ani['animals']=[]
for i in range(0,20):
    head = random.randrange(6)
    arms = random.randrange(2,11,1)
    legs = random.randrange(3,13,1)
    tails = arms+legs
    str_head = ''
    body1 = petname.name()
    body2 = petname.name()
    str_body = body1 + "-" + body2
    animal={}
    if(head==1):
       str_head='snake'
    elif(head==2):
       str_head='bull'
    elif(head==3):
       str_head='lion'
    elif(head==4):
       str_head='raven'
    else:
       str_head='bunny'

    animal={
        'head':str_head,
        'body':str_body,
        'arms':arms,
        'legs':legs,
        'tail':tails
    }
    ani['animals'].append(animal)

with open('animals.json','w') as out:
    json.dump(ani,out,indent=2)








