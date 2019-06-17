import random

# Define player class
class Player:
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.activate_weapon()

    damage = 0
    critical_damage = 0
    chance_for_critcal_hit = 0
    chance_to_miss = 0

    def attack(self, game, opponent):
        if self.name == "You":
            message1 = "use"
            message2 = "have"
        else:
            message1 = "uses"
            message2 = "has"

        print("%s %s %s." %(self.name, message1, self.weapon.name))
        damages = game.damages_calculation(self)
        opponent.hp -= damages
        print("%s lost %d HP and %s %d HP left." %(opponent.name, damages, message2, opponent.hp))
    
    def activate_weapon(self):
        weapon.set_player_stats(self)

# Define weapon calss
class Weapon:
    def __init__(self, name, damage, critical_damage, chance_for_critcal_hit, chance_to_miss):
        self.name = name
        self.damage = damage
        self.critical_damage = critical_damage
        self.chance_for_critcal_hit = chance_for_critcal_hit
        self.chance_to_miss = chance_to_miss

    def set_player_stats(self, player):
        player.damage = self.damage
        player.critical_damage = self.critical_damage
        player.chance_for_critcal_hit = self.chance_for_critcal_hit
        player.chance_to_miss = self.chance_to_miss


# Create game class
class Game:
    def __init__(self, bow, gun, bazooka, spoon, shoe, stapplers,
                 liquid_n2, acid_gun, player1, enemy1, enemy2,
                 enemy3, enemy4, enemy5):
        self.bow = bow
        self.gun = gun
        self.bazooka = bazooka
        self.spoon = spoon
        self.shoe = shoe
        self.stapplers = stapplers
        self.liquid_n2 = liquid_n2
        self.acid_gun = acid_gun

        self.player1 = player1
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.enemy3 = enemy3
        self.enemy4 = enemy4
        self.enemy5 = enemy5

        self.start()

    def start(self):
        print("'The Fight of Your Life'")
        print("Ready to play the game?")

        while True:
            play = input("yes/no: ").strip().upper()
            if play == "NO":
                print("You're weak!!!")
                quit()
            elif play == "YES":
                break
            else:
                continue

        print("Great! Fight your opponents until there are no more left!")

        self.fighting_part()

    def choose_weapon(self, player):
        while True:
            print("Choose your weapon!")
            print("Bow: stats")
            print("Gun: stats")
            print("Bazooka: stats")
            print("Or surrender, if you're a chicken!")
            choice = input(": ").strip().upper()

            if choice == "BOW":
                player.weapon = self.bow
                break
            elif choice == "GUN":
                player.weapon = self.gun
                break
            elif choice == "BAZOOKA":
                player.weapon = self.bazooka
                break
            elif choice == "SURRENDER":
                print("Chicken!")
                self.end(False)
            else:
                print("You don't have this weapon!")
                continue

    def fighting_part(self):
        player = self.player1
        enemy_list = [self.enemy1,
                      self.enemy2,
                      self.enemy3,
                      self.enemy4,
                      self.enemy5]
        rounds = 0

        for enemy in enemy_list:
            rounds += 1
            print("Round %d" %(rounds))
            print("Your opponent is %s." %(enemy.name))
            print("FIGHT!")
            player_start = True
            while enemy.hp > 0 or player.hp > 0:
                if player_start:
                    self.choose_weapon(player)
                    player.attack(self, enemy)
                    player_start = False
                else:
                    enemy.attack(self, player)
                    player_start = True
            
            if player.hp <= 0:
                print("%s defeated you." %(enemy.name))
                self.end(False)
            else:
                print("You defeated %s." %(enemy.name))
        
        self.end(True)
            
            
    def damages_calculation(self, player):
        if random.random() < player.chance_to_miss:
            print("%s missed!" % (player.name))
            return 0
        elif random.random() < player.chance_for_critcal_hit:
            print("%s's attack succeeded!" %(player.name))
            print("It's a critical hit!")
            return player.critical_damage
        else:
            print("%s's attack succeeded!" %(player.name))
            return player.damage

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
# (self, bow, gun, bazooka, spoon, shoe, stapplers,
#  liquid_n2, acid_gun, player1, enemy1, enemy2,
#  enemy3, enemy4, enemy5)


game = Game()
