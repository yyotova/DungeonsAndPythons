class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __eq__(self, other):
        if other is not None:
            return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Hero has a spell: {self.name} with {self.damage} damage, {self.mana_cost} mana cost and {self.cast_range} cast range'
