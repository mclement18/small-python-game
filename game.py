# Game rules
# Two players: player and enemy
# 
# Both have 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
import random

# Define player class
class Player:
    name = ""
    hp = 0
    weapon = Weapon()
    damage = 0
    critical_damage = 0
    chance_for_critcal_hit = 0
    chance_to_miss = 0

    def attack(self, opponent):
        opponent.hp -= damages_calculation(self)
    
    def activate_weapon(self):
        weapon.set_player_stats(self)

# Define weapon calss
class Weapon:
    name = ""
    damage = 0
    critical_damage = 0
    chance_for_critcal_hit = 0
    chance_to_miss = 0

    def set_player_stats(self, player):
        player.damage = self.damage
        player.critical_damage = self.critical_damage
        player.chance_for_critcal_hit = self.chance_for_critcal_hit
        player.chance_to_miss = self.chance_to_miss

# Define damage calculation function
def damages_calculation(player):
    if evaluate_chance(player.chance_to_miss):
        print("%s miss!" % (player.name))
        return 0
    elif evaluate_chance(player.chance_for_critcal_hit):
        print("It's a critical hit!")
        return player.critical_damage
    else:
        print("%s's attack succeeded!" %(player.name))
        return player.damage

# Define miss function
def evaluate_chance(chance):
    if random.random() < chance:
        return True
    else:
        return False
