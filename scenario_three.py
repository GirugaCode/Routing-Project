"""
Scenario 3: Multiple long carrier route lists

You have 5 carrier route lists, each with 10,000,000 (10M) entries (in arbitrary order) and
a list of 10,000 phone numbers. How can you speed up your route cost lookup solution to handle this larger dataset?

"""
def file_to_array_of_tuple():
    """
    Converting the five text files into an list of tuples.

    Runtime: O(n) where n is all the route-costs 
    """
    file_name_1 = open('text_files/route-costs-10.txt')
    file_name_2 = open('text_files/route-costs-100.txt')
    file_name_3 = open('text_files/route-costs-35000.txt')
    file_name_4 = open('text_files/route-costs-10000000.txt')
    file_name_5 = open('text_files/route-costs-600.txt')
    all_files = [file_name_1,file_name_2,file_name_3, file_name_4, file_name_5]
    all_array_tuples = []
    for file in all_files:
        array_of_numbers_and_cost = []
        for routes in file:
            tuple_to_array = routes.strip().split(',')  #['+69696969', '0.5']
            phone_number = tuple_to_array[0]
            cost = tuple_to_array[1]
            array_of_numbers_and_cost.append((int(phone_number), cost))
        file.close()
        array_of_numbers_and_cost.sort()
        all_array_tuples += array_of_numbers_and_cost
    return list(set(all_array_tuples))

def turn_to_numbers(filename):
    """
    Takes in the phone numbers text file and appends them into a list

    Runtime: O(n) where n is the amount of phone numbers
    """
    numbers_list = []
    number_file = open(filename)
    for number in number_file:
        number = number.strip()
        numbers_list.append(int(number))
    number_file.close()
    return numbers_list

def binary_search_recursive(array, item, left=None, right=None):
    """
    Conducts a binary search through the list of tuples.
    Uses the phone number and compares it to the list of tuples prefixs 

    Runtime: O(log(n)) where n is the value we are looking for in the search
    """
    if right == None:
        left = 0
        right = len(array) - 1
    elif left > right:
        return None
    middleIndex = (left + right) // 2
    middleVal = array[middleIndex][0]       # First item in the routing number
    if middleVal == item:
        return array[middleIndex][1]        # Returns the match routing prefix
    if middleVal < item:                    # Searches the left side of the list
        left = middleIndex + 1
    elif middleVal > item:                  # Searches the left side of the list
        right = middleIndex - 1

    return binary_search_recursive(array, item, left, right)

def get_number_price():
    """
    Credit: Shout out to Sarin Swift and Stephan Ouyang for their code for Scenario three. 
    Guided us on using binary search through a list of tuples.
    We optimized the program by putting the list of tuples into a set.
    O(n^2)
    Best Case Scenario: 52.0 (seconds) O(n^2) Where we iterate through the entire list of routing 
    numbers while always checking if it is not empty.
    """
    array_tuples = file_to_array_of_tuple()
    list_numbers = turn_to_numbers('text_files/phone-numbers-10000.txt')

    final_array = []

    for num in list_numbers:
        curr_number = num
        while str(curr_number) != '':
            searched_num = binary_search_recursive(array_tuples, curr_number)
            if searched_num == None:
                cut_int = str(curr_number)[:-1]
                if cut_int == '':
                    final_array.append([('+'+str(num)), 0])
                    break
                curr_number = int(cut_int)
            else:
                final_array.append([('+'+str(num)), searched_num])
                break

    return final_array

get_number_price()

