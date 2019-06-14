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
        print("%s's attack succeeded!" %(player.name))
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

# Create game
class Game:
    player1 = Player()
    enemy1 = Player()
    enemy2 = Player()
    enemy3 = Player()
    enemy4 = Player()
    enemy5 = Player()

    bow = Weapon()
    gun = Weapon()
    bazooka = Weapon()

    def start(self):
        pass

    def choose_weapon(self):
        pass

    def fighting_part(self):
        player = self.player1
        enemy_list = [self.enemy1,
                      self.enemy2,
                      self.enemy3,
                      self.enemy4,
                      self.enemy5]

        for enemy in enemy_list:
            player_start = True
            while enemy.hp > 0 or player.hp > 0:
                if player_start:
                    player.attack(enemy)
                else:
                    enemy.attack(player)
            
            if player.hp <= 0:
                self.end(False)
            else:
                print("You defeated %s." %(enemy.name))
            
            if input("Do you want to change weapon?(yes/no) ").strip.upper == "YES":
                self.choose_weapon()
            


    def end(self, player_win):
        if player_win:
            print("Congratulation!")
            print("You defeated all the enemies!")
            print("Here is your reward:")
            print("|————————|")
            print("|        |")
            print("|________|")
            print("\\________/")
            print(" \\______/")
            print("  |    |")
            print(" _|____|_")
        else:
            print("You lose....")
            print()
            print("   \\__/   \\__/")
            print("            /\\")
            print("           |__|")
            print("  _____________")
            print(" /             \\")
            print()
        
        print("Try again!")
        quit()


# beginning game

game = Game()

game.start()

