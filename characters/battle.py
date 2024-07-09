from characters import knight
from enemies import skeleton
from bp import bpchar

def fight(char, enemy):
    bp = bpchar

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
                if action == '1':
                    damage = current.action1()
                    target.dmg_taken(damage)
                    print(f"{current.name} attacks {target.name} for {bp.dmg_armor(damage, target.armor)} HP.")
                elif action == '2':
                    heal_amount = current.action2()
                    print(f"{current.name} heals himself for {heal_amount} HP.")
                elif action == '3':
                    current.action3()
                    print(f"{current.name} is blocking")
            else:
                damage = current.attack()
                if target.blocking:
                    true_damage, blocked_damage = target.block(damage)
                    print(f"{current.name} attacks {target.name} for {true_damage} HP. Blocked damage: {blocked_damage}.")
                else:
                    target.dmg_taken(damage)
                    print(f"{current.name} attacks {target.name} for {bp.dmg_armor(damage, target.armor)} HP.")
            
            print(f"{char.name}: {char.health}/{char.maxhealth} HP")
            print(f"{enemy.name}: {enemy.health}/{enemy.maxhealth} HP")
            
            if char.death() or enemy.death():
                break


# name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects
knight_stats = knight("Reynauld", (3, 6), 35, 35, 1, 0, 10, 1, 0, [])
enemy_stats = skeleton("Enemy", (2, 5), 30, 30, 0, 0, 5, 2, 0, [])

fight(knight_stats, enemy_stats)
#TODO
#stres
#więcej niż 1 postać
#statusy
#miejsca