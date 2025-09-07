from stack import Stack


def is_balanced(input_str):
    stack_left = Stack()
    for i in input_str:
        if i == "(":
            stack_left.push("(")
        elif i == ")":
            if stack_left.size() != 0:
                stack_left.pop()
            else:
                return False
    if stack_left.size() == 0:
        return True
    return False
        
