# DungeonsAndPythons :snake:
This is a simple 2D, turn-based console game filled with dungeons and
pythons. There are a hero, enemies, weapons, treasures, and magic!
There is an uncomplicated UI where the user can move his hero, take
treasures, and fight with the enemies. When he fights all enemies on his
path to the end of the dungeon, he will reach the next level or wins the
game

### Requirements
``` pip install -r requirements.txt```

### UI
We use pygame library. 
So you can use ←, ↑, →, ↓ to move the hero who is in white. The enemies are in black and the treasures in red. You can attack by a spell, pressing the space button. So if the enemy is in range of the spell it will take damage to him.


## Characters

### Hero
Our hero starts with the given health and mana points. Those health and mana points are the maximum health and mana for the hero!
* When a hero reaches 0 health he is considered dead.
* When a hero reaches 0 mana, he cannot cast any spells.
The hero has the following methods:
* ***known_as()*** - returns a string, formatted in the following way: ```"{hero_name} the {hero_title}"```
* ***get_health()*** - returns the current ```health```
* ***get_mana()*** -  returns the current ```mana```
* ***is_alive()*** -  returns ```True```, if our hero is still alive. Otherwise -```False```.
* ***can_cast()*** - returns ```True```, if our hero can cast the magic he has been given. Otherwise - ```False```
* ***take_damage(damage_points)*** -  reduces the hero's health by ```damage```. If we inflict more damage than we have health, health will always be equal to zero and we cannot get below that!
* ***take_healing(healing_points)*** - Our hero can be healed! This method heals our hero.
If our hero is dead, the method should return False. It's too late to heal our hero. If our hero is dead, the method should return False. It's too late to heal our hero. If healing is successful (Our hero is not dead), the method should return True.
* ***take_mana(mana_points)*** -  increases his mana in two ways. 
1. Each time he makes a move, his mana is increased by mana_regeneration_rate amount.
2. He can drink a mana potion, which will increase his mana by the number of mana points the potion has.
Hero's mana cannot go above the start mana given to him, neither he can go down below 0 mana.

* ***equip(weapon)*** - Our hero can equip one weapon and one spell to have damage.
* ***learn(spell)*** - Our hero can learn only 1 spell at a time.
If you learn a given spell, and after this learn another one, the hero can use only the latest.
* ***attack()*** - returns the damage done either from the weapon or from the spell.
If the hero has not been equipped with weapons or he has no spells, his attack points are 0.

The method can be called in two ways:

- attack(by="weapon") - returns the damage of the weapon if equipped or 0 otherwise
- attack(by="magic") - returns the damage of the spell, if equipped or 0 otherwise

### Enemy
Enemy has the following methods just like our hero.
* ```is_alive()```
* ```can_cast()```
* ```get_health()```
* ```get_mana()```
* ```take_healing()```
* ```take_mana()```
* ```attack()```
* ```take_damage(damage)```

Enemies cannot regenerate mana!
Enemies have starting damage, which is different from a weapon or a spell. They can equip weapons or learn spells but it is not required for them to deal with the damage, as it is for our hero.

## Weapons and spells
We have ```treasures.txt``` file that contains the information about possible weapons' and spells' attributes. For our hero to have proper damage, he must be equipped with either a weapon or a spell. One hero can carry at max 1 weapon and 1 spell.

## Dungeon
This is a 2D map that we load from a file.
There are spawn points for different levels, obstacles, treasures, enemies, and a gateway, which is the end of the dungeon.

## Fights
Our hero must fight his enemies to reach the exit of the dungeon.
A fight happens when:
* Our hero walks into the same position as the enemy - then the fights start automatically.
* Our hero is within some range of the enemy. Then we can attack our enemy with a spell.

The fight follows this algorithm:
* Our hero always attacks first.
* We always use the attack that deals more damage.
* If our weapon and our spell deal the same amount of damage, use the spell first.
* When you run out of mana, use the weapon (if any)