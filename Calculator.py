# Main program function

def main():

    # Allow the user to choose between addition, subtraction, multiplication and division
    choice: str = user_choice()

    # While choice does not equal "5" (exit program), run the program
    while choice != "5":

        # 1 = addition
        if choice == "1":
            result = addition(first_number=get_first_number(), second_number=get_second_number())
            print("The result is " + str(result))

        # 2 = subtraction
        if choice == "2":
            result = subtraction(first_number=get_first_number(), second_number=get_second_number())
            print("The result is " + str(result))

        # 3 = multiplication
        if choice == "3":
            result = multiplication(first_number=get_first_number(), second_number=get_second_number())
            print("The result is " + str(result))

        # 4 = division
        if choice == "4":
            result = division(first_number=get_first_number(), second_number=get_second_number())
            print("The result is " + str(result))

        # Allow the user to select a new operation or quit the program
        choice = user_choice()

    # When 5 is pressed, break out of the while loop and exit the program
    else:
        print("Thanks for using the Python calculator")
        quit()


# Function to manage asking for the operator
def user_choice():
    user_input: str = input("Press 1 for addition, 2 for subtraction, 3 for subtraction, 4 for multiplication, "
                            "5 to exit: ")
    return user_input


# Function for getting first number through user input
def get_first_number():
    number1 = input("Enter first number: ")
    return number1


# Function for getting second number through user input
def get_second_number():
    number2 = input("Enter second number: ")
    return number2


# Function for addition
def addition(first_number, second_number):

    # Try to return the sum of the two numbers. If an input is invalid, a message is displayed and the main program
    # is re-run
    try:
        return float(first_number) + float(second_number)
    except ValueError:
        print ("Invalid input")
        # Re-run the main function
        main()


# Function for subtraction
def subtraction(first_number, second_number):
    # Try to return the difference of the two numbers. If an input is invalid, a message is displayed and the main
    # program is re-run
    try:
        return float(first_number) - float(second_number)
    except ValueError:
        print("Invalid input")
        # Re-run the main function
        main()


# Function for multiplication
def multiplication(first_number, second_number):
    # Try to return the product of the two numbers. If an input is invalid, a message is displayed and the main
    # program is re-run
    try:
        return float(first_number) * float(second_number)
    except ValueError:
        print("Invalid input")
        # Re-run the main function
        main()


# Function for division
def division(first_number, second_number):
    # Try to return the division of the two numbers. If an input is invalid, a message is displayed and the main
    # program is re-run
    try:
        return float(first_number) / float(second_number)
    except ValueError:
        print("Invalid input")
        # Re-run the main function
        main()


# Welcome the user
print("Welcome to the python calculator")

# Call the main game function
main()
