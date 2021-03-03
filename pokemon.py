import random
import time
from utilities import setup_game, load_pokemon

# POKEMON: YEET
# Class that defines a pokemon
class Pokemon:
    def __init__(self, name, type, hp = 100):
        self.name = name
        self.type = type
        self.attacks = {"tackle": 10, "leer": 20, "cut": 25, "scratch": 35}
        self.hp = hp
        #self.weakness = weakness
        #self.status = "awake"

    # print print hp
    def get_status(self):
        print(f"{self.name}: HP: {self.hp} TYPE: {self.type}")

    # print move list
    def get_attacks(self):
        for k, v in self.attacks.items():
            print(k,v)

    def run_attack(self):
        attack = random.choice(list(self.attacks.keys()))
        damage = self.attacks[attack]
        print(f"{self.name} attacked with {attack} and it did {damage} damage")
        time.sleep(2)

        return damage
    
    def receive_attack(self, damage):
        self.hp -= damage
        self.get_status()

class Lineup:
    def __init__(self):
        self.members = []

    def add_member(self, pokemon):
        if len(self.members) < 3:
            self.members.append(pokemon)
        else:
            print("Sorry Team Already Full")

    def show_lineup(self):
        for i in self.members:
            i.get_status()
        
    def recruit(self):
        for i in range(0,3):
            rand_pokemon = random.randint(1,152)
            poke_name, poke_type, poke_hp = load_pokemon(rand_pokemon)
            pokemon_to_add = Pokemon(poke_name, poke_type, poke_hp)
            self.members.append(pokemon_to_add)
            #del pokelist[pokemon_to_add.name]
            
        return self
        


def gameLogic():
    print("get ready, now recruiting your team of pokemon!")
    our_team = Lineup().recruit()
    time.sleep(1.5)
    print("\n")

    print("team selected! meet your new team")
    our_team.show_lineup()
    time.sleep(3)
    print("\n")

    print("now recruiting the enemy team!")
    your_team = Lineup().recruit()
    time.sleep(1.5)
    print("\n")

    print("team selected! meet your enemies!")
    your_team.show_lineup()
    time.sleep(5)

    print("PREPARE TO FIGHT!!!!!")
    time.sleep(3)

    our_score = 0
    enemy_score = 0

    for i in range(len(your_team.members)):
        while your_team.members[i].hp > 0 and our_team.members[i].hp > 0:
            damage = our_team.members[i].run_attack()
            your_team.members[i].receive_attack(damage)
            time.sleep(1)

            if your_team.members[i].hp <= 0:
                print(f"{your_team.members[i].name} has FAINTED")
                your_team.members[i].status = "Fainted"
                your_team.members[i].get_status()
                our_score += 1
                print(f"THE SCORE IS: ME:{our_score} ENEMY:{enemy_score}")
                continue

            damage = your_team.members[i].run_attack()
            our_team.members[i].receive_attack(damage)
            time.sleep(1)

            if our_team.members[i].hp <= 0:
                print(f"{our_team.members[i].name} has FAINTED")
                our_team.members[i].status = "Fainted"
                our_team.members[i].get_status()
                enemy_score += 1
                print(f"THE SCORE IS: ME:{our_score} ENEMY:{enemy_score}")
                continue
    
    if our_score > enemy_score:
        print("WE WON HAHAHAHAHAHAHAHAHAHAHAHA")
    else:
        print("WE LOST BECAUSE WE ARE LOSERS")

setup_game()
gameLogic()