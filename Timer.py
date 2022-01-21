# Import time
# Necessary to ensure there is a one-second gap for each tick of the clock
# Otherwise the time would tick at the speed of the program, which is faster than one second
import time


# Main method for the program
def main():
    # Set user_input to be the result from get_time_length
    user_input = get_time_length()

    # An invalid input is a string or a number less than 0
    # If an input is invalid, display a message and recall the main() function
    if user_input.isnumeric():
        if int(user_input) < 0:

            print("Invalid input")
            main()

        else:
            # If user input is 0 create the ticking clock
            if str(user_input) != "0":

                # Loop through each second
                for x in range(0, int(user_input) + 1):

                    # Call the time tick method
                    time_tick(x, user_input)
                    # When the clock reaches 0, display 'time's up' and recall main()
                    if int(user_input) - x == 0:
                        print("Time's up")
                        main()

            # Else user enters 0 to exit, thank the user and exit the program
            else:
                print("Thanks for using the Python timer")
                quit()

    # Else display invalid input message and exit the program
    else:
        print("Invalid input")
        main()


# Method to ask user for how long the timer should be
def get_time_length():
    choice = input("Enter time in seconds or 0 to exit ")
    return choice


# Time tick method to display the time remaining
def time_tick(x, user_input):
    time.sleep(1)
    print(int(user_input) - x)


# Welcome the user and call the main method
print("Welcome to the Python timer")
main()
