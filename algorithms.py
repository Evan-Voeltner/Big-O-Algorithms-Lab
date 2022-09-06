def even_or_odd(given_int):
    """
    The given code will always run once making it a constant O(1)
    No matter the size of the number, the amount of steps remain the same
    """
    if given_int % 2 == 0:
        return True
    else:
        return False

print(even_or_odd(2))
print(even_or_odd(5))

def less_than_one_hundred(given_list):
    """
    The given code will run more depending on the size of the input making it linear O(n)
    Depending on the size of the list, the for loop will iterate more times
    """
    for num in given_list:
        if num > 100:
            return False
    return True

print(less_than_one_hundred([2,53,15,84,84,17]))
print(less_than_one_hundred([2,53,15,84,84,1327]))

def repeated_names(list_of_names):
    """
     The given code will run more depending on the size of the input making it Quadratic O(n^2)
     The bigger the list_of_names get, the more it will have to check a single element to EVERY OTHER ELEMENT
    """
    # for i in range(len(list_of_names)):
    #     for j in range(len(list_of_names)):
    #         if i == j:
    #             break
    #         if list_of_names[i] == list_of_names[j]:
    #             return True
    # return False
    """
     The given code will run more depending on the size of the input making it linear O(n)
     The bigger the list_of_names get, the more it will have to compare an element to every remaining element that hasn't been checked
    """
    while len(list_of_names) != 0:
        for index in range(len(list_of_names)):
            if index == 0:
                continue
            if list_of_names[0] == list_of_names[index]:
                return True
            
        list_of_names.pop(0)
    return False

print('Task 3')
print(repeated_names(['jamie','lanny','evan','jj','nevin','evan']))
print(repeated_names(['jamie','lanny','evan','jj','nevin']))

def sort_list(unsorted_list):
    """
    The given code will run more depending on the size of the input making it Quadratic O(n^2)
    The bigger the unsorted_list gets, the more times the for loop will have to check each number with the number next to it
    """
    
    list_unchanged = False
    while list_unchanged == False:
        
        list_unchanged = True
        for current_index in range(len(unsorted_list)-1):
            
            next_index = current_index + 1
            if unsorted_list[current_index] > unsorted_list[next_index]:
                changed_number = unsorted_list.pop(next_index)
                unsorted_list.insert(current_index, changed_number)
                list_unchanged = False


       
    return unsorted_list

print(sort_list([4,6,9,1,2,5,6]))
print(sort_list([4,6,9,1,2,5,6,5,5,5,123,44,40]))
print(sort_list([8,7,6,5,4,3,2,1]))

