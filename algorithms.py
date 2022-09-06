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
    for i in range(len(list_of_names)):
        for j in range(len(list_of_names)):
            if i == j:
                break
            if list_of_names[i] == list_of_names[j]:
                return True
    return False

print(repeated_names(['jamie','lanny','evan','jj','nevin','evan']))
print(repeated_names(['jamie','lanny','evan','jj','nevin']))
