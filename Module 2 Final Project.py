# Defeat the Evil Wizard !

import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        # Randomize attack damage within a range (80% to 120% of attack power)
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self):
        print(f"{self.name} uses a powerful strike!")
        return self.attack_power * 2

    def second_ability(self):
        print(f"{self.name} uses a shield bumrush, stunning the opponent!")
        return self.attack_power * 1.5  # Moderate damage with a stun effect

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self):
        print(f"{self.name} casts a fireball!")
        return self.attack_power * 3

    def second_ability(self):
        print(f"{self.name} casts a icy supernova, freezing the opponent!")
        return self.attack_power * 2  # Moderate damage with a freeze effect

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)

    def special_ability(self):
        print(f"{self.name} shoots a barrage of arrows!")
        return self.attack_power * 2

    def second_ability(self):
        print(f"{self.name} uses a poison arrow, dealing damage over time!")
        return self.attack_power * 1.5  # Moderate damage with a poison effect

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

    def special_ability(self):
        print(f"{self.name} uses divine healing!")
        self.heal(20)
        return 0

    def second_ability(self):
        print(f"{self.name} uses an esoteric shield, reducing incoming damage!")
        self.health += 10  # Small heal
        return 0  # No direct damage, but provides defense

# Knight class (inherits from Character)
class Knight(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=90)

    def special_ability(self):
        print(f"{self.name} uses a vibranium sword slash!")
        return self.attack_power * 2  

    def second_ability(self):
        print(f"{self.name} uses a jousting attack, knocking the opponent back!")
        return self.attack_power * 1.5  # Moderate damage with a knockback effect

# Enchantress class (inherits from Character)
class Enchantress(Character):
    def __init__(self, name):
        super().__init__(name, health=175, attack_power=75)

    def special_ability(self):
        print(f"{self.name} projects an illusion spell!")
        return self.attack_power * 3  

    def second_ability(self):
        print(f"{self.name} uses a pheromone spell, seducing the opponent!")
        return self.attack_power * 2  # Moderate damage with a confusion effect

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=40)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin") 
    print("5. Knight") 
    print("6. Enchantress")

    while True:
        class_choice = input("Enter the number of your class choice:")
        if class_choice in ['1', '2', '3', '4', '5', '6']:
            break
        print("Invalid choice. Please enter a number between 1 and 6.")

    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return Knight(name)
    elif class_choice == '6':
        return Enchantress(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Use Second Ability")
        print("4. Heal")
        print("5. View Stats")

        while True:
            choice = input("Choose an action: ")
            if choice in ['1', '2', '3', '4', '5']:
                break
            print("Invalid choice. Please enter a number between 1 and 5.")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            damage = player.special_ability()
            if damage > 0:
                wizard.health -= damage
                if wizard.health <= 0:
                    print(f"{wizard.name} has been defeated!")
                    break
        elif choice == '3':
            damage = player.second_ability()
            if damage > 0:
                wizard.health -= damage
                if wizard.health <= 0:
                    print(f"{wizard.name} has been defeated!")
                    break
        elif choice == '4':
            player.heal(20)
        elif choice == '5':
            player.display_stats()

        # Evil Wizard's Turn
        if wizard.health > 0:
            print("\n--- Evil Wizard's Turn ---")
            wizard.regenerate()
            wizard.attack(player)

        # Check if the player is defeated
        if player.health <= 0:
            print(f"\n{player.name} has been defeated by {wizard.name}!")
            print("You have been defeated by the Evil Wizard!. Better luck next time!")
            break

    # Victory Message
    if wizard.health <= 0:
        print(f"\nThe wizard {wizard.name} has been defeated by {player.name}!")
        print("Congratulations! You have emerged victorious against the Evil Wizrd!")

def main():
    player = create_character()
    wizard = EvilWizard("The Evil Wizard")
    print(f"\nA wild {wizard.name} appears!")
    battle(player, wizard)

if __name__ == "__main__":
    main()   