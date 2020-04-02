import unittest
from dungeon import Dungeon
from spell import Spell
from weapon import Weapon
from enemy import Enemy
from hero import Hero
class test_dungeon_class(unittest.TestCase):
	def test_dungeon_class_create_and_list(self):
		dungeon_map=[["S",".","#","#",".",".",".",".",".","T" ],
		["#","T","#","#",".",".","#","#","#","."],
		["#",".","#","#","#","E","#","#","#","E"],
		["#",".","E",".",".",".","#","#","#","."],
		["#","#","#","T","#","#","#","#","#","G"]
		]
		enemy_list=[Enemy(health=100, mana=100,damage=20),Enemy(health=100, mana=100,damage=10),Enemy(health=100, mana=100,damage=50),Enemy(health=100, mana=100,damage=30)]
		treasures=[Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2),Weapon(name="The Axe of Destiny", damage=20)]
		map=Dungeon(dungeon_map,treasures,enemy_list)
		map.fill_location_list()
		# print(map.__dict__)
		hero = Hero(name = "Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
		
		map.spawn(hero)
		# print(map.hero_location)
		map.print_map()
		print("==================================================")
		map.move_hero("right")
		map.print_map()
		# print(map.hero_location)
		print("==================================================")
		map.move_hero("down")
		map.print_map()
		print("==================================================")
		map.move_hero("up")
		map.print_map()
		# print(map.hero_location)
		print("==================================================")
		map.move_hero("up")
		map.print_map()
		# print(map.hero_location)
		print("==================================================")
		map.move_hero("right")
		map.print_map()
		# print(map.hero_location)
		print("==================================================")
		# print(map.test_hero())
if __name__ == '__main__':
		unittest.main()	