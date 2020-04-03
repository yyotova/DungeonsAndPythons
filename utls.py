from main_classes.potion import Potion
from main_classes.spell import Spell
from main_classes.weapon import Weapon
from main_classes.enemy import Enemy
from random import randint

def convert_treasures_as_instance(dict_with_treasures):
    list_with_instance = []

    for key, value in dict_with_treasures.items():
        if key == 'potion':
            for potion in value:
                if 'health' in potion:
                    list_with_instance.append(Potion(potion = 'health', points = potion['health']))
                elif 'mana' in potion:
                    list_with_instance.append(Potion(potion = 'mana', points = potion['mana']))

        elif key == 'spell':
            for spell in value:
                list_with_instance.append(Spell(name = spell['name'],damage = spell['damage'],mana_cost = spell['mana_cost'],cast_range = spell['cast_range']))

        elif key == 'weapon':
            for weapon in value:
                list_with_instance.append(Weapon(name = weapon['name'],damage = weapon['damage']))

    return list_with_instance

def convert_enemies_as_instance(dict_with_enemies):
    list_with_instance = []

    for enemy in dict_with_enemies['enemy']:
        list_with_instance.append(Enemy(health = enemy['health'],damage = enemy['damage'], mana = enemy['mana']))

    return list_with_instance


def random_treasure(treasures):
    index = randint(0, len(treasures))

    return treasures[index]

def random_enemy(enemies):
    index = randint(0, len(enemies))

    return enemies[index]
