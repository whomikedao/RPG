import random

class Character(object):
    def __init__(self, playChar, health, power, hp):
        self.playChar = playChar
        self.health = health
        self.power = power 

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False 

    def attack(self, enemy):
        while goblin.alive() and hero.alive():
            print("You have {} health and {} power.".format(hero_health, hero_power))
            print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks goblin
                knight.attack()
                # goblin_health -= hero_power
                # print("You do {} damage to the goblin.".format(hero_power))
                # if goblin_health <= 0:
                #     print("The goblin is dead.")
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if goblin_health > 0:
                # Goblin attacks hero
                goblin.attack()
                # hero_health -= goblin_power
                # print("The goblin does {} damage to you.".format(goblin_power))
                # if hero_health <= 0:
                #     print("You are dead.")


#Characters #Characters #Characters #Characters

class Knight(Character):
    def __init__(self, bounty):
        super().__init__(playChar, health, power)
        self.playChar = 'Knight'
        self.health = 10
        self.power = 6
        self.bounty = 0

    def attack(enemy):
        self.goblin_health -= self.hero_power
            print("You do {} damage to the goblin.".format(self.hero_power))
            if self.goblin_health <= 0:
                print("The goblin is dead.")
    
    def crit(self):
        chance = random.randint(1, 11)
        if chance == 1 or chance == 2:
            self.power == self.power * 2
            print(f"You've dealt {self.power} critical damage!")

    def print_status(self):
        print(f"Health: {self.hero_health}")


class Medic(Character):
    def __init__(self):
        super().__init__(playChar, health, power)

    def regen(self):
        if chance == 1 or chance == 2:
            self.health += 2
            print(f"You've successfully healed 2 health points!")


class Goblin(Character):
    def __init__(self):
        super().__init__(playChar, health, power)
        self.playChar = 'Goblin'
        self.health = 6
        self.power = 2

    def attack(hero):
        self.hero_health -= self.goblin_power
            print("The goblin does {} damage to you.".format(self.goblin_power))
            if hero_health <= 0:
                print("You are dead.")

    def print_status(self):
        print(f"Health: {self.goblin_health}")

    def coindrop(self, hero):
        if self.health <= 0:
            print(f"You've killed {self.playChar} and dropped 5 coins.")
            hero.bounty += 5
    

class Zombie(Character):
    def __init(self):
        super().__init__(playChar, health, power)
        self.playChar = 'Zombie'
        self.health = 1
        self.power = 2
    
    def attack(self, hero):
        pass

    def alive(self):
        if self.health == 1:
            return True 
    
    def coindrop(self, hero):
        if self.health <= 0:
            print(f"You've killed {self.playChar} and dropped 5 coins.")
            hero.bounty += 5


class Shadow(Character):
    def __init__(self):
        super().__init__(playChar, health, power)
        self.health = 1

    def evasionS(self, Knight):
        chance = random.randint(1, 11)
        if chance == 1:
            print("Your attack was ineffective.")

    def coindrop(self, hero):
        if self.health <= 0:
            print(f"You've killed {self.playChar} and dropped 5 coins.")
            hero.bounty += 6

class DimsumGirl(Character):
    def __init__(self):
        super().__init__(playChar, health, power)

class AsianDriver(Character):
    def __init__(self):
        super().__init__(playChar, health, power)

    def attack(self, hero):
        chance = random.randint(1, 11)
        if chance == 1 or chance == 2:
            self.power = self.power * 3
            hero.health() -= self.power
            print("Asian driver did {} damage to you after changing lanes.".format(self.power))

    def coindrop(self, hero):
        if self.health <= 0:
            print(f"You've killed {self.playChar} and dropped 5 coins.")
            hero.bounty += 5
        
