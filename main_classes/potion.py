class Potion:
	def __init__(self, name, points):
		self.name = name
		self.points = points

	def __eq__(self, other):
		return self.__dict__ == other.__dict__
