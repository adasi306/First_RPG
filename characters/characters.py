from bp import bpchar
import random

class knight(bpchar):
    def __init__(self, name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects)

    def attack1(self): #1 przeciwnik
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(base_damage)
        else:
            return base_damage
        
    def attack2(self): #2 przecirwników 50% dmg
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(round(base_damage * 0.6))
        else:
            return round(base_damage * 0.6)

    def attack3(self): #stun 50% dmg, stun do zaimplementowania
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(round(base_damage * 0.4))
        else:
            return round(base_damage * 0.4)
    
    #akcja 4 block

    #akcja 5 ruch o 1 miejsce

class rouge(bpchar):
    def __init__(self, name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects)

    def attack1(self): #1 przeciwnik
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(base_damage)
        else:
            return base_damage
        
    def attack2(self): #2 przeciwników 50% dmg
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return round(self.crit(base_damage * 0.5)) + 1
        else:
            return round(base_damage * 0.5) + 1
        
    def attack3(self): #1 przeciwnik 80%dmg bleed na 2 tury (do zaimplementowania)
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return round(self.crit(base_damage * 0.8)) + 1
        else:
            return round(base_damage * 0.8) + 1
    
    #akcja 4 block

    #akcja 5 ruch o 1 miejsce
        
rouge_stats = rouge("char2", (5, 10), 25, 25, 2, 6, 25, 8, 0, [])
print(rouge_stats)

damage = rouge_stats.attack1()
print(damage)
damage = rouge_stats.attack2()
print(damage)

class healer(bpchar):
    def __init__(self, name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects)

    def heal1(self): #1 postać
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(base_damage)
        else:
            return base_damage

    def heal2(self): #cały team heal
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return round(self.crit(base_damage * 0.25)) + 1
        else:
            return round(base_damage * 0.25) + 1
    
    #akcja 4 block

    #akcja 5 ruch o 1 miejsce
        
healer_stats = healer("char3", (3, 6), 20, 20, 1, 4, 10, 4, 0, [])
print(healer_stats)

damage = healer_stats.heal1()
print(damage)

class pd(bpchar):
    def __init__(self, name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects):
        super().__init__(name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects)

    def attack1(self):
        base_damage = random.choice(range(*self.damage))
        if random.randint(1, 100) <= self.crit_chance:
            return self.crit(base_damage)
        else:
            return base_damage

    
    #akcja 4 block

    #akcja 5 ruch o 1 miejsce
        
pd_stats = pd("char4", (3, 6), 20, 20, 5, 4, 0, 5, 0, [])
print(pd_stats)

damage = pd_stats.attack1()
print(damage)