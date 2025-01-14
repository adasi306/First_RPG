from characters import knight, rouge, hero
from blueprint import CharacterStats, BlueprintCharacter
from enemies import skeleton


def fight(chars, enemies):
    BlueprintCharacter.assign_positions(chars, is_player=True)
    BlueprintCharacter.assign_positions(enemies, is_player=False)
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

    while any(not char.dead for char in chars) and any(not enemy.dead for enemy in enemies):
        BlueprintCharacter.update_positions(chars)
        BlueprintCharacter.update_positions(enemies)
        print("\n--- Current team status ---")
        for char in chars:
            if not char.dead:
                print(f"{char.position}. {char.name}: {char.stats.health}/{char.stats.maxhealth} HP \t {char.stats.stress}/100 Stress \t Status: {char.get_status_effects_str()}")
        for enemy in enemies:
            if not enemy.dead:
                print(f"{enemy.position}. {enemy.name}: {enemy.stats.health}/{enemy.stats.maxhealth} HP \t Status: {enemy.get_status_effects_str()}")
        print("---------------------------")

        for current in sorted_combatants:
            if current.dead:
                continue

            status_effect = current.process_status_effects()

            if status_effect is True:
                continue

            if current.stats.stress >= 76:
                print(f"\n{current.name} is highly stressed, losing 2 HP and gaining 2 stress at the start of the turn.")
                current.stats.health -= 2
                current.stats.stress -= 2
                if current.stats.health <= 0:
                    current.death()
                    BlueprintCharacter.update_positions(chars)
                    continue

            if current.stats.health <= 0:
                current.death()
                BlueprintCharacter.update_positions(chars)
                continue

            if isinstance(current, hero):
                print(f"\n{current.name}'s turn:")
                action = current.take_action()
                while action not in ["1", "2", "3", "4", "5"]:
                    print("\nInvalid action. Choose again.")
                    action = current.take_action()

                if action == "1":
                    current.action1(chars, enemies)
                elif action == "2":
                    current.action2(chars, enemies)
                elif action == "3":
                    current.action3(chars, enemies)
                elif action == "4":
                    current.action3(chars, enemies)
                elif action == "5":
                    current.action3(chars, enemies)

            else:
                if status_effect and status_effect["type"] == "taunt":
                    target = status_effect["taunter"]
                else:
                    current.attack(chars)

            if all(enemy.dead for enemy in enemies):
                print("\nAll enemies are defeated!")
                return
            elif all(char.dead for char in chars):
                print("\nAll your characters are defeated!")
                return

        BlueprintCharacter.update_positions(chars)
        BlueprintCharacter.update_positions(enemies)

    print("\nAll your characters are defeated!")


heroes = [
    knight("Reynauld", CharacterStats((3, 6), 35, 10, 0, 100, 0, 1, 0, [], 30, 40, 20)),
    rouge("Dismas1", CharacterStats((4, 7), 30, 10, 0, 95, 0, 3, 0, [], 30, 50, 25)),
    rouge("Dismas2", CharacterStats((4, 7), 30, 10, 0, 95, 0, 3, 0, [], 30, 50, 25)),
]

enemies = [
    skeleton("Skeleton 1", CharacterStats((1, 2), 30, 0, 0, 0, 100, 2, 0, [], 0, 0, 0)),
    skeleton("Skeleton 2", CharacterStats((1, 2), 25, 0, 0, 0, 100, 2, 0, [], 0, 0, 0)),
]

fight(heroes, enemies)


# TODO
# naprawić statusy
# dodać postacie
# dodać resztę skilli których na obecną chwilę z jakiegoś powodu nie mogę dadać (np buffy)
# przetestować wszystkie klasy
# złe pozycje
# dodać quirki
# dodać progress postaci
# dodać przeciwników
# zapis postaci

# znane błędy:

# pokazywanie dobrych pozycji


# import os
# input("Press Enter to continue...")
# os.system('cls')


# XD? wszyscy przed już mieli ten status nagle po prostu znów im wyjebało wszystkim naraz

# Reynauld is highly stressed, losing 2 HP and 2 stress at the start of the turn.
# jd
# you died
# Dismas1 is highly stressed, losing 2 HP and 2 stress at the start of the turn.
# jd
# you died
# Dismas2 is highly stressed, losing 2 HP and 2 stress at the start of the turn.


# bonus dmg z mark nie działa
# już działa, ale pokazuje źle
#Skeleton 1 is marked! Takes 6 damage.
#Reynauld attacks Skeleton 1 for 4 HP.
