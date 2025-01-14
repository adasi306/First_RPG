import random


class CharacterStats:
    def __init__(
        self,
        damage,
        #        health,
        maxhealth,
        armor,
        dodge,
        accuracy,
        crit_chance,
        speed,
        stress,
        status_effects,
        bleed_resist,
        poison_resist,
        stun_resist,
    ):
        self.damage = damage
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.armor = armor
        self.dodge = dodge
        self.accuracy = accuracy
        self.crit_chance = crit_chance
        self.speed = speed
        self.stress = stress
        self.status_effects = status_effects
        self.bleed_resist = bleed_resist
        self.poison_resist = poison_resist
        self.stun_resist = stun_resist


class BlueprintCharacter:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.base_accuracy = stats.accuracy
        self.base_damage = stats.damage
        self.damage_modifier = 1.0
        self.healing_modifier = 1.0
        self.dead = False

    def attack(self):
        raise NotImplementedError(
            "This method needs to be implemented for each character"
        )

    def death(self):
        raise NotImplementedError(
            "This method needs to be implemented for each faction"
        )

    def heal(self, amount):
        adjusted_heal = round(amount * self.healing_modifier)
        self.stats.health += adjusted_heal
        if self.stats.health > self.stats.maxhealth:
            self.stats.health = self.stats.maxhealth
        print(f"\n{self.name} heals for {adjusted_heal} HP.")

    def dmg_armor(self, damage, armor):
        return max(damage - armor, 0)

    def dmg_taken(self, damage):
        if any(effect["type"] == "mark" for effect in self.stats.status_effects):
            print("\njd")
            damage = round(damage * 1.5)
            print(f"\n{self.name} is marked! Takes {damage} damage.")
        true_damage = max(round(damage - self.stats.armor), 0)
        self.stats.health = max(self.stats.health - true_damage, 0)
        self.stress_()
        if self.stats.health <= 0 and not self.dead:
            self.death()
        return true_damage

    def block(self, damage):
        reduced_damage = round(damage * 0.5)
        true_damage = self.dmg_taken(reduced_damage)
        return true_damage, reduced_damage

    def crit(self, damage):
        return (
            round(damage * 2)
            if random.randint(1, 100) <= self.stats.crit_chance
            else damage
        )

    def if_attack_hit(self):
        return random.randint(1, 100) > self.stats.accuracy

    def roll_dodge(self):
        return random.randint(1, 100) <= self.stats.dodge * 5

    def stress_(self):
        self.stats.stress = max(0, min(self.stats.stress, 100))
        if self.stats.stress >= 0 and self.stats.stress <= 10:
            self.stats.accuracy = self.base_accuracy
            self.damage_modifier = 1.0
            self.healing_modifier = 1.0
        elif self.stats.stress > 10 and self.stats.stress <= 25:
            self.damage_modifier = 1.1
            self.stats.accuracy = self.base_accuracy * 0.95
        elif self.stats.stress > 25 and self.stats.stress <= 50:
            self.damage_modifier = 1.0
            self.stats.accuracy = self.base_accuracy * 0.85
        elif self.stats.stress > 50 and self.stats.stress <= 75:
            self.stats.accuracy = self.base_accuracy * 0.80
            self.healing_modifier = 0.95
        elif self.stats.stress > 75 and self.stats.stress <= 100:
            self.stats.accuracy = self.base_accuracy * 0.80
            self.healing_modifier = 0.85

    def stress_heal(self, amount):
        self.stats.stress = max(self.stats.stress - amount, 0)

    # uładnić i skrócić jak bym umiał
    def apply_status_effect(self, effect_type, charges):
        if (
            effect_type == "poison"
            and random.randint(1, 100) <= self.stats.poison_resist
        ):
            print(f"\n{self.name} resisted poison!")
            return
        elif (
            effect_type == "bleed" and random.randint(1, 100) <= self.stats.bleed_resist
        ):
            print(f"\n{self.name} resisted bleed!")
            return

        existing_effect = next(
            (
                effect
                for effect in self.stats.status_effects
                if effect["type"] == effect_type
            ),
            None,
        )

        if existing_effect:
            existing_effect["charges"] += charges
        else:
            self.stats.status_effects.append({"type": effect_type, "charges": charges})

        print(
            f"\n{self.name} has been affected by {effect_type} with {charges} charges."
        )

    def process_status_effects(self, taunter=None):
        effects_to_remove = []

        stun_effect = next(
            (
                effect
                for effect in self.stats.status_effects
                if effect["type"] == "stun"
            ),
            None,
        )
        taunt_effect = next(
            (
                effect
                for effect in self.stats.status_effects
                if effect["type"] == "taunt"
            ),
            None,
        )

        if stun_effect and taunt_effect:
            print(f"\n{self.name} is stunned and taunted but skips their turn.")
            self.stats.status_effects.remove(stun_effect)
            self.stats.status_effects.remove(taunt_effect)
            return True

        if stun_effect:
            if random.randint(1, 100) <= self.stats.stun_resist:
                print(f"\n{self.name} resisted stun!")
                self.stats.status_effects.remove(stun_effect)
            else:
                print(f"\n{self.name} is stunned and skips their turn.")
                self.stats.status_effects.remove(stun_effect)
                return True

        if taunter:
            if taunt_effect:
                print(
                    f"\n{self.name} is already taunted by {taunt_effect['taunter'].name}!"
                )
            else:
                self.stats.status_effects.append({"type": "taunt", "taunter": taunter})
                print(f"\n{self.name} is taunted and must attack {taunter.name}!")
        elif taunt_effect:
            print(
                f"\n{self.name} is taunted and must attack {taunt_effect['taunter'].name}!"
            )
            self.stats.status_effects.remove(taunt_effect)
            return taunt_effect

        for effect in self.stats.status_effects[:]:
            if effect["type"] == "poison":
                poison_damage = effect["charges"]
                self.stats.health -= poison_damage
                print(f"\n{self.name} takes {poison_damage} poison damage.")
                effect["charges"] -= 1
                if effect["charges"] <= 0:
                    effects_to_remove.append(effect)

            elif effect["type"] == "bleed":
                bleed_damage = effect["charges"]
                self.stats.health -= bleed_damage
                effect["charges"] = max(0, round(effect["charges"] * 0.5))
                print(f"\n{self.name} takes {bleed_damage} bleed damage.")
                if effect["charges"] <= 0:
                    effects_to_remove.append(effect)

            elif effect["type"] == "mark":
                effect["charges"] -= 1
                if effect["charges"] <= 0:
                    effects_to_remove.append(effect)
                    print(f"\n{self.name} is no longer marked.")

            if self.stats.health <= 0:
                self.death()
                break

        for effect in effects_to_remove:
            self.stats.status_effects.remove(effect)

        return False

    def get_status_effects_str(self):
        effects = []
        for effect in self.stats.status_effects:
            if effect["type"] == "stun":
                effects.append(f"stun")
            elif effect["type"] == "taunt":
                effects.append(f"taunt")
            else:
                effects.append(f"{effect['type']} {effect['charges']}")
        return ", ".join(effects)

    def assign_positions(ally_team, is_player=True):
        if is_player:
            print("\nAssign positions for your characters (choose between 1 to 4):")
            available_positions = list(range(1, 5))
            for character in ally_team:
                while True:
                    try:
                        pos = int(input(f"Choose position for {character.name}: "))
                        if pos in available_positions:
                            character.position = pos
                            available_positions.remove(pos)
                            break
                        else:
                            print(
                                "\nInvalid position or position already taken. Choose again."
                            )
                    except ValueError:
                        print("\nInvalid input. Please enter a number between 1 and 4.")
        else:
            for i, character in enumerate(ally_team):
                character.position = i + 1

    def update_positions(team):
        position = 1
        for character in team:
            if not character.dead:
                character.position = position
                position += 1

    def gain_xp(self, amount):
        self.stats.xp += amount
        print(f"\n{self.name} gained {amount} XP!")

    def __str__(self):
        return (
            f"\nName: {self.name} \t Damage {self.stats.damage} \t Health {self.stats.health}/{self.stats.maxhealth} \t Armor {self.stats.armor} \t "
            f"Dodge {self.stats.dodge} \t Accuracy {self.stats.accuracy} \t Crit chance {self.stats.crit_chance}% \t Speed {self.stats.speed} \t "
            f"Stress {self.stats.stress}/100 \t Status effects {self.stats.status_effects}"
        )
