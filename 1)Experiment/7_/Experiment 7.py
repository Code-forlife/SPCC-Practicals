import prettytable as pt

class CodeGenerator:
    def __init__(self):
        self.registers = {f"R{i}": None for i in range(4)}  # Simulate 4 registers
        self.address_descriptors = {}  # Map variable names to address descriptors
        self.code = []  # List to store generated machine code instructions (simplified)

    def getreg(self, var_name):
    # Check if variable is already in a register
        if var_name in self.address_descriptors:
            descriptor = self.address_descriptors[var_name]
            if isinstance(descriptor["location"], str):  # Check if location is a register name
                # Free up the current register
                current_register = descriptor["location"]
                self.registers[current_register] = None
        # Find an empty register
        for reg in self.registers:
            if self.registers[reg] is None:
                self.registers[reg] = var_name
                return reg


    def generate_code(self, statement, is_last_statement=False):
        parts = statement.split()  # Split the statement into words
        if len(parts) < 3:
            raise ValueError(f"Invalid statement format: {statement}")
        operand, op, operand2 = parts[2:]  # Get first three words (assuming op is binary)
    
        result_reg = self.getreg(operand)
        var = parts[0]
        # Handle operand (assuming it's already in a register or memory)
        operand_descriptor = self.address_descriptors.get(operand)
        operand_loc = operand_descriptor["location"] if operand_descriptor else operand
    
        # Handle operand2 (assuming it's already in a register or memory)
        operand2_descriptor = self.address_descriptors.get(operand2)
        operand2_loc = operand2_descriptor["location"] if operand2_descriptor else operand2
    
        # Generate instructions (replace with actual machine code for specific architecture)
        if operand_loc != result_reg:
            self.code.append(f"MOV {operand_loc}, {result_reg}")  # Move operand if needed
        if op == "+":
            self.code.append(f"ADD {operand2_loc}, {result_reg}")
        elif op == "-":
            self.code.append(f"SUB {operand2_loc}, {result_reg}")
    
        # If it's the last statement, move the result from register to variable
        if is_last_statement:
            self.code.append(f"MOV {result_reg}, {var}")
    
        # Update address descriptors
        self.address_descriptors[var] = {"location": result_reg}

        # Return generated code and reset for the next statement
        generated_code = "\n".join(self.code)
        self.code = []  # Reset code for next statement
        return generated_code

# Initialize PrettyTable
table = pt.PrettyTable(["Statement", "Generated Code", "Register Descriptor", "Address Descriptor"])

codegen = CodeGenerator()
statements = ["t = a - b", "u = a - c","v = t + u","d = v + u"]

def find_next_use(x,index):
    if index+1 == len(statements) and x == letters[-1]:
        return True
    for s in statements[index+1::]:
        if x in s:
            return True
    return False
letters = [x[0] for x in statements ]
# Generate code and populate the table
for i, statement in enumerate(statements):
    generated_code = codegen.generate_code(statement, is_last_statement=(i == len(statements) - 1))
    address_descriptor = codegen.address_descriptors[statement.split()[0]]["location"]
    actual_adr = []
    for l in letters:
        if find_next_use(l,i):
            if l in codegen.address_descriptors:
                actual_adr.append((l,codegen.address_descriptors[l]["location"]))
    reg_desc = ''
    for a in actual_adr:
        reg_desc+=f'{a[1]} contains {a[0]}\n'
    adr_desc = ''
    for a in actual_adr:
        adr_desc+=f'{a[0]} in {a[1]}\n'
    if i+1 == len(statements):
        adr_desc+=f'{letters[-1]} in memory'
    result_reg = address_descriptor if address_descriptor is not None else "N/A"
    table.add_row([statement, generated_code, reg_desc, adr_desc])



print("Table:")
print(table)
