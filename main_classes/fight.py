from hero import Hero
from enemy import Enemy
class Fight(Hero,Enemy):

	def __init__(self,hero,enemy):
		self.hero=hero
		self.enemy=enemy

	def mortal_kombat(self):
		
	