import unittest
from main_classes.potion import Potion
from main_classes.spell import Spell
from main_classes.weapon import Weapon
from main_classes.enemy import Enemy
from utls import convert_treasures_as_instance, convert_enemies_as_instance


class TestCaseConvertingTreasuers(unittest.TestCase):
    def test_converting_one_health_potion_into_instance(self):
        treasures = {'potion': [{'health': 20}]}
        res = convert_treasures_as_instance(treasures)
        exp = [Potion(potion='health', points=20)]

        self.assertEqual(res, exp)

    def test_converting_more_health_potions_into_instances(self):
        treasures = {'potion': [{'health': 20}, {'health': 40}]}
        res = convert_treasures_as_instance(treasures)
        exp = [Potion(potion='health', points=20), Potion(potion='health', points=40)]

        self.assertEqual(res, exp)

    def test_converting_health_potion_and_mana_potion_into_instances(self):
        treasures = {'potion': [{'health': 20}, {'health': 40}, {'mana': 45.5}]}
        res = convert_treasures_as_instance(treasures)
        exp = [Potion(potion='health', points=20), Potion(potion='health', points=40), Potion(potion='mana', points=45.5)]

        self.assertEqual(res, exp)

    def test_converting_one_spell_into_instance(self):
        treasures = {'spell': [{'name': 'Pfu', 'damage': 20, 'mana_cost': 20, 'cast_range': 2}]}
        res = convert_treasures_as_instance(treasures)
        exp = [Spell(name='Pfu', damage=20, mana_cost=20, cast_range=2)]

        self.assertEqual(res, exp)

    def test_converting_more_spells_into_instances(self):
        treasures = {'spell': [{'name': 'Pfu', 'damage': 20, 'mana_cost': 20, 'cast_range': 2},
        {"name": "Abrakadabra", "damage": 28, "mana_cost": 29, "cast_range": 2}]}
        res = convert_treasures_as_instance(treasures)
        exp = [Spell(name='Pfu', damage=20, mana_cost=20, cast_range= 2), Spell(name='Abrakadabra', damage=28, mana_cost=29, cast_range=2)]

        self.assertEqual(res, exp)

    def test_converting_one_weapon_into_instance(self):
        treasures = {'weapon': [{'name': 'Axe', 'damage': 30}]}
        res = convert_treasures_as_instance(treasures)
        exp = [Weapon(name='Axe', damage=30)]

        self.assertEqual(res, exp)

    def test_converting_more_weapons_into_instances(self):
        treasures = {'weapon': [{'name': 'Axe', 'damage': 30}, {"name": "Axe2", "damage": 10.5}]}
        res = convert_treasures_as_instance(treasures)
        exp = [Weapon(name='Axe', damage=30), Weapon(name='Axe2', damage=10.5)]

        self.assertEqual(res, exp)

    def test_converting_into_instance_different_treasures(self):
        treasures = {
        'potion': [{'health': 20}, {'mana': 30}],
        'spell': [
            {'name': 'Pfu', 'damage': 20, 'mana_cost': 20, 'cast_range': 2},
            {"name": "Abrakadabra", "damage": 28, "mana_cost": 29, "cast_range": 2}
            ],
        'weapon': [
            {'name': 'Axe', 'damage': 30},
            {"name": "Axe2", "damage": 10.5}
            ]
        }

        res = convert_treasures_as_instance(treasures)

        exp = [Potion(potion='health', points=20), Potion(potion='mana', points=30),
        Spell(name='Pfu', damage=20, mana_cost=20, cast_range=2),
        Spell(name='Abrakadabra', damage=28, mana_cost=29, cast_range=2),
        Weapon(name='Axe', damage=30), Weapon(name='Axe2', damage=10.5)]

        self.assertEqual(res, exp)


class TestConvertingEnemies(unittest.TestCase):
    def test_converting_enemies_as_instnace_returns_list_with_inctances(self):
        enemies = {
        'enemy': [
            {"health": 100, "damage": 10, "mana": 150},
            {"health": 200, "damage": 20, "mana": 100},
            {"health": 150, "damage": 50, "mana": 90},
            {"health": 180, "damage": 5, "mana": 50}
            ]
        }
        res = convert_enemies_as_instance(enemies)
        exp = [ Enemy(health=100, damage=10, mana=150), Enemy(health=200, damage=20, mana=100), 
        Enemy(health=150, damage=50, mana=90), Enemy(health=180, damage=5, mana=50) ]

        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
