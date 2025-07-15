import random

crew = ["Captain", "Scientist", "Engineer", "Medic"]
ship_status = {"oxygen": 100, "fuel": 100, "morale": 100}

def space_adventure():
    print("=== SPACE ADVENTURE ===")
    print(f"Crew: {', '.join(crew)}")
    print("Your ship enters an unknown galaxy...")

    while True:
        print(f"\nShip Status: Oxygen ({ship_status['oxygen']}%), Fuel ({ship_status['fuel']}%), Morale ({ship_status['morale']}%)")
        print("\nOptions:")
        print("1. Explore a nearby planet")
        print("2. Repair ship systems")
        print("3. Hibernate and wait for help")
        choice = input("What will you do? ")

        if choice == "1":
            event = random.choice(["friendly_alien", "radiation_storm", "habitable_planet"])
            if event == "friendly_alien":
                print("\nYou meet a peaceful civilization! They offer resources.")
                ship_status["fuel"] += 20
            elif event == "radiation_storm":
                print("\nRadiation storm! Oxygen and morale drop.")
                ship_status["oxygen"] -= 30
                ship_status["morale"] -= 15
            else:
                print("\nHabitable planet. The crew rests. +Morale.")
                ship_status["morale"] += 25
        elif choice == "2":
            print("\nYou repair the ship. Oxygen and fuel improve.")
            ship_status["oxygen"] = min(100, ship_status["oxygen"] + 40)
            ship_status["fuel"] += 10
        elif choice == "3":
            print("\nYou hibernate... but the ship runs out of power. GAME OVER.")
            break

        # Check game over conditions
        if ship_status["oxygen"] <= 0 or ship_status["morale"] <= 0:
            print("\nThe crew didn't survive. GAME OVER.")
            break
        elif ship_status["fuel"] >= 150:
            print("\nYou found the way home! VICTORY.")
            break
    space_adventure()
    print("Thanks for playing!")