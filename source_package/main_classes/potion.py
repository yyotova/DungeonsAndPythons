class Potion:
	def __init__(self, potion, points):
		self.potion = potion
		self.points = points

	def __eq__(self, other):
		return self.__dict__ == other.__dict__
