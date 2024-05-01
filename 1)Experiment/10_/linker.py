import os
from prettytable import PrettyTable

class Variable:
    def __init__(self, name, type, size, address):
        self.name = name
        self.type = type
        self.size = size
        self.address = address

class SymbolTable:
    def __init__(self):
        self.variables = []

def read_file_size_and_content(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        size = os.path.getsize(filename)
    return size, content.decode('utf-8')

def parse_variables(content, symbol_table, start_address):
    lines = content.split('\n')
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            type, name = parts[:2]
            size = None
            if type == "int":
                size = 4
            elif type == "char":
                size = 1
            elif type == "float":
                size = 4
            elif type == "double":
                size = 8
            if size is not None:
                symbol_table.variables.append(Variable(name, type, size, start_address))
                start_address += size

def parse_ext_variables(content, symbol_table):
    lines = content.split('\n')
    for line in lines:
        parts = line.split()
        if len(parts) >= 3 and parts[0] == "extern":
            symbol_table.variables.append(Variable(parts[2], parts[1], 0, -1))

def print_symbol_table(symbol_table):
    table = PrettyTable(["Variable", "Type", "Size", "Address"])
    for variable in symbol_table.variables:
        table.add_row([variable.name, variable.type, variable.size, variable.address])
    print(table)

def print_symbol_tablet(symbol_table):
    table = PrettyTable(["Variable", "Type"])
    for variable in symbol_table.variables:
        table.add_row([variable.name, variable.type])
    print(table)

def print_symbol_tables(symbol_table1, symbol_table2):
    table = PrettyTable(["Variable", "Type", "Size", "Address"])
    for variable in symbol_table1.variables:
        table.add_row([variable.name, variable.type, variable.size, variable.address])
    for variable in symbol_table2.variables:
        table.add_row([variable.name, variable.type, variable.size, variable.address])
    print(table)

def main():
    memory_size = int(input("Enter the size of memory: "))
    
    size_a, content_a = read_file_size_and_content("a.c")
    size_b, content_b = read_file_size_and_content("b.c")

    total_size = size_a + size_b

    if total_size > memory_size:
        print("Insufficient memory.")
        return

    symbol_table_a = SymbolTable()
    symbol_table_b = SymbolTable()
    symbol_table_c = SymbolTable()
    symbol_table_d = SymbolTable()

    parse_variables(content_a, symbol_table_a, 1000)
    parse_variables(content_b, symbol_table_b, 5000)

    parse_ext_variables(content_a, symbol_table_c)
    parse_ext_variables(content_b, symbol_table_d)

    print("Symbol Table for a.c")
    print_symbol_table(symbol_table_a)

    print("Symbol Table for extern a.c")
    print_symbol_tablet(symbol_table_c)

    print("Symbol Table for b.c")
    print_symbol_table(symbol_table_b)

    print("Symbol Table for extern b.c")
    print_symbol_tablet(symbol_table_d)

    print("Global variable Table")
    print_symbol_tables(symbol_table_a, symbol_table_b)

if __name__ == "__main__":
    main()
