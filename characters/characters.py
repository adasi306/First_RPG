from blueprint import BlueprintCharacter, CharacterStats
import random

class hero(BlueprintCharacter):
    actions = []
    def action1(self, ally_team, enemy_team):
        raise NotImplementedError("xd")
    
    def action2(self, ally_team, enemy_team):
        raise NotImplementedError("xd")
    
    def action3(self, ally_team, enemy_team):
        raise NotImplementedError("xd")

    def take_action(self):
        self.blocking = False
        print(self.action_names)
        action = input("pick an action\n")
        return action

    def choose_target(self, target_team):
        print("Choose your target:")
        for i, target in enumerate(target_team):
            if target.stats.health > 0:
                print(f"{i + 1}. {target.name} (HP: {target.stats.health}/{target.stats.maxhealth})")

        while True:
            try:
                choice = int(input("Enter the number of the target: ")) - 1
                if choice < 0 or choice >= len(target_team) or target_team[choice].stats.health <= 0:
                    print("Invalid choice. Choose again.")
                else:
                    return target_team[choice]
            except ValueError:
                print("Please enter a valid number.")

    def death(self):
        if self.stats.health <= 0:
            self.stats.health = random.randint(0, 1)
            if self.stats.health == 1:
                print("you lived fatal blow")
            elif self.stats.health == 0:
                print("you died")


class knight(hero):
    action_names = ["attack", "heal", "block"]

    def __init__(self, name, damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects):
        stats = CharacterStats(damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects)
        super().__init__(name, stats)
        self.actions = [self.action1, self.action2, self.action3]
        self.blocking = False

    def action1(self, ally_team, enemy_team): #basic attack
        base_damage = random.choice(range(*self.stats.damage))
        stress_damage = 0
        if random.randint(1, 100) <= self.stats.crit_chance:
            base_damage = self.crit(base_damage)
            stress_damage = random.randint(15, 20)
        target = self.choose_target([t for t in enemy_team if t.stats.health > 0])
        if target.roll_dodge():
            print(f"{target.name} dodged attack.")
        elif self.if_attack_hit():
            print(f"{self.name} missed attack.")
        else:
            target.dmg_taken(base_damage)
            print(f"{self.name} attacks {target.name} for {BlueprintCharacter.dmg_armor(base_damage, target.stats.armor)} HP.")
            if stress_damage > 0:
                self.stress_heal(stress_damage)
                print(f"{self.name} heals {stress_damage} stress.")

    def action2(self, ally_team, enemy_team): #heal
        target = self.choose_target([t for t in ally_team if t.stats.health > 0])
        stress_damage = 0
        heal_amount = random.choice(range(*self.stats.damage))
        if random.randint(1, 100) <= self.stats.crit_chance:
            heal_amount = self.crit(heal_amount)
            stress_damage = random.randint(15, 20)
        target.heal(heal_amount)
        print(f"{self.name} heals {target.name} for {heal_amount} HP.")
        if stress_damage > 0:
            self.stress_heal(stress_damage)
            print(f"{self.name} heals {stress_damage} stress.")

    def action3(self, ally_team, enemy_team): #block
        print(f"{self.name} is blocking")
        self.blocking = True

class rouge(hero):
    action_names = ["throw dagger", "throw toxic dagger", "block"]

    def __init__(self, name, damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects):
        stats = CharacterStats(damage, health, maxhealth, armor, dodge, accucary, crit_chance, speed, stress, status_effects)
        super().__init__(name, stats)
        self.blocking = False

    def action1(self, ally_team, enemy_team): #basic attack
        base_damage = random.choice(range(*self.stats.damage))
        stress_damage = 0
        if random.randint(1, 100) <= self.stats.crit_chance:
            base_damage = self.crit(base_damage)
            stress_damage = random.randint(15, 20)
        target = self.choose_target([t for t in enemy_team if t.stats.health > 0])
        if target.roll_dodge():
            print(f"{target.name} dodged attack.")
        elif self.if_attack_hit():
            print(f"{self.name} missed attack.")
        else:
            target.dmg_taken(base_damage)
            print(f"{self.name} attacks {target.name} for {BlueprintCharacter.dmg_armor(base_damage, target.stats.armor)} HP.")
            if stress_damage > 0:
                self.stress_heal(stress_damage)
                print(f"{self.name} heals {stress_damage} stress.")
        

    def action2(self, ally_team, enemy_team): #attack with poison
        base_damage = random.choice(range(*self.stats.damage))
        stress_damage = 0
        poison_charges = 2
        if random.randint(1, 100) <= self.stats.crit_chance:
            base_damage = self.crit(base_damage)
            stress_damage = random.randint(15, 20)
        target = self.choose_target([t for t in enemy_team if t.stats.health > 0])
        if target.roll_dodge():
            print(f"{target.name} dodged attack.")
        elif self.if_attack_hit():
            print(f"{self.name} missed attack.")
        else:
            target.dmg_taken(base_damage)
            target.apply_poison(poison_charges)
            print(f"{self.name} attacks {target.name} for {BlueprintCharacter.dmg_armor(base_damage, target.stats.armor)} HP and applies {poison_charges} poison charges.")
            if stress_damage > 0:
                self.stress_heal(stress_damage)
                print(f"{self.name} heals {stress_damage} stress.")

    def action3(self, ally_team, enemy_team): #block
        print(f"{self.name} is blocking")
        self.blocking = True
