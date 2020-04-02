class Spell:
<<<<<<< HEAD
	
	def __init__(self,name,damage,mana_cost,cast_range):
		self.name
		self.damage=damage
		self.mana_cost=mana_cost
		self.cast_range=cast_range
=======
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
>>>>>>> d5bddbad2c06ccdad54c9fa1fb78285e66a94683

