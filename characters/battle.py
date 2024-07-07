from characters import knight
from enemies import skeleton

def fight(char, enemy):
    while char.health > 0 and enemy.health > 0:
        print(f"\n{char.name}'s turn:")
        action = input("Choose action: (1) Attack1 (2) Attack2 (3) Block\n")
        if action == '1':
            damage = char.attack1()
            enemy.enemy_dmg_taken(damage)
            if damage - enemy.armor < 0:
                xd = 0
            else:
                xd = damage - enemy.armor
            print(f"{char.name} attacks {enemy.name} for {xd} damage.")
        elif action == '2':
            damage = char.attack2()
            enemy.enemy_dmg_taken(damage)
            if damage - enemy.armor < 0:
                xd = 0
            else:
                xd = damage - enemy.armor
            print(f"{char.name} attacks {enemy.name} for {xd} damage.")
        elif action == '3':
            char.block
        else:
            print(f"\n{enemy.name}'s turn:")
            damage = enemy.attack()
            char.char_dmg_taken(damage)
        if damage - char.armor < 0:
            xd = 0
        else:
            xd = damage - char.armor
        if char.health <= 0:
            char.health == 0
        if enemy.health <= 0:
            enemy.health == 0
        print(f"{enemy.name} attacks {char.name} for {xd} damage.")
        print(f"{char.name}: {char.health}/{char.maxhealth} HP")
        print(f"{enemy.name}: {enemy.health}/{enemy.maxhealth} HP")
        if char.char_death() or enemy.enemy_death():
            break
        

#name, damage, health, maxhealth, armor, dodge_chance, crit_chance, speed, stress, status_effects
knight_stats = knight("Reynauld", (3, 6), 35, 35, 1, 0, 10, 1, 0, [])
enemy_stats = skeleton("Enemy", (2, 5), 30, 30, 0, 0, 5, 1, 0, [])

fight(knight_stats, enemy_stats)
