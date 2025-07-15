import random

player = {"hp": 100, "attack": 15, "defense": 10}
enemies = ["Goblin", "Skeleton", "Orc"]

def combat():
    enemy = random.choice(enemies)
    enemy_hp = random.randint(40, 70)
    enemy_attack = random.randint(10, 20)

    print(f"\nA wild {enemy} appears! (HP: {enemy_hp}, Attack: {enemy_attack})")

    while player["hp"] > 0 and enemy_hp > 0:
        print(f"\nYour HP: {player['hp']} | {enemy} HP: {enemy_hp}")
        print("1. Attack")
        print("2. Block")
        print("3. Heal (+20 HP)")
        choice = input("Choose action: ")

        if choice == "1":
            damage = random.randint(player["attack"] - 5, player["attack"] + 5)
            enemy_hp -= damage
            print(f"You attack and deal {damage} damage!")
        elif choice == "2":
            mitigated_damage = random.randint(5, 15)
            print(f"You block! (Reduce {mitigated_damage} damage)")
        elif choice == "3":
            player["hp"] = min(100, player["hp"] + 20)
            print("You heal 20 HP!")
        else:
            print("Invalid action. You waste a turn.")

        # Enemy's turn (if alive)
        if enemy_hp > 0 and choice != "2":
            damage = max(0, random.randint(enemy_attack - 5, enemy_attack + 5))
            player["hp"] -= damage
            print(f"The {enemy} attacks you for {damage} damage!")
        elif enemy_hp > 0:
            damage = max(0, random.randint(enemy_attack - 5, enemy_attack + 5) - mitigated_damage)
            player["hp"] -= damage
            print(f"The {enemy} attacks, but you reduce damage to {damage}!")

    if player["hp"] <= 0:
        print("\nYou were defeated! GAME OVER.")
    else:
        print(f"\nYou defeated the {enemy}! VICTORY!")

def mini_rpg():
    print("=== MINI RPG ===")
    print("Fight dangerous creatures. Survive!")

    while player["hp"] > 0:
        input("\nPress Enter to search for an enemy...")
        combat()
        if player["hp"] <= 0:
            break
        print("\nContinue? (y/n)")
        if input().lower() != "y":
            break
mini_rpg()
print("Thanks for playing!")