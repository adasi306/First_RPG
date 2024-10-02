from blueprint import BlueprintCharacter, CharacterStats
import random


class enemy(BlueprintCharacter):
    def death(self):
        self.dead = True
        self.stats.health = 0
        print(f"\n{self.name} died!")

    def choose_target(self, target_team):
        taunt_effect = next((effect for effect in self.stats.status_effects if effect["type"] == "taunt"), None)
        if taunt_effect:
            print(f"\n{self.name} is taunted and must attack {taunt_effect['taunter'].name}!")
            return taunt_effect["taunter"]
        else:
            return random.choice([t for t in target_team if not t.dead])


class skeleton(enemy):
    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.dead = False

    def attack(self, target_team):
        target = self.choose_target(target_team)
        base_damage = random.choice(range(*self.stats.damage))

        if random.randint(1, 100) <= self.stats.crit_chance:
            damage = self.crit(base_damage)
            stress_change = random.randint(15, 20)
        else:
            damage = base_damage
            stress_change = 0

        if target.roll_dodge():
            print(f"\n{target.name} dodged the attack.")
        else:
            if target.blocking:
                target.stats.stress += stress_change
                true_damage, blocked_damage = target.block(damage)
                print(f"\n{self.name} attacks {target.name} for {true_damage} HP. Blocked damage: {blocked_damage}.")
            else:
                target.stats.stress += stress_change
                target.dmg_taken(damage)
                print(f"\n{self.name} attacks {target.name} for {target.dmg_armor(damage, target.stats.armor)} HP.")

            if stress_change > 0:
                print(f"\n{target.name} gains {stress_change} stress.")

        return damage, stress_change