from source_package.main_classes.hero import Hero
from source_package.main_classes.enemy import Enemy
<<<<<<< HEAD
import sys
sys.path.append('.')

=======
>>>>>>> fix mortal kombat

class Fight(Hero, Enemy):
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def hero_hit_enemy(self):
        if self.hero.spell:
<<<<<<< HEAD
            if self.hero.mana < self.hero.spell.mana_cost:
                self.enemy.take_damage(self.hero.attack(by="weapon"))
            else:
                self.enemy.take_damage(self.hero.attack(by="spell"))
        else:
            self.enemy.take_damage(self.hero.attack(by="weapon"))

    def enemy_hit_hero(self):
        if self.enemy.spell:
            if self.enem.mana < self.enemy.spell.mana_cost:
                self.hero.take_damage(self.enemy.attack(by="weapon"))
            else:
                self.hero.take_damage(self.enemy.attack(by="spell"))
        else:
            self.hero.take_damage(self.enemy.attack(by="weapon"))
=======
            if self.hero.mana >= self.hero.spell.mana_cost:
                self.enemy.take_damage(self.hero.attack(by="spell"))
                print("Hero hits enemy with {0} for {1} enemy health={2}".format(self.hero.spell.name, self.hero.spell.damage, self.enemy.health))
            else:
                self.enemy.take_damage(self.hero.attack(by="weapon"))
                if self.hero.weapon is None:
                    print("Hero hits enemy for 0 enemy health={1}".format(self.enemy.health))
                else:
                    print("Hero hits enemy with {0} for {1} enemy health={2}".format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health))
        else:
            self.enemy.take_damage(self.hero.attack(by="weapon"))
            if self.hero.weapon is None:
                print("Hero hits enemy for 0 enemy health={1}".format(self.enemy.health))
            else:
                print("Hero hits enemy with {0} for {1} enemy health={2}".format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health))

    def enemy_hit_hero(self):
        if self.enemy.spell:
            if self.enemy.mana < self.enemy.spell.mana_cost:
                self.hero.take_damage(self.enemy.attack(by="weapon"))
                if self.enemy.weapon is None:
                    print("Enemy hits hero for {0} hero health={1}".format(self.enemy.damage, self.hero.health))
                else:
                    print("Enemy hits hero with {0} for {1} hero health={2}".format(self.enemy.weapon.name, self.enemy.weapon.damage, self.hero.health))
            else:
                self.hero.take_damage(self.enemy.attack(by="spell"))
                print("Enemy hits hero with {0} for {1} hero health={2}".format(self.enemy.spell.name, self.enemy.spell.damage, self.hero.health))
        else:
            self.hero.take_damage(self.enemy.attack(by="weapon"))
            if self.enemy.weapon is None:
                print("Enemy hits hero for {0} hero health={1}".format(self.enemy.damage, self.hero.health))
            else:
                print("Enemy hits hero with {0} for {1} hero health={2}".format(self.enemy.weapon.name, self.enemy.weapon.damage, self.hero.health))
>>>>>>> fix mortal kombat

    def hero_in_line_of_object(self):
        # made because spell can only be cast in straight line
        if self.hero.location[0] == self.enemy.location[0]:
            return True
        elif self.hero.location[1] == self.enemy.location[1]:
            return True
        else:
            return False

    def enemy_in_casting_range(self):
<<<<<<< HEAD
        return self.hero.spell.cast_range >= (sum(self.enemy.location) / 2)
=======
        if self.enemy.location.count(0) == 1:
            return self.hero.spell.cast_range >= (sum(self.enemy.location) / 1)
        else:
            return self.hero.spell.cast_range >= (sum(self.enemy.location) / 2)
>>>>>>> fix mortal kombat

    def enemy_move_to_hero(self):
        if self.hero.location != self.enemy.location:
            # move up or down first
            if self.hero.location[0] != self.enemy.location[0]:
                if self.hero.location[0] > self.enemy.location[0]:
                    self.enemy.location[0] += 1
<<<<<<< HEAD
                else:
                    self.enemy.location[0] -= 1
            # move left or right
            # if self.hero.location[0] == self.enemy.location[0]:
=======
                    print("Enemy moves one step down to get to hero")
                else:
                    self.enemy.location[0] -= 1
                    print("Enemy moves one step up to get to hero")
            # move left or right
>>>>>>> fix mortal kombat
            else:
                if self.hero.location[1] != self.enemy.location[1]:
                    if self.hero.location[1] > self.enemy.location[1]:
                        self.enemy.location[1] += 1
<<<<<<< HEAD
                    else:
                        self.enemy.location[1] -= 1
=======
                        print("Enemy moves one step right to get to hero")
                    else:
                        self.enemy.location[1] -= 1
                        print("Enemy moves one step left to get to hero")
>>>>>>> fix mortal kombat

    def enemy_over_hero(self):
        return self.hero.location == self.enemy.location

    def mortal_kombat(self):
        game_turn = 1
        while self.hero.health > 0 and self.enemy.health > 0:
            if self.hero.spell:
                if self.hero_in_line_of_object() and self.enemy_in_casting_range():
                    if game_turn % 2 == 0:
                        if self.enemy_over_hero():
                            self.enemy_hit_hero()
<<<<<<< HEAD
                            print("Enemy hits hero for {0} hero healt = {1}".format(self.enemy.damage, self.hero.health))
                        else:
                            self.enemy_move_to_hero()
                            print("Enemy moves to hero")
                        game_turn += 1
                    if game_turn % 2 != 0:
                        self.hero_hit_enemy()
                        print("hero hits enemy for {0} enemy health={1}".format(self.hero.spell.damage,self.enemy.health))
                        game_turn += 1
                else:
                    print("Not in range spell")
            # print(game_turn)
            if self.hero.spell == None and self.enemy_over_hero() == False:
                self.enemy_move_to_hero()
                print("Enemy moves to hero hero waits because he is smart")
                game_turn += 1
            if self.enemy_over_hero():
                if game_turn % 2 == 0:
                    self.enemy_hit_hero()
                    print("Enemy hits hero for {0} hero health = {1}".format(self.enemy.damage, self.hero.health))
                    game_turn += 1
                if game_turn % 2 != 0:
                    self.hero_hit_enemy()
                    print("hero hits enemy for {0} enemy health = {1}".format(self.hero.weapon.damage, self.enemy.health))
                    game_turn += 1
            # else:
            #   print("Not in range")
            # game_turn+=1

        return self.hero
=======
                        else:
                            self.enemy_move_to_hero()
                        game_turn += 1
                    if game_turn % 2 != 0:
                        self.hero_hit_enemy()
                        game_turn += 1
                else:
                    print("Nothing in casting range {0}".format(self.hero.spell.cast_range))
                    return
            if self.hero.spell is None and self.enemy_over_hero() is False:
                self.enemy_move_to_hero()
                game_turn += 1

            if self.enemy_over_hero():
                if game_turn % 2 == 0:
                    self.enemy_hit_hero()
                    game_turn += 1
                if game_turn % 2 != 0:
                    self.hero_hit_enemy()
                    game_turn += 1

        return self.hero
>>>>>>> fix mortal kombat
