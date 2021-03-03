import requests
import json
import os

def setup_game():
    if os.path.isdir('./pokemon') == False:
        print("Creating pokemon directory...")
        os.mkdir('./pokemon')

    for i in range(1, 152):
        if os.path.isfile(f'./pokemon/{i}.json') == False:
            print("Importing Pokemon....")
            try:
                r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
                f = open(f"./pokemon/{i}.json", "a")
                f.write(r.text)
                f.close()

            except:
                print(f"Poke Number: {i} not found")
                continue
    
    print("Game is Setup and Ready to begin")


def load_pokemon(pokemon):
    with open(f'./pokemon/{pokemon}.json') as f:
        data = json.load(f)

        poke_name = data['name']
        poke_type = data['types'][0]['type']['name']
        poke_hp = data['stats'][0]['base_stat']

    return poke_name, poke_type, poke_hp