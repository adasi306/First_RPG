from blueprint import BlueprintCharacter, CharacterStats
import random


class hero(BlueprintCharacter):
    actions = []

    def take_action(self):
        self.blocking = False
        print("\nChoose an action:")
        for idx, action_name in enumerate(self.action_names, start=1):
            print(f"{idx}. {action_name}")

        while True:
            try:
                action = int(input("\nPick an action (1, 2, 3, 4, 5): "))
                if action in [1, 2, 3, 4, 5]:
                    return str(action)
                else:
                    print("\nInvalid choice. Please pick a valid action.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

    def choose_target(self, target_team):
        print("\nChoose your target:")
        available_targets = [t for t in target_team if t.stats.health > 0]
        for i, target in enumerate(available_targets, 1):
            print(f"{i}. {target.name} (HP: {target.stats.health}/{target.stats.maxhealth})")

        while True:
            try:
                choice = int(input("\nEnter the number of the target: ")) - 1
                if choice < 0 or choice >= len(target_team) or target_team[choice].stats.health <= 0:
                    print("\nInvalid choice. Choose again.")
                else:
                    return target_team[choice]
            except ValueError:
                print("\nPlease enter a valid number.")

    def death(self):
        self.death_chance = random.randint(1, 100)
        if self.death_chance >= 90:
            self.stats.stress += 5
            print("\nYou survived a fatal blow")
        else:
            self.dead = True
            print("\nYou died")

class knight(hero):
    action_names = ["attack", "heal", "block", "block2", "block3"]

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.actions = [self.action1, self.action2, self.action3]
        self.blocking = False
        self.dead = False

    def action1(self, ally_team, enemy_team):
        base_damage = round(random.choice(range(*self.base_damage)) * self.damage_modifier)
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
            if not any(effect["type"] == "stun" for effect in target.stats.status_effects):
                if random.randint(1, 100) <= stun_chance:
                    target.stats.status_effects.append({"type": "stun", "charges": 1})
                    print(f"\n{target.name} is stunned and will skip their next turn.")
            if stress_change > 0:
                self.stress_heal(stress_change)
                print(f"\n{self.name} is healed for {stress_change} stress.")

    def action2(self, ally_team, enemy_team):
        heal_amount = round(random.choice(range(*self.base_damage)) * self.healing_modifier)
        stress_change = 0
        if random.randint(1, 100) <= self.stats.crit_chance:
            heal_amount = round(self.crit(heal_amount))
            stress_change = random.randint(15, 20)
        target = self.choose_target([t for t in ally_team if t.stats.health > 0])
        target.heal(heal_amount)
        print(f"\n{self.name} heals {target.name} for {heal_amount} HP.")
        if stress_change > 0:
            self.stress_heal(stress_change)
            print(f"\n{self.name} heals {stress_change} stress.")

    def action3(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True

    def action4(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True

    def action5(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True


class rouge(hero):
    action_names = ["throw dagger", "throw toxic dagger", "block", "block2", "block3"]

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.blocking = False
        self.dead = False

    def action1(self, ally_team, enemy_team):
        base_damage = round(random.choice(range(*self.base_damage)) * self.damage_modifier)
        stress_change = 0
        mark_charges = 2
        mark_chance = 70
        taunt_chance = 100
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
            if random.randint(1, 100) <= mark_chance:
                target.apply_status_effect("mark", mark_charges)
            if random.randint(1, 100) <= taunt_chance:
                if not any(effect["type"] == "taunt" for effect in target.stats.status_effects):
                    target.stats.status_effects.append({"type": "taunt", "taunter": self})
                    print(f"\n{target.name} is taunted by {self.name} and must attack them for the next turn!")
            if stress_change > 0:
                self.stress_heal(stress_change)
                print(f"\n{self.name} heals for {stress_change} stress.")

    def action2(self, ally_team, enemy_team):
        base_damage = round(random.choice(range(*self.base_damage)) * self.damage_modifier)
        stress_change = 0
        poison_charges = 2
        bleed_charges = 4
        if random.randint(1, 100) <= self.stats.crit_chance:
            base_damage = round(self.crit(base_damage))
            stress_change = random.randint(15, 20)
        target = self.choose_target([t for t in enemy_team if t.stats.health > 0])
        if target.roll_dodge():
            print(f"\n{target.name} dodged the attack.")
        elif self.if_attack_hit():
            print(f"\n{self.name} missed the attack.")
        else:
            target.dmg_taken(base_damage)
            target.apply_status_effect("poison", poison_charges)
            target.apply_status_effect("bleed", bleed_charges)
            print(f"\n{self.name} attacks {target.name} for {round(target.dmg_armor(base_damage, target.stats.armor))} HP.")
            if stress_change > 0:
                self.stress_heal(stress_change)
                print(f"\n{self.name} heals {stress_change} stress.")

    def action3(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True

    def action4(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True

    def action5(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True

class musketeer(hero):
    action_names = ["attack", "heal", "block"]

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.actions = [self.action1, self.action2, self.action3]
        self.blocking = False
        self.dead = False

    def action1(self, ally_team, enemy_team):
        base_damage = round(random.choice(range(*self.base_damage)) * self.damage_modifier)
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
        pass

    def action3(self, ally_team, enemy_team):
        base_damage = round(random.choice(range(*self.base_damage)) * self.damage_modifier * 0.2)
        stress_change = 0
        mark_charges = 2
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
            target.apply_status_effect("mark", mark_charges)
            if stress_change > 0:
                self.stress_heal(stress_change)
                print(f"\n{self.name} is healed for {stress_change} stress.")

    def action4(self, ally_team, enemy_team):
        pass

    def action5(self, ally_team, enemy_team):
        print(f"\n{self.name} is blocking")
        self.blocking = True

class cleric(hero):
    action_names = ["attack", "heal", "block"]

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.actions = [self.action1, self.action2, self.action3]
        self.blocking = False
        self.dead = False

    def action1(self, ally_team, enemy_team):
        heal_amount = round(random.choice(range(*self.base_damage)) * self.healing_modifier)
        stress_change = 0
        if random.randint(1, 100) <= 50:
            heal_amount = round(self.crit(heal_amount))
            stress_change = random.randint(15, 20)
        target = self.choose_target([t for t in ally_team if t.stats.health > 0])
        if target.stats.health < target.stats.maxhealth * 0.5:
            target.heal(round(heal_amount * 1.25))
            print(f"\n{self.name} heals {target.name} for {round(heal_amount * 1.25)}) HP.")
        if target.stats.health >= target.stats.maxhealth * 0.5:
            target.heal(heal_amount)
            print(f"\n{self.name} heals {target.name} for {heal_amount} HP.")
        if stress_change > 0:
            self.stress_heal(stress_change)
            print(f"\n{self.name} heals {stress_change} stress.")
    
    def action2(self, ally_team, enemy_team):
        heal_amount = round(random.choice(range(*self.base_damage)) * self.healing_modifier * 0.4)
        stress_change = 0
        if random.randint(1, 100) <= 40:
            heal_amount = round(self.crit(heal_amount))
            stress_change = random.randint(15, 20)
        for target in ally_team:
            if target.stats.health > 0 and target.stats.health < target.stats.maxhealth * 0.5:
                target.heal(round(heal_amount * 1.25))
                print(f"\n{self.name} heals {target.name} for {round(heal_amount * 1.25)}) HP.")
            elif target.stats.health > 0 and target.stats.health >= target.stats.maxhealth * 0.5:
                target.heal(heal_amount)
                print(f"\n{self.name} heals {target.name} for {heal_amount} HP.")
        if stress_change > 0:
            for target in ally_team:
                if target.stats.health > 0:
                    self.stress_heal(stress_change)
                    print(f"\n{self.name} heals {target.name} for {stress_change} stress.")


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