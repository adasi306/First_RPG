from bp import bpchar
import random

class hero(bpchar):
    def take_action(self):
        self.blocking = False
        print(self.action_names)
        action = input("pick an action\n")
        return action
    
class hero(bpchar):
    def take_action(self):
        self.blocking = False
        print(self.action_names)
        action = input("pick an action\n")
        return action

    def choose_target(self, target_team):
        print("Choose your target:")
        for i, target in enumerate(target_team):
            if target.health > 0:
                print(f"{i + 1}. {target.name} (HP: {target.health}/{target.maxhealth})")

        while True:
            try:
                choice = int(input("Enter the number of the target: ")) - 1
                if choice < 0 or choice >= len(target_team) or target_team[choice].health <= 0:
                    print("Invalid choice. Choose again.")
                else:
                    return target_team[choice]
            except ValueError:
                print("Please enter a valid number.")

    def death(self):
        if self.health <= 0:
            self.health = random.randint(0, 1)
            if self.health == 1:
                print("you lived fatal blow")
            elif self.health == 0:
                print("you died")


class knight(hero):
    action_names = ["attack", "heal", "block"]

    def __init__(self, name, damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects)
        self.blocking = False

    def action1(self):
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            crit_damage = self.crit(base_damage)
            stress_damage = random.randint(15, 20)
            return crit_damage, stress_damage
        else:
            return base_damage, 0

    def action2(self):
        heal_amount = random.choice(range(*self.damage))
        self.heal(heal_amount)
        if random.randint(1, 100) <= self.crit_chance:
            heal_amount = self.crit(heal_amount)
            stress_damage = random.randint(15, 20)
            return heal_amount, stress_damage
        else:
            return heal_amount, 0

    def action3(self):
        print(f"{self.name} is blocking")
        self.blocking = True

class rouge(hero):
    action_names = ["attack", "throw harder", "block"]

    def __init__(self, name, damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects)
        self.blocking = False

    def action1(self):
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            damage = self.crit(base_damage)
            stress_damage = random.randint(15, 20)
            return damage, stress_damage
        else:
            return base_damage, 0

    def action2(self):
        base_damage = random.choice(range(*self.damage))
        poison_charges = 2
        if random.randint(1, 100) <= self.crit_chance:
            crit_damage = self.crit(base_damage)
            stress_damage = random.randint(15, 20)
            return round(crit_damage * 0.5), stress_damage, poison_charges
        else:
            return round(base_damage * 0.5), 0, poison_charges

    def action3(self):
        print(f"{self.name} is blocking")
        self.blocking = True
