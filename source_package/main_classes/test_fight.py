import unittest
import sys
sys.path.append('.')
from source_package.main_classes.fight import Fight
from source_package.main_classes.hero import Hero
from source_package.main_classes.enemy import Enemy
from source_package.main_classes.weapon import Weapon
from source_package.main_classes.spell import Spell


class Test_Fight(unittest.TestCase):

    def test_fight_spell_enemy_hero(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        hero.learn(s)
        enemy = Enemy(200, 100, 20)
        enemy = Enemy(130, 100, 20)
        enemy.learn(s)
        hero.location = [0, 0]
        enemy.location = [0, 2]
        f = Fight(hero, enemy)
        print("\n test spell both \n")
        hero = f.mortal_kombat()
        self.assertEqual(f.return_hero().health, 0)

    def test_fight_spell_enemy_hero_none(self):
        hero = Hero(name = "Bron", title = "Dragonslayer", health = 100, mana = 100, mana_regeneration_rate=2)
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        # hero.learn(s)
        enemy = Enemy(100, 100, 20)
        enemy = Enemy(200, 100, 20)
        enemy = Enemy(130, 100, 20)
        enemy.learn(s)
        hero.location = [0, 0]
        enemy.location = [0, 2]
        f = Fight(hero, enemy)
        print("\ntest hero no spell enime has \n")
        f.mortal_kombat()
        self.assertEqual(f.return_hero().health, 0)

    def test_fight_hero_naked(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(100, 100, 20)
        hero.location = [0, 0]
        enemy.location = [0, 2]
        f = Fight(hero, enemy)
        print("\ntest hero nothing\n")
        f.mortal_kombat()
        self.assertEqual(f.return_hero().health, 0)

    def test_fight_weapon(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        enemy = Enemy(100, 100, 20)
        hero.location = [0, 0]
        enemy.location = [2, 1]
        f = Fight(hero, enemy)
        print("\ntest only weapon\n")
        f.mortal_kombat()
        self.assertEqual(f.return_hero().health, 20)

    def test_fight_spell_weapon(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        enemy = Enemy(100, 100, 20)
        hero.location = [0, 0]
        enemy.location = [2, 0]
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        hero.learn(s)
        f = Fight(hero, enemy)
        print("\ntest hero weapon spell\n")
        f.mortal_kombat()
        self.assertEqual(f.return_hero().health, 80)

    def test_fight_direct(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        enemy = Enemy(100, 100, 20)
        hero.location = [0, 0]
        enemy.location = [0, 0]
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        hero.learn(s)
        f = Fight(hero, enemy)
        print("\ntest hero fight one over the other\n")
        f.mortal_kombat()
        self.assertEqual(f.return_hero().health, 40)

    def test_fight_direct_spell_weak(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        hero.equip(w)
        enemy = Enemy(100, 100, 20)
        hero.location = [0, 0]
        enemy.location = [0, 0]
        s = Spell(name="Fireball", damage=10, mana_cost=50, cast_range=2)
        hero.learn(s)
        f = Fight(hero, enemy)
        print("\ntest hero fight one over the other\n")
        f.mortal_kombat()
        self.assertEqual(f.return_hero().health, 20)

if __name__ == '__main__':
    unittest.main()
