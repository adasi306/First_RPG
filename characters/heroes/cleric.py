from characters import hero
import random


class cleric(hero):
    action_names = ["attack", "heal", "block"]

    def passive():
        pass

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.actions = [self.action1, self.action2, self.action3]
        self.blocking = False
        self.dead = False

    def action1(self, ally_team, enemy_team):
        heal_amount = round(
            random.choice(range(*self.base_damage)) * self.healing_modifier
        )
        stress_change = 0
        if random.randint(1, 100) <= 50:
            heal_amount = round(self.crit(heal_amount))
            stress_change = random.randint(15, 20)
        target = self.choose_target([t for t in ally_team if t.stats.health > 0])
        if target.stats.health < target.stats.maxhealth * 0.5:
            target.heal(round(heal_amount * 1.25))
            print(
                f"\n{self.name} heals {target.name} for {round(heal_amount * 1.25)}) HP."
            )
        if target.stats.health >= target.stats.maxhealth * 0.5:
            target.heal(heal_amount)
            print(f"\n{self.name} heals {target.name} for {heal_amount} HP.")
        if stress_change > 0:
            self.stress_heal(stress_change)
            print(f"\n{self.name} heals {stress_change} stress.")

    def action2(self, ally_team, enemy_team):
        heal_amount = round(
            random.choice(range(*self.base_damage)) * self.healing_modifier * 0.4
        )
        stress_change = 0
        if random.randint(1, 100) <= 40:
            heal_amount = round(self.crit(heal_amount))
            stress_change = random.randint(15, 20)
        for target in ally_team:
            if (
                target.stats.health > 0
                and target.stats.health < target.stats.maxhealth * 0.5
            ):
                target.heal(round(heal_amount * 1.25))
                print(
                    f"\n{self.name} heals {target.name} for {round(heal_amount * 1.25)}) HP."
                )
            elif (
                target.stats.health > 0
                and target.stats.health >= target.stats.maxhealth * 0.5
            ):
                target.heal(heal_amount)
                print(f"\n{self.name} heals {target.name} for {heal_amount} HP.")
        if stress_change > 0:
            for target in ally_team:
                if target.stats.health > 0:
                    self.stress_heal(stress_change)
                    print(
                        f"\n{self.name} heals {target.name} for {stress_change} stress."
                    )

    def action3(self, ally_team, enemy_team):
        pass

    def action4(self, ally_team, enemy_team):
        target = self.choose_target([t for t in ally_team if t.stats.health > 0])
        if target.stats.status_effects:
            target.stats.status_effects.clear()
            print(f"\n{self.name} removes all status effects from {target.name}.")
        else:
            print(f"\n{target.name} has no status effects to remove.")

    def action5(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True
