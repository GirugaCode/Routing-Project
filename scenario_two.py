"""
Scenario 2: List of route costs to check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order) 
and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?
"""

def phone_route_cost_check(route_file, number_file):
    """
    Code will break if there is an extra line in the text files

    Previously we were checking every digit of the number to match the route cost. We then set
    a condition to only check if the recursive amount is under three digits

    Best Case scenario: 8.0 (seconds) O(n^2) where we iterated through both the dictionary and the dictionary keys
    Worst Case scenario: 44.68 (seconds) O(n^2) where we iterate through the dictionary, phone numbers and do conduct
    a recursive call

    We could optimize the runtime by replacing the arrays with sets.
    """
    open_file = open(route_file, 'r')
    # data_array = open_file.read().split('\n').split(',')
    route_dict = dict(item.split(",") for item in open_file.read().split("\n")) #O(n^2)
    # print("Route Dictionary:", route_dict)
    open_file.close() 
    number_array = phone_numbers(number_file) #O(n)
    # print("Number Array:",number_array)
    # print(route_dict['+492885555'])
    return (phone_search(route_dict, number_array)) #O(n^3)
    

def phone_numbers(filename):
    open_file = open(filename, 'r')
    data_array = open_file.read().split('\n')
    return data_array

def phone_search(route_dict, numbers_array):
    # Get keys into the array
    key_array = route_dict.keys()
    key_value_array = []
    # Loop through the array of phone numbers
    for current_num in numbers_array:
        # If dictionary key index of the current number matches the current number
        if route_dict.get(current_num, None) is not None:
            # print("Cost:",route_dict[current_num])
            # save the key-value pair as string into an array
            string = current_num + "," + route_dict[current_num]
            # print("String:", string)
            key_value_array.append(string)
        # Else
        else:
            recursive_cost = recursive_array(route_dict, key_array, current_num)
            if recursive_cost is None:
                key_value_array.append(current_num + "," + "None")
            else:
                key_value_array.append(current_num + "," + recursive_cost)  
            # Return the dictionary's lowest value
            # Save the current cost return with the current phone number into key-value array
    # Return the key-value string array
    if len(key_value_array) > 0: 
        return key_value_array
    else:
        return None

def recursive_array(route_dict, key_array, current_num, recursive = 5):
    cost_array = []
    # Loop through the keys array
    for key in key_array:
        # Each phone number will have the closest cost and will be appended into the key-value string array
        # Compare the first five numbers of key to the first five numbers of the current number
        # If it matches append into new array
        if current_num[0:recursive] == key[0:recursive]: # TODO: Replace 5 for a recursion
            # Append any matches
            cost_array.append(float(route_dict[key]))
    # print("Cost Array:", cost_array)
    cost_array.sort()
    # print("It works!")
    if len(cost_array) > 0 :
        return str(cost_array[0])
    else:
        if recursive > 3: 
            return recursive_array(route_dict, key_array, current_num, recursive - 1)
        else:
            return None

phone_route_cost_check('text_files/route-costs-106000.txt', 'text_files/phone-numbers-1000.txt')