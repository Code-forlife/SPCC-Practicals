from prettytable import PrettyTable

def is_operator(char):
    return char in ['+', '-', '*', '/', '^', '=']

def precedence(op):
    precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence_dict.get(op, 0)

def infix_to_postfix(infix_exp):
    postfix_exp = []
    stack = []
    for char in infix_exp:
        if char.isalnum():  # Operand
            postfix_exp.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_exp.append(stack.pop())
            stack.pop()  # Discard '('
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix_exp.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix_exp.append(stack.pop())
    
    return ''.join(postfix_exp)

def display_quadruple(quadruples):
    table = PrettyTable()
    table.field_names = ["Operator", "Arg1", "Arg2", "Result"]
    for quadruple in quadruples:
        table.add_row(quadruple)
    print("Quadruple Representation:")
    print(table)

def postfix_to_quadruple(exp):
    stack = []
    quadruples = []
    temp = 1
    for char in exp:
        if char.isalnum():
            stack.append(char)
        elif is_operator(char):
            op2 = stack.pop()
            op1 = stack.pop()
            temp_var = "T" + str(temp)
            temp += 1 
            quadruples.append([char, op1, op2, temp_var])
            stack.append(temp_var)
    return quadruples

def main():
    infix_exp = input("Enter the infix expression: ")
    postfix_exp = infix_to_postfix(infix_exp)
    print("Postfix Expression:", postfix_exp)
    
    quadruples = postfix_to_quadruple(postfix_exp)
    display_quadruple(quadruples)

if __name__ == "__main__":
    main()
