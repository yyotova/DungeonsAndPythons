import unittest
from read_file import read_from_file
class test_read_from_file(unittest.TestCase):
	def test_read_from_file_func(self):
		res, tre=read_from_file("level1.txt")
		exp=[
		["S",".","#","#",".",".",".",".",".","T" ],
		["#","T","#","#",".",".","#","#","#","."],
		["#",".","#","#","#","E","#","#","#","E"],
		["#",".","E",".",".",".","#","#","#","."],
		["#","#","#","T","#","#","#","#","#","G"]
		]
		self.assertEqual(res,exp)
		self.assertEqual(tre, ["health","mana","weapon"])

if __name__ == '__main__':
	unittest.main()