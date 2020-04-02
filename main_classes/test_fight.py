import unittest
from fight import Fight
from hero import Hero
from enemy import Enemy
from weapon import Weapon
class Test_Fight(unittest.TestCase):
	def test_fight(self):
		hero = Hero(name = "Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
		w = Weapon(name="The Axe of Destiny", damage=20)
		hero.equip(w)
		enemy=Enemy(100,100,20)
		f=Fight(hero,enemy)
		hero=f.mortal_kombat()
		print(f.hero.health)
		print(f.enemy.health)
		
		# print(hero.__dict__)

if __name__ == '__main__':
	unittest.main()