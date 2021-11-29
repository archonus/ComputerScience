from collections import deque
from typing import Callable

arithmetic_mapping = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}


def evaluate_rpn(input_expression: str, operator_mapping: dict[str, Callable]) -> int:
    """Evaluate a Reverse Polish Notation expression using the defined operators"""
    data_stack = deque()  # Double ended queue, implemented as a linked list
    # The list of values from the input, separated by spaces
    values = input_expression.split()
    n = len(values)
    if values[n-1] not in operator_mapping:
        raise ValueError("The expression must end with an operator")

    for value in values:
        if value in operator_mapping:
            operator = operator_mapping[value]
            operand2 = data_stack.pop()  # The operands will be popped in reverse order
            operand1 = data_stack.pop()
            result = operator(operand1, operand2)
            data_stack.append(result)
        else:
            num = int(value)
            data_stack.append(num)
    return data_stack.pop()


def main():
    input_expression = input(
        "Enter a Reverse Polish Notation expression to evaluate...")
    try:
        result = evaluate_rpn(input_expression, arithmetic_mapping)
        print(f"The result is {result}")
    except:
        print("The input is invalid. Cannot evaluate")


if __name__ == "__main__":
    main()
