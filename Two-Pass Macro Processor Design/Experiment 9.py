from prettytable import PrettyTable
class DefinitionTable:
    def __init__(self):
        self.index = None
        self.definition = None
        self.arg = [None, None]
        self.next = None

class ArgumentListArray:
    def __init__(self):
        self.index = None
        self.arg = None
        self.next = None

class NameTable:
    def __init__(self):
        self.index = None
        self.name = None
        self.dt_index = None
        self.next = None

def find_arg_index(arg, al_head):
    temp = al_head
    while temp is not None:
        if temp.arg == arg:
            return temp
        temp = temp.next
    return None

def find_name(name, nt_head):
    temp = nt_head
    while temp is not None:
        if temp.name == name:
            return temp.dt_index
        temp = temp.next
    return None

def pass1(fp):
    global MDTC, MNTC
    MDTC = MNTC = 1
    dt_head = None
    nt_head = None
    al_head = None
    al_index = 1

    while True:
        line = fp.readline()
        if not line:
            break

        if "MACRO" in line:
            tokens = line.split()
            print(f"\nMACRO {tokens[0]} Detected...\n")

            if nt_head is None:
                nt_head = NameTable()
                nt_temp = nt_head
            else:
                nt_temp.next = NameTable()
                nt_temp = nt_temp.next

            nt_temp.index = MNTC
            MNTC += 1
            nt_temp.name = tokens[0]
            print(f"\n{tokens[0]} added into Name Table")

            for token in tokens[1:]:
                if token != "MACRO" and token != "\n":
                    if al_head is None:
                        al_head = ArgumentListArray()
                        al_temp = al_head
                    else:
                        al_temp.next = ArgumentListArray()
                        al_temp = al_temp.next

                    al_temp.index = al_index
                    al_index += 1
                    al_temp.arg = token
                    print(f"\nArgument {al_temp.arg} added into argument list array")

            if dt_head is None:
                dt_head = DefinitionTable()
                dt_temp = dt_head
            else:
                dt_temp.next = DefinitionTable()
                dt_temp = dt_temp.next

            dt_temp.definition = nt_temp.name
            print(f"\nDefinition table entry created for {nt_temp.name}")
            nt_temp.dt_index = dt_temp

            while True:
                line = fp.readline()
                if line.strip() == "MEND":
                    break

                tokens = line.split()
                is_arg = 0
                index = 0

                for token in tokens:
                    if is_arg == 0:
                        if dt_head is None:
                            dt_head = DefinitionTable()
                            dt_temp = dt_head
                        else:
                            dt_temp.next = DefinitionTable()
                            dt_temp = dt_temp.next

                        dt_temp.index = MDTC
                        MDTC += 1
                        dt_temp.definition = token
                        print(f"\nEntry appended for {dt_temp.definition} at index {dt_temp.index}")
                        is_arg = 1
                    else:
                        if find_arg_index(token, al_head) is None:
                            if al_head is None:
                                al_head = ArgumentListArray()
                                al_temp = al_head
                            else:
                                al_temp.next = ArgumentListArray()
                                al_temp = al_temp.next

                            al_temp.index = al_index
                            al_index += 1
                            al_temp.arg = token
                            dt_temp.arg[index] = al_temp
                        else:
                            dt_temp.arg[index] = find_arg_index(token, al_head)
                        index += 1

        # print("\nAll three tables are updated. Pass 1 Complete!\n")
    # Assuming nt_head, dt_head, and al_head are initialized in the main function
    print_name_table(nt_head)
    print_definition_table(dt_head)
    print_argument_list_array(al_head)

def pass2(fp):
    line = fp.readline()
    while line:
        print(line)
        temp = find_name(line, nt_head)
        if temp is not None:
            while temp.definition != "MEND":
                print("-", temp.definition, temp.arg[0], temp.arg[1])
                temp = temp.next
        line = fp.readline()

    print("\nOutput file updated with expanded code. Pass 2 Complete!\n")



def print_name_table(nt_head):
    table = PrettyTable(["Index", "Name", "Definition Table Index"])
    temp = nt_head
    while temp:
        table.add_row([temp.index, temp.name, temp.dt_index.index])
        temp = temp.next
    print("Name Table:")
    print(table)

def print_definition_table(dt_head):
    table = PrettyTable(["Index", "Definition", "Arguments", "Next"])
    temp = dt_head
    while temp:
        arg_list = [arg.arg for arg in temp.arg if arg]
        table.add_row([temp.index, temp.definition, arg_list, temp.next])
        temp = temp.next
    print("\nDefinition Table:")
    print(table)

def print_argument_list_array(al_head):
    table = PrettyTable(["Index", "Argument", "Next"])
    temp = al_head
    while temp:
        table.add_row([temp.index, temp.arg, temp.next])
        temp = temp.next
    print("\nArgument List Array:")
    print(table)


def main():
    global nt_head, al_head
    nt_head = None
    al_head = None

    try:
        with open("input.asm", "r") as fp:
            print("\nPass 1 in progress\n")
            pass1(fp)

        with open("input.asm", "r") as fp:
            print("\nPass 2 in progress\n")
            pass2(fp)
            

    except IOError:
        print("\nFailed to open the assembly file!")


if __name__ == "__main__":
    main()
