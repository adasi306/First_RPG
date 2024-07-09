from bp import bpchar
import random

class hero(bpchar):
    def take_action(self):
        self.blocking = False
        print(self.action_names)
        action = input("pick an action\n")
        return action

    def death(self):
        if self.health <= 0:
            self.health = random.randint(0, 1)
            if self.health == 1:
                print("you lived fatal blow")
            elif self.health == 0:
                print("you died")


class knight(hero):
    action_names=["attack", "heal" , "block"]
    def __init__(self, name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects)
        self.blocking = False

    def action1(self):
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(base_damage)
        else:
            return base_damage
        
    def action2(self):
        heal_amount = random.choice(range(*self.damage))
        self.heal(heal_amount)
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(heal_amount)
        else:
            return heal_amount

    def action3(self):
        self.blocking = True