from hero import Hero
from enemy import Enemy
class Fight(Hero,Enemy):

	def __init__(self,hero,enemy):
		self.hero=hero
		self.enemy=enemy
	
	def hero_in_line_of_object(self):
		if hero.location[0]==enemy.location[0]:
			return True
		elif hero.location[1]==enemy.location[1]:
			return True
		else:
			return False

	def mortal_kombat(self):
		game_turn=1
		while self.hero.health>0 and self.enemy.health>0:

			if self.hero.location==self.enemy.location:
				if game_turn%2==0:
					self.hero.take_damage(self.enemy.attack(by="weapon"))
				if game_turn%2!=0:
					self.enemy.take_damage(self.hero.attack(by="weapon"))
			game_turn+=1
	

		return self.hero	
	