import unittest
from read_file import (read_from_file_with_first_level,
                    read_from_file_with_treasures,
                    read_from_file_with_enemies)

class test_read_from_file(unittest.TestCase):

    def test_read_from_file_with_first_level_returns_list_with_each_line_as_list_of_strings(self):
        res = read_from_file_with_first_level("level1.txt")
        exp=[
        ["S",".","#","#",".",".",".",".",".","T" ],
        ["#","T","#","#",".",".","#","#","#","."],
        ["#",".","#","#","#","E","#","#","#","E"],
        ["#",".","E",".",".",".","#","#","#","."],
        ["#","#","#","T","#","#","#","#","#","G"]
        ]
        
        self.assertEqual(res,exp)

    def test_read_from_file_with_treasures_returns_dic_with_each_treasure_as_dict(self):
        res = read_from_file_with_treasures('treasures.txt')
        exp = {
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
        self.assertEqual(res,exp)


    def test_read_from_file_with_enemies_returns_dict_with_each_enemy_as_dict(self):
        res = read_from_file_with_enemies('enemies.txt')
        exp = {
        'enemy': [
            {"name": "Targaryen","damage": 100, "mana_cost": 100,"cast_range": 2},
            {"name":"Lannister", "damage": 100,"mana_cost": 100,"cast_range": 2},
            {"name":"Stark", "damage": 100, "mana_cost":100,"cast_range": 2},
            {"name":"Baratheon", "damage": 100,"mana_cost": 100, "cast_range":2}
            ]
        }

        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()