from characters import knight
from enemies import skeleton
from bp import bpchar

def fight(char, enemy):
    if char.speed >= enemy.speed:
        first, second = char, enemy
    else:
        first, second = enemy, char

    while char.health > 0 and enemy.health > 0:
        for current, target in [(first, second), (second, first)]:
            if current.health <= 0 or target.health <= 0:
                break
            
            print(f"\n{current.name}'s turn:")
            if isinstance(current, knight):
                action = current.take_action()
                while action not in ["1", "2", "3"]:
                    print("pick an action")
                    action = current.take_action()
                if action == '1':
                    damage, stress_damage = current.action1()
                    if target.dodge_chance():
                        print(f"{target.name} dodged attack.")
                    else:
                        target.dmg_taken(damage)
                        print(f"{current.name} attacks {target.name} for {bpchar.dmg_armor(damage, target.armor)} HP.")
                        if stress_damage > 0:
                            current.stress_heal(stress_damage)
                            print(f"{current.name} heals {stress_damage} stress.")
                elif action == '2':
                    heal_amount, stress_damage = current.action2()
                    print(f"{current.name} heals himself for {heal_amount} HP.")
                    if stress_damage > 0:
                        current.stress_heal(stress_damage)
                        print(f"{current.name} heals {stress_damage} stress.")
                elif action == '3':
                    current.action3()
                    print(f"{current.name} is blocking")
            else:
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
            
            print(f"{char.name}: {char.health}/{char.maxhealth} HP \t {char.stress}/100")
            print(f"{enemy.name}: {enemy.health}/{enemy.maxhealth} HP")
            
            if char.death() or enemy.death():
                break


# name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects
knight_stats = knight("Reynauld", (3, 6), 35, 35, 1, 10, 100, 1, 0, [])
enemy_stats = skeleton("Enemy", (2, 5), 30, 30, 0, 0, 100, 2, 0, [])
print(knight_stats)
print(enemy_stats)
fight(knight_stats, enemy_stats)
#TODO
#więcej niż 1 postać
#statusy
#resisty
#miejsca
#blokada umiejętności jak zła pozycja

#znane błędy:
#1) Reynauld heals himself for (3, False) HP.  XD? (nie umiem odtworzyć, możliwe że załatane jak zmieniałem kod)