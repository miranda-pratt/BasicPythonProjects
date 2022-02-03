# Main function for the main program
def main():
    # Welcome the user
    print("Welcome to Mad-libs")

    # Collect information
    name = input("Enter a name: ")
    age = input("Enter an age: ")
    monster = input("Enter a monster: ")
    weapon = input("Enter a weapon: ")

    number = int(input("Enter a number greater than 1: "))
    # While loop to only let the user enter a number greater than 1
    # If number is greater than 1, repeat the input until number is greater than 1
    while number < 1:
        print("Invalid number, please try again")
        number = int(input("Enter a number greater than 1: "))
    # Cast number back to string
    number = str(number)
    food = input("Enter a food: ")
    place = input("Enter a place: ")

    # Call the save_in_file method with the information collected as arguments
    save_in_file(name, age, monster, weapon, food, place, number)
    print("Open the file Story.txt to view the story ")


# Save in_file function to store the information and the story in a file
# Parameters from the information collected earlier.
def save_in_file(character_name, character_age, character_monster, character_weapon, character_food, character_place,
                 character_number):
    # Open a file (or create the file if it no longer exists
    # "w" means overwrite pre-existing contents (if any)
    file = open("Story.txt", "w")
    # Write the story using the parameters
    # Spaces and new line have to be hardcoded
    file.write(character_name + " is " + character_age + " years old.\n" + character_name + " was going to " +
               character_place + "\nBut " + character_name + " saw an angry " + character_monster +
               " blocking the path.\n" + character_name + " tried to attack the " + character_monster + " with "
               + character_weapon + " " + character_number + " times but this did not work. \nEventually " +
               character_name + " decided to give the " + character_monster + " some " + character_food + ".\nThe " +
               character_monster + " loved it and let " + character_name + " live and so " + character_name +
               " was able to continue to travelling to " + character_place + ".")
    # Close the file
    file.close()


# Call the main function
main()
