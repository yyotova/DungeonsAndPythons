import unittest
from main_classes.potion import Potion
from main_classes.spell import Spell
from main_classes.weapon import Weapon
from utls import convert_into_treasures_as_instance

class TestCaseConvertingTreasuers(unittest.TestCase):
    def test_converting_one_health_potion_into_instance(self):
        treasures = {'potion': [{'health': 20}]}
        res = convert_into_treasures_as_instance(treasures)
        exp = [Potion('health', 20)]

        self.assertEqual(res, exp)

    def test_converting_more_health_potions_into_instances(self):
        treasures = {'potion': [{'health': 20}, {'health': 40}]}
        res = convert_into_treasures_as_instance(treasures)
        exp = [Potion('health', 20), Potion('health', 40)]

        self.assertEqual(res, exp)

    def test_converting_health_potion_and_mana_potion_into_instances(self):
        treasures = {'potion': [{'health': 20}, {'health': 40}, {'mana': 45.5}]}
        res = convert_into_treasures_as_instance(treasures)
        exp = [Potion('health', 20), Potion('health', 40), Potion('mana', 45.5)]

        self.assertEqual(res, exp)

    def test_converting_one_spell_into_instance(self):
        treasures = {'spell': [{'name': 'Pfu', 'damage': 20, 'mana_cost': 20, 'cast_range': 2}]}
        res = convert_into_treasures_as_instance(treasures)
        exp = [Spell('Pfu', 20, 20, 2)]

        self.assertEqual(res, exp)

    def test_converting_more_spells_into_instances(self):
        treasures = {'spell': [{'name': 'Pfu', 'damage': 20, 'mana_cost': 20, 'cast_range': 2},
        {"name": "Abrakadabra","damage": 28,"mana_cost": 29,"cast_range": 2}] }
        res = convert_into_treasures_as_instance(treasures)
        exp = [Spell('Pfu', 20, 20, 2), Spell('Abrakadabra', 28, 29, 2)]

        self.assertEqual(res, exp)

    def test_converting_one_weapon_into_instance(self):
        treasures = {'weapon': [{'name': 'Axe', 'damage': 30}]}
        res = convert_into_treasures_as_instance(treasures)
        exp = [Weapon('Axe', 30)]

        self.assertEqual(res, exp)

    def test_converting_more_weapons_into_instances(self):
        treasures = {'weapon': [{'name': 'Axe', 'damage': 30}, {"name": "Axe2","damage": 10.5}]}
        res = convert_into_treasures_as_instance(treasures)
        exp = [Weapon('Axe', 30), Weapon('Axe2', 10.5)]

        self.assertEqual(res, exp)

    def test_converting_into_instance_different_treasures(self):
        treasures = {
        'potion': [{'health': 20}, {'mana': 30}], 
        'spell': [
            {'name': 'Pfu', 'damage': 20, 'mana_cost': 20, 'cast_range': 2},
            {"name": "Abrakadabra","damage": 28,"mana_cost": 29,"cast_range": 2}
            ], 
        'weapon': [
            {'name': 'Axe', 'damage': 30},
            {"name": "Axe2","damage": 10.5}
            ]
        }

        res = convert_into_treasures_as_instance(treasures)

        exp = [Potion('health', 20), Potion('mana', 30), Spell('Pfu', 20, 20, 2), Spell('Abrakadabra', 28, 29, 2),
        Weapon('Axe', 30), Weapon('Axe2', 10.5)]

        self.assertEqual(res, exp)

if __name__ == '__main__':
    unittest.main()