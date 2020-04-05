import unittest
import sys
sys.path.append('.')
from source_package.main_classes.hero import Hero
from source_package.main_classes.spell import Spell
from source_package.main_classes.weapon import Weapon


class TestHero(unittest.TestCase):
    def test_known_as_with_hero_returns_string(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        res = hero.known_as()

        self.assertEqual(res, 'Bron the Dragonslayer')

    def test_equip_hero_with_a_weapon_returns_heros_weapon(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)

        hero.equip(w)

        heros_weapon = hero.weapon

        self.assertEqual(heros_weapon, w)

    def test_equip_with_more_weapons_returns_last_weapon(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w1 = Weapon(name="The Axe of Destiny", damage=20)
        w2 = Weapon(name="The sword of Destiny", damage=30)

        hero.equip(w1)
        hero.equip(w2)

        heros_weapon = hero.weapon

        self.assertEqual(heros_weapon, w2)

    def test_learn_spell_when_hero_does_not_have_enough_mana_raise_an_error(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=20, mana_regeneration_rate=2)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

        exc = None
        try:
            hero.learn(s)
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Cannot cast that spell')

    def test_learn_spell_when_hero_has_enough_mana_returns_heros_spell(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

        hero.learn(s)
        heros_spell = hero.spell

        self.assertEqual(heros_spell, s)

    def test_learn_more_spells_when_hero_has_enough_mana_returns_heros_spell_equal_to_the_last_one(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s1 = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        s2 = Spell(name="Fireballs", damage=40, mana_cost=30, cast_range=2)

        hero.learn(s1)
        hero.learn(s2)
        heros_spell = hero.spell

        self.assertEqual(heros_spell, s2)


if __name__ == '__main__':
    unittest.main()
