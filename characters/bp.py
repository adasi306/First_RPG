import random

class bpchar:
    def __init__(self, name, damage, health, maxhealth, armor, dodge, accuracy, crit_chance, speed, stress, status_effects):
        self.name = name
        self.damage = damage
        self.health = health
        self.maxhealth = maxhealth
        self.armor = armor
        self.dodge = dodge
        self.crit_chance = crit_chance
        self.speed = speed
        self.stress = stress
        self.status_effects = status_effects
        self.accuracy = accuracy
        #resist

    def attack(self):
        raise NotImplementedError("trzeba dla każdej postaci osobno napisać")

    def death(self):
        raise NotImplementedError("trzeba dla każdej frakcji napisać")
    
    def heal(self, amount):
        self.health += amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth
    
    def block(self, damage):
        true_damage = max(damage - self.armor, 0)
        blocked_damage = true_damage - round(true_damage * 0.5)
        self.health -= round(true_damage * 0.5)
        self.stress_()
        self.death()
        return true_damage, blocked_damage
    
    def dmg_armor(damage, armor):
        if damage - armor < 0:
            return 0
        else:
            return damage - armor

    def dmg_taken(self, damage):
        true_damage = max(damage - self.armor, 0)
        self.health -= true_damage
        self.stress_()
        self.death()

    def crit(self, damage):
        if random.randint(1, 100) <= self.crit_chance:
            return damage * 2
        else:
            return damage
        
    def if_attack_hit(self):
        self.hit = random.randint(1, 100) > self.accuracy
        return self.hit
        
    def dodge_chance(self):
        self.dodge_xd = random.randint(1, 100) <= self.dodge * 5
        return self.dodge_xd

    def stress_(self):    #zmienia hp na 1 (zawał)
        if self.stress >= 100:
            self.health = 1
            self.stress = 75

    def stress_heal(self, amount):
        self.stress = max(self.stress - amount, 0)

    def dmg_buff(self, damage):
        return damage * 1.5

    def dmg_reduction_buff(self, damage):
        return damage * 0.5
    
    def bleed(self):
        raise NotImplementedError("trzeba dla każdej postaci osobno napisać")
    
    def apply_poison(self, charges):
        poison_effect = next((effect for effect in self.status_effects if effect['type'] == 'poison'), None)
        if poison_effect:
            poison_effect['charges'] += charges
        else:
            self.status_effects.append({'type': 'poison', 'charges': charges})
        print(f"{self.name} has been poisoned! Poison charges: {charges}")

    def process_status_effects(self):
        for effect in self.status_effects:
            if effect['type'] == 'poison':
                poison_damage = effect['charges']
                self.health -= poison_damage
                effect['charges'] -= 1
                print(f"{self.name} takes {poison_damage} poison damage.")
                if effect['charges'] <= 0:
                    self.status_effects.remove(effect)
                if self.health <= 0:
                    self.death()
    
    def stun(self):
        raise NotImplementedError("trzeba dla każdej postaci osobno napisać")
    
    def get_status_effects_str(self):
        return ", ".join([f"{effect['type']} {effect['charges']}" for effect in self.status_effects])

    def __str__(self):
        return (f"Name: {self.name} \t Damage {self.damage} \t Health {self.health}/{self.maxhealth} \t Armor {self.armor} \t "
                f"Dodge {self.dodge} \t Accuracy {self.accuracy} \t Crit chance {self.crit_chance}% \t Speed {self.speed} \t "
                f"Stress {self.stress}/100 \t Status effects {self.status_effects}")