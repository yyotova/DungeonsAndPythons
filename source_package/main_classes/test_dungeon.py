import unittest
import sys
sys.path.append('.')

from source_package.file_manipulation.read_file import read_from_file_with_first_level
from source_package.main_classes.dungeon import Dungeon
# from source_package.main_classes.spell import Spell
# from source_package.main_classes.weapon import Weapon
# from source_package.main_classes.enemy import Enemy
from source_package.main_classes.hero import Hero


class test_dungeon_class(unittest.TestCase):
    # def test_creating_dungeon_and_print_it(self):

    #     dungeon = Dungeon("level1.txt")
    #     dungeon.print_map()

    # def test_set_obstacle_locations_returns_obstacle_coordinations(self):
    #     dungeon = Dungeon("level1.txt")

    #     dungeon.set_obstacle_location()
    #     exp = [[0, 2], [0, 3], [1, 0], [1, 2], [1, 3], [1, 6], [1, 7], [1, 8], [2, 0], [2, 2], [2, 3],
    #     [2, 4], [2, 6], [2, 7], [2, 8], [3, 0], [3, 6], [3, 7], [3, 8],
    #     [4, 0], [4, 1], [4, 2], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8]]

        # self.assertEqual(dungeon.obstacle_localtions, exp)

    # def test_set_treasures_locations_returns_treasures_coordinations(self):
    #     dungeon = Dungeon("level1.txt")

    #     dungeon.set_treasure_location()
    #     exp = [[0, 9], [1, 1], [4, 3]]

    #     self.assertEqual(dungeon.treasure_locations, exp)

    # def test_set_enemies_locations_returns_enemies_coordinations(self):
    #     dungeon = Dungeon("level1.txt")

    #     dungeon.set_enemy_location()
    #     exp = [[2, 5], [2, 9], [3, 2]]

    #     self.assertEqual(dungeon.enemy_locations, exp)

    # def test_spawn_hero_when_there_are_no_spawning_points_return_false(self):
    #     dungeon = Dungeon("level1.txt")
    #     hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    #     res = dungeon.spawn(hero)
    #     self.assertEqual(res, False)

    # def test_spawn_hero_when_there_is_one_spawning_point_returns_hero_on_map(self):
    #     dungeon = Dungeon("level1.txt")
    #     hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    #     dungeon.spawn(hero)

    #     spawn_locations_exp = []

    #     self.assertEqual(dungeon.hero, hero)
    #     self.assertEqual(dungeon.spawn_locations, spawn_locations_exp)
    #     dungeon.print_map()

    # def test_spawn_hero_when_there_are_more_spawning_points_returns_hero_on_map(self):
    #     dungeon = Dungeon("level1.txt")
    #     hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    #     dungeon.spawn(hero)
    #     dungeon.spawn(hero)
    #     spawn_locations_exp = [[3, 5]]

    #     self.assertEqual(dungeon.hero, hero)
    #     self.assertEqual(dungeon.spawn_locations, spawn_locations_exp)
    #     dungeon.print_map()

    # def test_move_hero_up_if_there_is_a_bounder(self):
    #     dungeon = Dungeon("level1.txt")
    #     hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    #     dungeon.spawn(hero)
    #     dungeon.move_hero("Up")
    #     dungeon.print_map()
    # def test_move_hero_up_if_there_is_no_bounder_obstacle_enemy_or_treasure(self):
    #     dungeon = Dungeon("level1.txt")
    #     hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    #     dungeon.spawn(hero)

    #     print(dungeon.obstacle_localtions)
    #     print(dungeon.hero.location)
    #     dungeon.move_hero("Up")

    # def test_move_hero_up_if_there_is_treasure(self):
    #     dungeon = Dungeon("level1.txt")
    #     # T.##.....T
    #     # ST##..###.
    #     # #.###E###E
    #     # #.E...###.
    #     # ###T#####G
    #     hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    #     dungeon.spawn(hero)
    #     dungeon.move_hero("Up")
    #     dungeon.print_map()

    # def test_move_hero_up_if_there_is_enemy(self):
    #     dungeon = Dungeon("level1.txt")
    #     # E.##.....T
    #     # ST##..###.
    #     # #.###E###E
    #     # #.E...###.
    #     # ###T#####G
    #     hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    #     dungeon.spawn(hero)
    #     dungeon.move_hero("Up")
    #     dungeon.print_map()

    def test_move_into_treasure_which_is_health_potion_returns_heros_new_health(self):
        dungeon = Dungeon("level1.txt")
    #     # T.##.....T
    #     # ST##..###.
    #     # #.###E###E
    #     # #.E...###.
    #     # ###T#####G
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        dungeon.spawn(hero)
        dungeon.move_hero('Up')
        pass

if __name__ == '__main__':
        unittest.main()
