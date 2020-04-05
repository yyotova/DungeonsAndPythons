import sys
sys.path.append('.')

from utls import *
from source_package.file_manipulation.read_file import *
from source_package.main_classes.hero import Hero
from source_package.main_classes.potion import Potion
from source_package.main_classes.spell import Spell
from source_package.main_classes.weapon import Weapon
from source_package.main_classes.fight import Fight


def get_locations_of_objects(array, object):
    locations = []

    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if array[i][j] == object:
                locations.append([i * 100, j * 100])

    return locations


def check_for_something(points, array):
    for obstacle in array:
        if points[0] == obstacle[0] and points[1] == obstacle[1]:
            return True
    return False


class Dungeon:
    def __init__(self, file_name):
        self.file_name = file_name
        self.map = read_from_file_with_first_level(file_name)
        self.hero = None
        self.fill_location_list()

    def set_obstacle_location(self):
        self.obstacle_localtions = get_locations_of_objects(self.map, "#")

    def set_treasure_location(self):
        self.treasure_locations = get_locations_of_objects(self.map, "T")

    def set_enemy_location(self):
        self.enemy_locations = get_locations_of_objects(self.map, "E")

    def set_spawn_location(self):
        self.spawn_locations = get_locations_of_objects(self.map, "S")

    def set_gateway_location(self):
        self.gateway_location = get_locations_of_objects(self.map, "G")

    def fill_location_list(self):
        self.set_obstacle_location()
        self.set_enemy_location()
        self.set_spawn_location()
        self.set_treasure_location()
        self.set_gateway_location()

    def spawn(self, hero):
        if len(self.spawn_locations) == 0:
            return False
        else:
            if self.hero is not None:
                self.hero = hero
                self.hero.location = self.spawn_locations[0]
                self.spawn_locations.remove(self.spawn_locations[0])
            else:
                self.hero = hero
                self.hero.location = self.spawn_locations[0]
                self.spawn_locations.remove(self.spawn_locations[0])

    def print_map(self):
        res = ''
        for line in self.map:
            for char in line:
                res += ''.join(char)
            res += ''.join('\n')
        print(res)

    def move_hero(self, direction):
        direction = direction.upper()

        if direction == "UP":
            new_x = self.hero.location[0] - 100
            new_y = self.hero.location[1]
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_x >= 0:
                self.hero.location[0] -= 100
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()

        elif direction == "DOWN":
            new_x = self.hero.location[0] + 100
            new_y = self.hero.location[1]
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_x < len(self.map) * 100:
                self.hero.location[0] += 100
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()

        elif direction == "RIGHT":
            new_x = self.hero.location[0]
            new_y = self.hero.location[1] + 100
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_y < len(self.map[0]) * 100:
                self.hero.location[1] += 100
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()

        elif direction == "LEFT":
            new_x = self.hero.location[0]
            new_y = self.hero.location[1] - 100
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_y >= 0:
                self.hero.location[1] -= 100
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()

    def check_for_treasure(self):
        if check_for_something(self.hero.location, self.treasure_locations) is True:
            treasure = random_treasure(convert_treasures_as_instance(read_from_file_with_treasures('treasures.txt')))
            self.treasure_locations.remove(self.hero.location)
            if treasure.__class__.__name__ == 'Potion':
                if treasure.potion == 'health':
                    self.hero.take_healing(treasure.points)
                else:
                    self.hero.take_mana(treasure.points)
            elif treasure.__class__.__name__ == 'Spell':
                if treasure.damage > self.hero.attack(by="spell"):
                    self.hero.learn(treasure)
            else:
                if treasure.damage > self.hero.attack(by="weapon"):
                    self.hero.equip(treasure)
            print(treasure)

    def check_for_enemy(self):
        if check_for_something(self.hero.location, self.enemy_locations) is True:
            enemy = random_enemy(convert_enemies_as_instance(read_from_file_with_enemies('enemies.txt')))
            enemy.location = self.hero.location
            self.enemy_locations.remove(enemy.location)
            fight = Fight(self.hero, enemy)
            fight.mortal_kombat()
            self.hero = fight.return_hero()

            if not self.hero.is_alive():
                print('GAME OVER')

    def hero_attack(self, by):
        hero_x = self.hero.location[0]
        hero_y = self.hero.location[1]

        nearest_enemies = []
        cast_range = self.hero.spell.cast_range

        for enemy in self.enemy_locations:
            if enemy[0] >= hero_x - cast_range and enemy[0] <= hero_x + cast_range and enemy[1] == hero_y:
                nearest_enemies.append(enemy)
                self.enemy_locations.remove(enemy)
            elif enemy[1] >= hero_y - cast_range and enemy[1] <= hero_y + cast_range and enemy[0] == hero_x:
                nearest_enemies.append(enemy)
                self.enemy_locations.remove(enemy)

        if len(nearest_enemies) > 0:
            enemy = random_enemy(convert_enemies_as_instance(read_from_file_with_enemies('enemies.txt')))

            # getting first coordinates in the list
            enemy.location = nearest_enemies[0]
            fight = Fight(self.hero, enemy)
            fight.mortal_kombat()
            self.hero = fight.return_hero()
            if not self.hero.is_alive():
                print('GAME OVER')
        else:
            print(f'Nothing in casting range {self.hero.spell.cast_range // 100}')
