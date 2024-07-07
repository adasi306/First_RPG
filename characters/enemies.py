from bp import bpchar
import random

class skeleton(bpchar):
    def __init__(self, name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects)

    def attack(self):
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(base_damage)
        else:
            return base_damage
