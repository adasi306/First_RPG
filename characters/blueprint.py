import random

class CharacterStats:
    """
    A class to hold and manage the character's stats.
    """
    
    def __init__(self, damage, health, maxhealth, armor, dodge, accuracy, crit_chance, speed, stress, status_effects):
        """
        Initializes a new CharacterStats instance with given stats and attributes.
        """
        self.damage = damage
        self.health = health
        self.maxhealth = maxhealth
        self.armor = armor
        self.dodge = dodge
        self.accuracy = accuracy
        self.crit_chance = crit_chance
        self.speed = speed
        self.stress = stress
        self.status_effects = status_effects

class BlueprintCharacter:
    """
    A blueprint class for characters in a combat scenario. This class defines the common properties
    and methods that all characters will have. Specific characters should inherit from this class
    and implement unique methods as needed.

    Attributes:
        name (str): The name of the character.
        stats (CharacterStats): An instance of CharacterStats holding all the character's core attributes.
    """
    
    def __init__(self, name, stats):
        """
        Initializes a new BlueprintCharacter instance with a name and stats.

        Args:
            name (str): The name of the character.
            stats (CharacterStats): An instance of CharacterStats holding the character's core stats.
        """
        self.name = name
        self.stats = stats

    def attack(self):
        raise NotImplementedError("need to implement for each character")

    def death(self):
        raise NotImplementedError("need to implement for each fraction")
    
    def heal(self, amount):
        self.stats.health += amount
        if self.stats.health > self.stats.maxhealth:
            self.stats.health = self.stats.maxhealth
    
    def block(self, damage):
        true_damage = max(damage - self.stats.armor, 0)
        blocked_damage = true_damage - round(true_damage * 0.5)
        self.stats.health -= round(true_damage * 0.5)
        self.stress_()
        self.death()
        return true_damage, blocked_damage
    
    def dmg_armor(damage, armor):
        if damage - armor < 0:
            return 0
        else:
            return damage - armor

    def dmg_taken(self, damage):
        true_damage = max(damage - self.stats.armor, 0)
        self.stats.health -= true_damage
        self.stress_()
        self.death()

    def crit(self, damage):
        if random.randint(1, 100) <= self.stats.crit_chance:
            return damage * 2
        else:
            return damage
        
    def if_attack_hit(self):
        self.hit = random.randint(1, 100) > self.stats.accuracy
        return self.hit
        
    def roll_dodge(self):
        self.dodge = random.randint(1, 100) <= self.stats.dodge * 5
        return self.dodge

    def stress_(self):
        if self.stats.stress >= 100:
            self.stats.health = 1
            self.stats.stress = 75

    def stress_heal(self, amount):
        self.stats.stress = max(self.stats.stress - amount, 0)

    def dmg_buff(self, damage):
        return damage * 1.5

    def dmg_reduction_buff(self, damage):
        return damage * 0.5
    
    def bleed(self):
        raise NotImplementedError("waiting to be implemented")
    
    def apply_poison(self, charges):
        poison_effect = next((effect for effect in self.stats.status_effects if effect['type'] == 'poison'), None)
        if poison_effect:
            poison_effect['charges'] += charges
        else:
            self.stats.status_effects.append({'type': 'poison', 'charges': charges})
        print(f"{self.name} has been poisoned! Poison charges: {charges}")

    def process_status_effects(self):
        for effect in self.stats.status_effects:
            if effect['type'] == 'poison':
                poison_damage = effect['charges']
                self.stats.health -= poison_damage
                effect['charges'] -= 1
                print(f"{self.name} takes {poison_damage} poison damage.")
                if effect['charges'] <= 0:
                    self.stats.status_effects.remove(effect)
                if self.stats.health <= 0:
                    self.death()
    
    def stun(self):
        raise NotImplementedError("need to implement for each combatant")
    
    def get_status_effects_str(self):
        return ", ".join([f"{effect['type']} {effect['charges']}" for effect in self.stats.status_effects])

    def __str__(self):
        return (f"Name: {self.name} \t Damage {self.stats.damage} \t Health {self.stats.health}/{self.stats.maxhealth} \t Armor {self.stats.armor} \t "
                f"Dodge {self.stats.dodge} \t Accuracy {self.stats.accuracy} \t Crit chance {self.stats.crit_chance}% \t Speed {self.stats.speed} \t "
                f"Stress {self.stats.stress}/100 \t Status effects {self.stats.status_effects}")