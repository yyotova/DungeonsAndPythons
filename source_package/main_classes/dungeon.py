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
                locations.append([i, j])

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

    def fill_location_list(self):
        self.set_obstacle_location()
        self.set_enemy_location()
        self.set_spawn_location()
        self.set_treasure_location()

    def spawn(self, hero):
        self.set_spawn_location()
        if len(self.spawn_locations) == 0:
            return False
        else:
            if self.hero is not None:
                self.remove_hero_from_map()
                self.hero = hero
                self.hero.location = self.spawn_locations[0]
                self.spawn_locations.remove(self.spawn_locations[0])
                self.put_hero_on_map()
            else:
                self.hero = hero
                self.hero.location = self.spawn_locations[0]
                self.spawn_locations.remove(self.spawn_locations[0])
                self.put_hero_on_map()

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
            new_x = self.hero.location[0] - 1
            new_y = self.hero.location[1]
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_x >= 0:
                self.remove_hero_from_map()
                self.hero.location[0] -= 1
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()
                self.put_hero_on_map()

        elif direction == "DOWN":
            new_x = self.hero.location[0] + 1
            new_y = self.hero.location[1]
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_x < len(self.map):
                self.remove_hero_from_map()
                self.hero.location[0] += 1
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()
                self.put_hero_on_map()

        elif direction == "RIGHT":
            new_x = self.hero.location[0]
            new_y = self.hero.location[1] + 1
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_y < len(self.map[0]):
                self.remove_hero_from_map()
                self.hero.location[1] += 1
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()
                self.put_hero_on_map()

        elif direction == "LEFT":
            new_x = self.hero.location[0]
            new_y = self.hero.location[1] - 1
            if not check_for_something([new_x, new_y], self.obstacle_localtions) and new_y >= 0:
                self.remove_hero_from_map()
                self.hero.location[1] -= 1
                self.hero.add_mana_from_regeneration_rate()
                self.check_for_treasure()
                self.check_for_enemy()
                self.put_hero_on_map()

    def remove_hero_from_map(self):
        hero_point_x = self.hero.location[0]
        hero_point_y = self.hero.location[1]
        self.map[hero_point_x][hero_point_y] = "."

    def put_hero_on_map(self):
        hero_point_x = self.hero.location[0]
        hero_point_y = self.hero.location[1]
        self.map[hero_point_x][hero_point_y] = "H"

    def check_for_treasure(self):
        if check_for_something(self.hero.location, self.treasure_locations) is True:
            treasure = random_treasure(convert_treasures_as_instance(read_from_file_with_treasures('treasures.txt')))
            if treasure.__class__.__name__ == 'Potion':
                if treasure.potion == 'health':
                    self.hero.take_healing(treasure.points)
                else:
                    self.hero.take_mana(treasure.points)
            elif treasure.__class__.__name__ == 'Spell':
                self.hero.learn(treasure)
            else:
                self.hero.equip(treasure)

    def check_for_enemy(self):
        if check_for_something(self.hero.location, self.enemy_locations) is True:
            enemy = random_enemy(convert_enemies_as_instance(read_from_file_with_enemies('enemies.txt')))
            fight = Fight(self.hero, enemy)
            fight.mortal_kombat()
            self.hero = fight.rerun_hero()

            if not self.hero.is_alive():
                print('GAME OVER')

    def hero_attack(self, by):
        if by == 'spell':
            hero_x = self.hero.location[0]
            hero_y = self.hero.location[1]
            nearest_enemies = []
            cast_range = self.hero.spell.cast_range

            for enemy in self.enemy_locations:
                if enemy[0] >= hero_x - cast_range and enemy[0] <= hero_x + cast_range:
                    nearest_enemies.append(enemy)
                elif enemy[1] >= hero_y - cast_range and enemy[1] <= hero_y + cast_range:
                    nearest_enemies.append(enemy)

            if len(nearest_enemies) > 0:
                enemy = random_enemy(read_from_file_with_enemies('enemies.txt'))
                # getting first coordinates in the list
                enemy.location = nearest_enemies[0]
                fight = Fight(self.hero, enemy)
                fight.mortal_kombat()
                self.hero = fight.return_hero()
                if not self.hero.is_alive():
                    print('GAME OVER')
            else:
                print(f'Nothing in casting range {self.hero.spell.cast_range}')
        else:
            print('There is no enemy to attack')
