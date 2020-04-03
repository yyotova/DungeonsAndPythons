import unittest
import sys
sys.path.append('.')
from source_package.main_classes.fight import Fight
from source_package.main_classes.hero import Hero
from source_package.main_classes.enemy import Enemy
from source_package.main_classes.weapon import Weapon
from source_package.main_classes.spell import Spell
class Test_Fight(unittest.TestCase):
    def test_fight(self):
        hero = Hero(name = "Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        hero.learn(s)
        enemy=Enemy(100,100,20)
        hero.location=[0,0]
        enemy.location=[0,2]
        f=Fight(hero,enemy)
        hero=f.mortal_kombat()
        print(f.hero.health)
        print(f.enemy.health)
    def test_fight_weapon(self):
        hero = Hero(name = "Bron", title = "Dragonslayer", health = 100, mana = 100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        # s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        # hero.learn(s)
        enemy = Enemy(100, 100, 20)
        hero.location = [0, 0]
        enemy.location = [0, 2]
        f = Fight(hero, enemy)
        hero = f.mortal_kombat()
        print(f.hero.health)
        print(f.enemy.health)


    def test_fight_out_of_range(self):
        hero = Hero(name = "Bron", title = "Dragonslayer", health = 100, mana = 100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        hero.learn(s)
        enemy = Enemy(100, 100, 20)
        hero.location = [0, 0]
        enemy.location = [0, 4]
        f = Fight(hero, enemy)
        hero = f.mortal_kombat()
        

    #   # print(hero.__dict__)
    # def test_enemy_moving_o_hero(self):
    #   hero = Hero(name = "Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    #   w = Weapon(name="The Axe of Destiny", damage=20)
    #   hero.equip(w)
    #   enemy=Enemy(100,100,20)
    #   hero.location=[0,0]
    #   enemy.location=[2,1]
    #   print(hero.location)
    #   print(enemy.location)
    #   print("==================================")
    #   f=Fight(hero,enemy)
    #   f.enemy_move_to_hero()
    #   print(f.hero.location)
    #   print(f.enemy.location)
    #   print("==================================")
    #   f.enemy_move_to_hero()
    #   print(f.hero.location)
    #   print(f.enemy.location)
    #   print("==================================")
    #   f.enemy_move_to_hero()
    #   print(f.hero.location)
    #   print(f.enemy.location)
if __name__ == '__main__':
    unittest.main()