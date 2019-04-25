def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

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
            goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(hero_power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

main()


class Character(object):
    def __init__(self):
        hero_health = 10
        hero_power = 5
        goblin_health = 6
        goblin_power = 2

    def alive(self):
        if health > 0:
            return True

class Hero(Character):
    def __init__(self):
        self.hero_health = 10
        self.hero_power = 5

    def attack(enemy):
        self.goblin_health -= self.hero_power
            print("You do {} damage to the goblin.".format(self.hero_power))
            if self.goblin_health <= 0:
                print("The goblin is dead.")
    
    def alive(self):
        if self.hero_health > 0:
            return True

    def print_status(self):
        print(f"Health: {self.hero_health}")

class Goblin(Character):
    def __init__(self):
        self.goblin_health = 6
        self.goblin_power = 2

    def attack(hero):
        self.hero_health -= self.goblin_power
            print("The goblin does {} damage to you.".format(self.goblin_power))
            if hero_health <= 0:
                print("You are dead.")

    def alive(self):
        if self.goblin_health > 0:
            return True

    def print_status(self):
        print(f"Health: {self.goblin_health}")
