class Assembler:

    def __init__(self):
        self.memory_index = 16  # first register for non-reserved memory

    def allocate_memory(self):
        # increase the memory index when necessary
        return

    def build_symbol_table(self):
        # run through list and
        # create table of each
        # symbol encountered
        return

    def assemble_c_instruction(self):
        return

    def assemble_a_instruction(self):
        return

    def assemble_line(self):
        return

    def assemble(self):
        # grab normalized list
        # for each item in list
        # if A translate A
        # if C translate C
        return

    def write_to_file(self):
        return

    def print_data(self, flag):
        """prints assembler data"""
        print_list = []
        if flag == "a":
            print_list = self.read_data()
        for line in print_list:
            print(line)


# - OLD METHODS ###

    def is_a_instruction(self, line):
        # is A instruction
        if "@" in line:
            return True
        # is C or L instruction
        else:
            return False

    def is_c_or_l_instruction(self, line):
        # is L instruction
        if "(" in line:
            return False
        # is C instruction
        else:
            return True

    def return_binary_value(self, number):
        return str("{0:b}".format(number))

    def parse_input(self):
        output = ""
        data_list = "@2"
        #data_list = self.read_data()
        if self.is_a_instruction(data_list):
            output += "0"
            output += "0" * (15 - len(self.return_binary_value(2)))
            output += self.return_binary_value(2)
        return output
