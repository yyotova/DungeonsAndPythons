from source_package.main_classes.hero import Hero
from source_package.main_classes.enemy import Enemy
import sys
sys.path.append('.')


class Fight(Hero, Enemy):

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def hero_hit_enemy(self):
        if self.hero.spell:
            if self.hero.mana >= self.hero.spell.mana_cost and self.hero.spell.damage >= self.hero.weapon.damage:
                self.enemy.take_damage(self.hero.attack(by="spell"))
                print("Hero hits enemy with {0} for {1} enemy health={2}".format(self.hero.spell.name, self.hero.spell.damage, self.enemy.health))
            else:
                self.enemy.take_damage(self.hero.attack(by="weapon"))
                if self.hero.weapon is None:
                    print("Hero hits enemy for 0 enemy health={0}".format(self.enemy.health))
                else:
                    print("Hero hits enemy with {0} for {1} enemy health={2}".format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health))
        else:
            self.enemy.take_damage(self.hero.attack(by="weapon"))
            if self.hero.weapon is None:
                print("Hero hits enemy for 0 enemy health={0}".format(self.enemy.health))
            else:
                print("Hero hits enemy with {0} for {1} enemy health={2}".format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health))

    def enemy_hit_hero(self):
        if self.enemy.spell:
            if self.enemy.mana < self.enemy.spell.mana_cost and self.enemy.spell.damage >= self.enemy.damage:
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

    def hero_in_line_of_object(self):
        # made because spell can only be cast in straight line
        if self.hero.location[0] == self.enemy.location[0]:
            return True
        elif self.hero.location[1] == self.enemy.location[1]:
            return True
        else:
            return False

    def enemy_in_casting_range(self):
        if self.enemy.location.count(0) == 1:
            return self.hero.spell.cast_range >= (sum(self.enemy.location) / 1)
        else:
            return self.hero.spell.cast_range >= (sum(self.enemy.location) / 2)

    def hero_in_casting_range(self):
        if self.hero.location.count(0) == 1:
            return self.enemy.spell.cast_range >= (sum(self.hero.location) / 1)
        else:
            return self.enemy.spell.cast_range >= (sum(self.hero.location) / 2)

    def enemy_move_to_hero(self):
        if self.hero.location != self.enemy.location:
            # move up or down first
            if self.hero.location[0] != self.enemy.location[0]:
                if self.hero.location[0] > self.enemy.location[0]:
                    self.enemy.location[0] += 100
                    print("Enemy moves one step down to get to hero")
                else:
                    self.enemy.location[0] -= 100
                    print("Enemy moves one step up to get to hero")
            # move left or right
            else:
                if self.hero.location[1] != self.enemy.location[1]:
                    if self.hero.location[1] > self.enemy.location[1]:
                        self.enemy.location[1] += 100
                        print("Enemy moves one step right to get to hero")
                    else:
                        self.enemy.location[1] -= 100
                        print("Enemy moves one step left to get to hero")

    def hero_move_to_enemy(self):
        if self.hero.location != self.enemy.location:
            # move up or down first
            if self.hero.location[0] != self.enemy.location[0]:
                if self.enemy.location[0] > self.hero.location[0]:
                    self.hero.location[0] += 100
                    print("Hero moves one step down to get to enemy")
                else:
                    self.hero.location[0] -= 100
                    print("Hero moves one step up to get to enemy")
            # move left or right
            else:
                if self.enemy.location[1] != self.hero.location[1]:
                    if self.enemy.location[1] > self.hero.location[1]:
                        self.hero.location[1] += 100
                        print("Hero moves one step right to get to enemy")
                    else:
                        self.hero.location[1] -= 100
                        print("Hero moves one step left to get to enemy")

    def return_hero(self):
        return self.hero

    def enemy_over_hero(self):
        return self.hero.location == self.enemy.location

    def enemy_game_turn(self, game_turn):
        if self.enemy.is_alive() and self.hero.is_alive():
            # stop dead object form doing a turn
            if self.enemy.spell and self.enemy.mana >= self.enemy.spell.mana_cost:
                self.enemy_hit_hero()
            else:
                if self.enemy_over_hero():
                    self.enemy_hit_hero()
                else:
                    self.enemy_move_to_hero()
            game_turn += 1
        return game_turn

    def hero_game_turn(self, game_turn):
        if self.enemy.is_alive() and self.hero.is_alive():
            if self.hero.spell and self.hero.mana >= self.hero.spell.mana_cost:
                self.hero_hit_enemy()
            else:
                if self.enemy_over_hero():
                    self.hero_hit_enemy()
                else:
                    self.hero_move_to_enemy()
            game_turn += 1
        return game_turn

    def mortal_kombat(self):
        game_turn = 1
        while self.hero.health > 1 and self.enemy.health > 1:
            # check for hero spell
            if self.hero.spell:
                # if self.hero_in_line_of_object() and self.enemy_in_casting_range():

                if game_turn % 2 == 0:
                    game_turn = self.enemy_game_turn(game_turn)

                if game_turn % 2 != 0:
                    game_turn = self.hero_game_turn(game_turn)

            # do if enemy has spell and hero doesnt have a spell
            if self.hero.spell is None and self.enemy.spell:
                # if self.hero_in_line_of_object() and self.hero_in_casting_range():

                if game_turn % 2 == 0:
                    game_turn = self.enemy_game_turn(game_turn)

                if game_turn % 2 != 0:
                    game_turn = self.hero_game_turn(game_turn)

            if self.hero.spell is None and self.enemy_over_hero() is False and self.enemy.spell is None:
                self.enemy_move_to_hero()
                game_turn += 1

                if game_turn % 2 == 0:
                    game_turn += 1

            if self.enemy_over_hero():

                if game_turn % 2 == 0:
                    game_turn = self.enemy_game_turn(game_turn)

                if game_turn % 2 != 0:
                    game_turn = self.hero_game_turn(game_turn)

        if self.hero.health <= 0:
            print("Hero is dead")
        else:
            print("Enemy is dead")


'''
Fight class works with game turns the hero is first and the enemy is second
it covers the cases :
hero has spell and weapon enemy has weapon or none -> hero attacks with spell then with weapon enemy gets to hero then attack
hero has spell and weapon enemy has spell and weapon -> hero attacks wiht spell enemy attacks with spell when mana is over they use wepaons enemy gets to hero
hero casts out of range -> return Nothing to hit
hero has nothing -> enemy kills hero hero makes 0 dmg
hero doesnt have spell enemy has spell -> enemy attacks hero hero gets to enemy then attacks
'''
