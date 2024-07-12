from bp import bpchar
import random


class enemy(bpchar):
    def death(self):
        if self.health <= 0:
            print("you've killed an enemy")


class skeleton(enemy):
    def __init__(self, name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects)

    def attack(self):
        base_damage = random.choice(range(*self.damage))
        damage, is_crit = self.crit(base_damage)
        stress_damage = random.randint(15,20) if is_crit else 0  # Dodaj 20 stresu przy krytycznych uderzeniach
        return damage, stress_damage
