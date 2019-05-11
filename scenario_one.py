"""
Scenario 1: One-time route cost check
You have a carrier route list with 100,000 (100K) entries (in arbitrary order) 
and a single phone number. How quickly can you find the cost of calling this number?
"""

# Scenario One Pseudocode:
# Given: Route-Costs of 100,000 numbers. One Phone Number
# Output: Find the cost of calling that number
# 
def phone_route_cost_check(filename, number):
    """
    We saved performance when reading the file. We sorted each line into a string in an array.
    The trade of is that it makes it slower to read the contents of the string.

    The list gets smaller each recursion by taking out values that are not similar.

    Best case scenario: 0.95 (seconds) O(n) [If the number is found in its entirety]
    Worse case scenario: 18.70 (seonds) O(log(n)) [If the item is not matching even the first 2 numbers with any of the number on the list]
    """
    open_file = open(filename, 'r')
    data_array = open_file.read().split('\n') # O(n)
    # print(data_array)
    phone_search(data_array, number) # O(log(n))
    open_file.close()

def phone_search(array, number, recursion=5):
    new_array = []

    for item in array: # O(n^2)
        current_number = ""
        cost = ""
        index = 0

        # Remove the cost
        for char in item:
            if char == ',':
                current_number = item[0:index]
                cost = item[index + 1:len(item)]
            index += 1
        # print("Current number:",current_number)

        # print("Current cost:",cost)
        # Check if it matches perfectly with the number.
        if current_number == number:
            # print('cost of', number, ":", cost)
            return cost # Return cost.

        # We compare the first 5 characters. Recursion 
        elif current_number[0:recursion] == number[0:recursion]:
            # if it matches append into new array
            new_array.append(item)

    # Return new array
    # print(new_array)
    if len(new_array) == 1:
        cost = new_array[0][len(new_array[0]) - 4: len(new_array[0])]
        # print("item cost:", cost)
        return cost
    elif len(new_array) > 1:
        # Return lowest cost
        costs_array = []
        # For each item in the new array: get all the costs and return the lowest value.
        for item in new_array: # O(n^2)
            # print("current item:", item)
            count = 0
            for char in item:
                if char == ',':
                    cost = str(item[count + 1:len(item)])
                    # print("Cost while sorting new array:", cost)
                    cost_as_number = float(cost)
                    costs_array.append(cost_as_number)
                count += 1

        # pick the smallest
        costs_array.sort()
        # print("all costs in new array:", costs_array)
        # print("Smallest value:", costs_array[0])
        return costs_array[0] # return smallest value
    else: # if the array is empty
        if recursion > 3:
            return phone_search(new_array, number, recursion - 1)
        else:
            return None

# print out the number of the phone numbers

print(phone_route_cost_check("text_files/route-costs-10000000.txt", '+55555'))
# routefile = open("route-costs-106000.txt").read().split("\n")
# phonenum = "+861721532"
# print("Looking for", phonenum)

