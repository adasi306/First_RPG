from bp import bpchar
import random


class enemy(bpchar):
    def death(self):
        if self.health <= 0:
            print("you've killed an enemy")


class skeleton(enemy):
    def __init__(self, name, damage, health, maxhealth, armor, dodge, accuracy , crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge, accuracy , crit_chance, speed, stress, status_effects)

    def attack(self):
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            damage = self.crit(base_damage)
            stress_damage = random.randint(15, 20)
            return damage, stress_damage
        else:
            return base_damage