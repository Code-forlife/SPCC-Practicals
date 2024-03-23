from prettytable import PrettyTable

def is_op(char):
    return char in ["+", "-", "*", "/", "^", "="]

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
        elif is_op(char):
            op2 = stack.pop()
            op1 = stack.pop()
            temp_var = "T" + str(temp)
            temp += 1 
            quadruples.append([char, op1, op2, temp_var])
            stack.append(temp_var)
    return quadruples

def main():
    exp = input("Enter the postfix expression: ")
    
    quadruples = postfix_to_quadruple(exp)
    display_quadruple(quadruples)

if __name__ == "__main__":
    main()
