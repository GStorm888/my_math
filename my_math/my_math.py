def min():
    first_num = input("input first number")
    second_num = input("input second number")

    if not first_num.isdigit() and not second_num.isdigit():
        return "please enter a number"
    
    if first_num < second_num:
        min = second_num
    elif first_num > second_num:
        min = first_num
    else:
        min = first_num
        