"""
Scenario 2: List of route costs to check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order) 
and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?
"""

def phone_route_cost_check(route_file, number_file):
    """
    """
    open_file = open(route_file, 'r')
    # data_array = open_file.read().split('\n').split(',')
    dictionary = dict(item.split(",") for item in open_file.read().split("\n"))
    print(dictionary)
    open_file.close() 
    number_array = phone_numbers(number_file)
    print(number_array)
    

def phone_numbers(filename):
    open_file = open(filename, 'r')
    data_array = open_file.read().split('\n')
    return data_array

def phone_search(dict, array):
    pass
    # Get keys into the array
    key_array = dict.keys()
    key_value_array = []
    # Loop through the array of phone numbers
    
        # If dictionary key index of the current number matches the current number
            # save the key-value pair as string into an array
        # Else
            # Loop through the keys array
                # Each phone number will have the closest cost and will be appended into the key-value string array
    # Return the key-value string array


print(phone_route_cost_check('text_files/route-costs-10.txt', 'text_files/phone-numbers-10.txt'))