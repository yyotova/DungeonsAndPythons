import sys
sys.path.append('.')
from source_package.main_classes.spell import Spell
from source_package.main_classes.weapon import Weapon

class Enemy(Weapon,Spell):
    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.weapon = None
        self.spell = None
        self.location=[]
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def learn(self, spell):
        if self.mana < spell.mana_cost:
            raise ValueError('Cannot cast that spell')
        else:
            self.spell = spell

    def equip(self, weapon):
        if self.damage < weapon.damage:
            self.weapon = weapon
            return weapon.damage

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        elif self.health == self.max_health:
            return False
        else:
            self.health += healing_points
            return True

    def take_mana(self, mana_points):
        if not self.mana == self.max_mana:
            self.mana += mana_points

    def attack(self, by):
        if by == 'weapon':
            if self.weapon is not None:
                return self.weapon.damage
            else:
                return self.damage
        else:
            if self.spell is not None:
                self.mana -= self.spell.mana_cost
                return self.spell.damage
            else:
                return self.damage