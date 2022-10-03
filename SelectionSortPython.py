# Selection sort in Python
import math

# Method to perform selection sort
# Takes in a paramater list_to_sort
def selection_sort(list_to_sort):

    # Set the current_minimum to a large number
    # Obviously this does create limitations
    current_minimum = 1000000
    current_item = 0
    current_minimum_index = 0

    # Iterate over the list from left to right
    for sorted_partition_marker in range(0, len(list_to_sort)):

        # Iterate from the start of the unsorted partition to the end of the list
        for current_item in range(sorted_partition_marker, len(list_to_sort)):

            # If the current item is less than the current minimum log the index of the current minimum
            if int(list_to_sort[current_item]) < int(current_minimum):
                current_minimum = list_to_sort[current_item]
                current_minimum_index = current_item

        # 2 elements:
        # The element that indicates the sorted/unsorted partition marker
        # The current minimum
        # These elements are sorted
        temp = list_to_sort[sorted_partition_marker]
        list_to_sort[sorted_partition_marker] = current_minimum
        list_to_sort[current_minimum_index] = temp

        # Reset the current_minimum and current_minimum_index
        current_minimum = 1000000
        current_minimum_index = 0
    return list_to_sort

# Main method to get the input from the user, perform selection sort and output the results
def main ():
    user_input = input("Enter numbers separated by a space: ")

    # Split the input into a list using split
    number_list = user_input.split(" ")

    # Carry out selection sort on this list
    sorted_list = selection_sort(number_list)

    # Print out the sorted list
    print ("Sorted list")
    for x in sorted_list:
        print(x)

# Call the main method
main()
