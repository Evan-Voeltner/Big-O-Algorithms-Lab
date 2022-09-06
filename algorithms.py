def even_or_odd(given_int):
    """
    The given code will always run once making it a constant
    No matter the size of the number, the amount of steps remain the same
    """
    if given_int % 2 == 0:
        return True
    else:
        return False

print(even_or_odd(2))
print(even_or_odd(5))