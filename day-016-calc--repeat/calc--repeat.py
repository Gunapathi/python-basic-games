def add(curr, value):
    return curr + value


def sub(curr, value):
    return curr - value


def mul(curr, value):
    return curr * value


def div(curr, value):
    return curr / value


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

num1 = int(input(f"What's the first number?:"))
num2 = int(input(f"What's the second number?:"))
print('+, -, *, /')
operator_symbol = input(f"Pick an operation:")
count_continue = True

answer = operations[operator_symbol](num1, num2)
print(f"{num1} {operator_symbol} {num2} = {answer}")


def start_operation(num_1, num_2, op_sym):
    operation_function = operations[op_sym]
    return operation_function(num_1, num_2)


while count_continue:
    user_input = input("Want to continue? y/n")
    if user_input == 'y':
        count_continue = True
        select_symbol = input(f"Pick an operation:")
        num3 = int(input(f"What's the next number?:"))
        prev_ans = answer
        answer = start_operation(answer, num3, select_symbol)
        print(f"{prev_ans} {select_symbol} {num3} = {answer}")
    elif user_input == 'n':
        count_continue = False
    else:
        print("Invalid input. Please enter 'y' or 'n'")
