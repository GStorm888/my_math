def is_digit(first_num, second_num):
    if first_num.isdigit() and second_num.isdigit():
        return False
    else:
        return  True

def min_func():
    first_num = input("input first number >>>")
    second_num = input("input second number >>>")

    if is_digit(first_num, second_num):
        return "please enter a number"
    
    if first_num < second_num:
        min = first_num
    elif first_num > second_num:
        min = second_num
    else:
        min = first_num
    return min

def max_func():
    first_num = input("input first number >>>")
    second_num = input("input second number >>>")

    if is_digit(first_num, second_num):
        return "please enter a number"
    
    if first_num < second_num:
        max = second_num
    elif first_num > second_num:
        max = first_num
    else:
        max = first_num
    return max

def average():
    first_num = input("input first number")
    second_num = input("input second number")

    if is_digit(first_num, second_num):
        return "please enter a number"
    
    if first_num < second_num:
        average = second_num - first_num
    elif first_num > second_num:
        average =  first_num - second_num
    else:
        average = 0

    return average
