from characters import knight, rouge
from enemies import skeleton
from bp import bpchar
import random

def fight(chars, enemies):
    all_combatants = chars + enemies
    sorted_combatants = []
    while all_combatants:
        fastest = all_combatants[0]
        for combatant in all_combatants:
            if combatant.speed > fastest.speed:
                fastest = combatant
        sorted_combatants.append(fastest)
        all_combatants.remove(fastest)

    all_combatants = sorted_combatants

    while any(char.health > 0 for char in chars) and any(enemy.health > 0 for enemy in enemies):
        for current in all_combatants:
            if current.health <= 0:
                continue  # Skip dead characters

            # Przetwarzanie efektów statusu przed rozpoczęciem tury
            current.process_status_effects()

            if current.health <= 0:
                continue  # Skip further actions if character died from poison

            if current in chars:
                target_team = enemies
                ally_team = chars
            else:
                target_team = chars
                ally_team = enemies

            if all(target.health <= 0 for target in target_team):
                break  # If all targets in the opposing team are dead, end the fight

            print(f"\n{current.name}'s turn:")
            if isinstance(current, (knight, rouge)):
                action = current.take_action()
                while action not in ["1", "2", "3"]:
                    print("pick an action")
                    action = current.take_action()

                # Obsługa różnych akcji
                if action == '1':  # Atak
                    target = current.choose_target([t for t in target_team if t.health > 0])
                    damage, stress_damage = current.action1()
                    if target.dodge_chance():
                        print(f"{target.name} dodged attack.")
                    elif current.if_attack_hit():
                        print(f"{current.name} missed attack.")
                    else:
                        target.dmg_taken(damage)
                        print(f"{current.name} attacks {target.name} for {bpchar.dmg_armor(damage, target.armor)} HP.")
                        if stress_damage > 0:
                            current.stress_heal(stress_damage)
                            print(f"{current.name} heals {stress_damage} stress.")

                elif action == '2':  # Leczenie (tylko dla `knight` - wybór sojusznika)
                    if isinstance(current, knight):
                        target = current.choose_target([t for t in ally_team if t.health > 0])  # Wybór sojusznika do leczenia
                        heal_amount, stress_damage = current.action2()
                        target.heal(heal_amount)
                        print(f"{current.name} heals {target.name} for {heal_amount} HP.")
                        if stress_damage > 0:
                            current.stress_heal(stress_damage)
                            print(f"{current.name} heals {stress_damage} stress.")
                    else:  # `rouge` atak z trucizną
                        target = current.choose_target([t for t in target_team if t.health > 0])
                        damage, stress_damage, poison_charges = current.action2()
                        if target.dodge_chance():
                            print(f"{target.name} dodged attack.")
                        elif current.if_attack_hit():
                            print(f"{current.name} missed attack.")
                        else:
                            target.dmg_taken(damage)
                            target.apply_poison(poison_charges)  # Nakłada truciznę jako efekt statusu
                            print(f"{current.name} attacks {target.name} for {bpchar.dmg_armor(damage, target.armor)} HP and applies {poison_charges} poison charges.")
                            if stress_damage > 0:
                                current.stress_heal(stress_damage)
                                print(f"{current.name} heals {stress_damage} stress.")

                elif action == '3':  # Blokowanie (nie wymaga wyboru celu)
                    current.action3()
                    print(f"{current.name} is blocking")

            else:
                # Enemy's turn to attack (przeciwnik atakuje losowo)
                target = random.choice([t for t in chars if t.health > 0])
                damage, stress_damage = current.attack()
                if target.dodge_chance():
                    print(f"{target.name} dodged attack.")
                else:
                    if target.blocking:
                        target.stress += stress_damage
                        true_damage, blocked_damage = target.block(damage)
                        print(f"{current.name} attacks {target.name} for {true_damage} HP. Blocked damage: {blocked_damage}.")
                    else:
                        target.stress += stress_damage
                        target.dmg_taken(damage)
                        print(f"{current.name} attacks {target.name} for {bpchar.dmg_armor(damage, target.armor)} HP.")
                    if stress_damage > 0:
                        print(f"{target.name} gains {stress_damage} stress.")
            
            # Print status of all combatants
            for char in chars:
                print(f"{char.name}: {char.health}/{char.maxhealth} HP \t {char.stress}/100 Stress \t Status: {char.get_status_effects_str()}")
            for enemy in enemies:
                print(f"{enemy.name}: {enemy.health}/{enemy.maxhealth} HP \t Status: {enemy.get_status_effects_str()}")

            # Check if the current character died
            current.death()

            # Remove dead characters from the combatants list
            all_combatants = [c for c in all_combatants if c.health > 0]

        if all(enemy.health <= 0 for enemy in enemies):
            print("All enemies are defeated!")
            break
        elif all(char.health <= 0 for char in chars):
            print("All your characters are defeated!")
            break



# Example usage:

# Create a list of player characters
heroes = [
    knight("Reynauld", (3, 6), 35, 35, 1, 10, 100, 0, 1, 0, []),
    rouge("Dismas", (4, 7), 30, 30, 1, 12, 95, 0, 3, 0, []),
    rouge("Dismas", (4, 7), 30, 30, 1, 12, 95, 0, 3, 0, []),
]

# Create a list of enemy characters
enemies = [
    skeleton("Skeleton 1", (2, 5), 30, 30, 0, 0, 0, 100, 2, 0, []),
    skeleton("Skeleton 2", (3, 6), 25, 25, 0, 0, 0, 100, 2, 0, []),
]

# Start the fight
fight(heroes, enemies)
#TODO
#statusy
#resisty
#miejsca
#złe pozycje
#zapis postaci

#znane błędy:
#póki co chyba brak