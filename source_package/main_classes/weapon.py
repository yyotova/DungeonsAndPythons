class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __eq__(self, other):
        if other is not None:
            return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Hero has a weapon {self.name} with {self.damage} damage'
