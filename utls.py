from main_classes.potion import Potion
from main_classes.spell import Spell
from main_classes.weapon import Weapon

def convert_into_treasures_as_instance(dict_with_treasures):
    list_with_instance = []

    for key, value in dict_with_treasures.items():
        if key == 'potion':
            for potion in value:
                if 'health' in potion:
                    list_with_instance.append(Potion('health', potion['health']))
                elif 'mana' in potion:
                    list_with_instance.append(Potion('mana', potion['mana']))

        elif key == 'spell':
            for spell in value:
                list_with_instance.append(Spell(spell['name'], spell['damage'], spell['mana_cost'], spell['cast_range']))

        elif key == 'weapon':
            for weapon in value:
                list_with_instance.append(Weapon(weapon['name'], weapon['damage']))


    return list_with_instance