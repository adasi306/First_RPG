from characters import knight, rouge
from enemies import skeleton
from blueprint import BlueprintCharacter
import random

def fight(chars, enemies):
    all_combatants = chars + enemies
    sorted_combatants = []
    while all_combatants:
        fastest = all_combatants[0]
        for combatant in all_combatants:
            if combatant.stats.speed > fastest.stats.speed:
                fastest = combatant
        sorted_combatants.append(fastest)
        all_combatants.remove(fastest)

    all_combatants = sorted_combatants

    while any(char.stats.health > 0 for char in chars) and any(enemy.stats.health > 0 for enemy in enemies):
        for current in all_combatants:
            if current.stats.health <= 0:
                continue  # Skip dead characters

            # activate status
            current.process_status_effects()

            if current.stats.health <= 0:
                continue  # Skip further actions if character died from status

            if current in chars:
                target_team = enemies
                ally_team = chars
            else:
                target_team = chars
                ally_team = enemies

            if all(target.stats.health <= 0 for target in target_team):
                break  # If all targets in the opposing team are dead, end the fight

            print(f"\n{current.name}'s turn:")
            if isinstance(current, (knight, rouge)):
                action = current.take_action()
                while action not in ["1", "2", "3"]:
                    print("pick an action")
                    action = current.take_action()

                if action == '1':
                    current.action1(ally_team, target_team)
                elif action == '2':
                    current.action2(ally_team, target_team)

                elif action == '3':
                    current.action3(ally_team, target_team)

            else:
                # enemies turn
                target = random.choice([t for t in chars if t.stats.health > 0])
                damage, stress_damage = current.attack()
                if target.roll_dodge():
                    print(f"{target.name} dodged attack.")
                else:
                    if target.blocking:
                        target.stats.stress += stress_damage
                        true_damage, blocked_damage = target.block(damage)
                        print(f"{current.name} attacks {target.name} for {true_damage} HP. Blocked damage: {blocked_damage}.")
                    else:
                        target.stats.stress += stress_damage
                        target.dmg_taken(damage)
                        print(f"{current.name} attacks {target.name} for {BlueprintCharacter.dmg_armor(damage, target.stats.armor)} HP.")
                    if stress_damage > 0:
                        print(f"{target.name} gains {stress_damage} stress.")
            
            # Print status of all combatants
            for char in chars:
                print(f"{char.name}: {char.stats.health}/{char.stats.maxhealth} HP \t {char.stats.stress}/100 Stress \t Status: {char.get_status_effects_str()}")
            for enemy in enemies:
                print(f"{enemy.name}: {enemy.stats.health}/{enemy.stats.maxhealth} HP \t Status: {enemy.get_status_effects_str()}")

            # Check if the current character died
            current.death()

            # Remove dead characters from the combatants list
            all_combatants = [c for c in all_combatants if c.stats.health > 0]

        if all(enemy.stats.health <= 0 for enemy in enemies):
            print("All enemies are defeated!")
            break
        elif all(char.stats.health <= 0 for char in chars):
            print("All your characters are defeated!")
            break


# list of heroes
heroes = [
    knight("Reynauld", (3, 6), 35, 35, 1, 10, 100, 0, 1, 0, []),
    rouge("Dismas1", (4, 7), 30, 30, 1, 12, 95, 0, 3, 0, []),
    rouge("Dismas2", (4, 7), 30, 30, 1, 12, 95, 0, 3, 0, []),
]

# list of enemies
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