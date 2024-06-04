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
        min = second_num
    elif first_num > second_num:
        min = first_num
    else:
        min = first_num
    return min
