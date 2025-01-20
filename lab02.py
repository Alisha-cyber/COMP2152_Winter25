import random

try:
    # Define the array of weapons
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

    # Roll the dice (1-6)
    weaponRoll = random.randint(1, 6)

    # Ensure weaponRoll is an integer (though randint always returns an int)
    if not isinstance(weaponRoll, int):
        raise ValueError("Error: weapon roll is not an integer.")

    # Use weaponRoll as an index into the weapons array (adjust for 0-based indexing)
    chosen_weapon = weapons[weaponRoll - 1]

    # Define the hero's base combat strength
    hero_combat_strength = 100
    hero_combat_strength += weaponRoll

    # Define the conditions for weapon roll
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Check if the weapon rolled is not "Fist"
    if chosen_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

    # Print the results
    print("Weapon roll:", weaponRoll)
    print("Chosen weapon:", chosen_weapon)
    print("Hero's new combat strength:", hero_combat_strength)

except ValueError as ve:
    # Handle value errors
    print("Error:", ve)
    print("The program encountered an issue with the dice roll or inputs.")

except Exception as e:
    # Handle any other unexpected errors
    print("An unexpected error occurred:", e)
    print("Please check the program logic.")

