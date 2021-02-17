#!/usr/bin/env python3
import json
import random
import sys

def breed(first_anim, second_anim):
    assert isinstance(first_anim,dict), 'Input to this function should be a dictionary'
    assert isinstance(second_anim,dict), 'Input to this function should be a dictionary'    

    child = {}
    child['head'] = first_anim['head']+'-'+second_anim['head']
    child['body'] = first_anim['body']+'-'+second_anim['body']
    child['arms'] = round((first_anim['arms']+second_anim['arms'])/2)
    child['legs'] = round((first_anim['legs']+second_anim['legs'])/2)
    child['tail'] = child['arms']+child['legs']
    return child

def main():

    with open(sys.argv[1], 'r') as f:
        animal_dict = json.load(f)

    print(random.choice(animal_dict['animals']))
    first_anim = random.choice(animal_dict['animals'])
    second_anim = random.choice(animal_dict['animals'])

    child = breed(first_anim,second_anim)
    print('Parents: \n')
    print(first_anim)
    print('\n')
    print(second_anim)
    print('\n')
    print('Child: \n')
    print(child)
    
if __name__ == '__main__':
    main()






























