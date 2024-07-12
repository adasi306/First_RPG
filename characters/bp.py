import random

# kryt zdejmuje stes jak w darkest dungeon
class bpchar:
    def __init__(self, name, damage, health, maxhealth, armor, dodge, crit_chance, speed, stress, status_effects):
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
            return damage * 2, True
        else:
            return damage, False

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
        return 2
    
    def poison(self):
        return 5
    
    def stun(self):
        pass

    def __str__(self):
        return (f"Name: {self.name} \t Damage {self.damage} \t Health {self.health}/{self.maxhealth} \t Armor {self.armor} \t "
                f"Dodge {self.dodge} \t Crit chance {self.crit_chance}% \t Speed {self.speed} \t "
                f"Stress {self.stress}/100 \t Status effects {self.status_effects}")
    


#pomysły na postacie
#1)rycerz klasyczny tank z basic skillkami
#2)barbażyńca im mniej hp więcej dmg?
#3)rouge nakłada krawienie lub bije dużo bazowo
#4)rogal z bronią palną co strzela w wiele oponentów lub dowolnego
#5)rogal co rzuca nożami zatrutymi
#6)jakiś ziomek co losowe rzeczy robi, np atak ma 1/3, na krawienie, truciznę lub stuna, healka o losowej sile, losowego buffa lub dmg o losowej wartości
#7)kleryk klasyczny healer buffy
#8)plaugedoctor truciźny aoe i leczy chujowo
#9)klasa co zdejmuje głównie stres