class Potion:
    def __init__(self, potion, points):
        self.potion = potion
        self.points = points

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Hero has {self.points} points {self.potion} potion'
