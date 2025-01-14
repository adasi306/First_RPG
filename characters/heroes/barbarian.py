from characters import hero
import random


class barbarian(hero):
    action_names = ["attack", "heal", "block"]

    def passive():
        pass

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.actions = [self.action1, self.action2, self.action3]
        self.blocking = False
        self.dead = False

    def action1(self, ally_team, enemy_team):
        base_damage = round(
            random.choice(range(*self.base_damage)) * self.damage_modifier
        )
        stress_change = 0
        if random.randint(1, 100) <= self.stats.crit_chance:
            base_damage = round(self.crit(base_damage))
            stress_change = random.randint(15, 20)
        target = self.choose_target([t for t in enemy_team if t.stats.health > 0])
        if target.roll_dodge():
            print(f"\n{target.name} dodged the attack.")
        elif self.if_attack_hit():
            print(f"\n{self.name} missed the attack.")
        else:
            true_damage = round(self.dmg_armor(base_damage, target.stats.armor))
            target.dmg_taken(true_damage)
            print(f"\n{self.name} attacks {target.name} for {true_damage} HP.")
            if stress_change > 0:
                self.stress_heal(stress_change)
                print(f"\n{self.name} is healed for {stress_change} stress.")

    def action2(self, ally_team, enemy_team):
        base_damage = round((random.choice(range(*self.base_damage)) * self.damage_modifier) * 0.6)
        stress_change = 0
        if random.randint(1, 100) <= self.stats.crit_chance:
            base_damage = round(self.crit(base_damage))
            stress_change = random.randint(15, 20)
        target = self.choose_target([t for t in enemy_team if t.stats.health > 0])
        if target.roll_dodge():
            print(f"\n{target.name} dodged the attack.")
        elif self.if_attack_hit():
            print(f"\n{self.name} missed the attack.")
        else:
            true_damage = round(self.dmg_armor(base_damage, target.stats.armor))
            target.dmg_taken(true_damage)
            print(f"\n{self.name} attacks {target.name} for {true_damage} HP.")
            if stress_change > 0:
                self.stress_heal(stress_change)
                print(f"\n{self.name} is healed for {stress_change} stress.")

    def action3(self, ally_team, enemy_team):
        base_damage = round((random.choice(range(*self.base_damage)) * self.damage_modifier) * 0.9)
        stress_change = 0
        stun_chance = 100
        if random.randint(1, 100) <= self.stats.crit_chance:
            base_damage = round(self.crit(base_damage))
            stress_change = random.randint(15, 20)
        target = self.choose_target([t for t in enemy_team if t.stats.health > 0])
        if target.roll_dodge():
            print(f"\n{target.name} dodged the attack.")
        elif self.if_attack_hit():
            print(f"\n{self.name} missed the attack.")
        else:
            true_damage = round(self.dmg_armor(base_damage, target.stats.armor))
            target.dmg_taken(true_damage)
            print(f"\n{self.name} attacks {target.name} for {true_damage} HP.")
            if not any(
                effect["type"] == "stun" for effect in target.stats.status_effects
            ):
                if random.randint(1, 100) <= stun_chance:
                    target.stats.status_effects.append({"type": "stun", "charges": 1})
                    print(f"\n{target.name} is stunned and will skip their next turn.")
            if stress_change > 0:
                self.stress_heal(stress_change)
                print(f"\n{self.name} is healed for {stress_change} stress.")

    def action4(self, ally_team, enemy_team):
        pass

    def action5(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True