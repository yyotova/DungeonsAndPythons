class Weapon:
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage

    def __eq__(self, other):
        if other!=None:
            return self.__dict__ == other.__dict__
