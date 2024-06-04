def min():
    first_num = input("input first number")
    second_num = input("input second number")

    if not first_num.isdigit() and not second_num.isdigit():
        return "please enter a number"
    
    if first_num < second_num:
        min = first_num
    elif first_num > second_num:
        min = second_num
    else:
        min = first_num

def average():
    first_num = input("input first number")
    second_num = input("input second number")

    if not first_num.isdigit() and not second_num.isdigit():
        return "please enter a number"
    
    if first_num < second_num:
        average = second_num - first_num
    elif first_num > second_num:
        average =  first_num - second_num
    else:
        average = 0