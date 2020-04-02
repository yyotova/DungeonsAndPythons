class Weapon:
<<<<<<< HEAD
	
	def __init__(self,name,damage):
		self.name=name
		self.damage=damage
=======
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
>>>>>>> d5bddbad2c06ccdad54c9fa1fb78285e66a94683


