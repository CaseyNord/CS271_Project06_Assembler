# Program specifications:
# input files are .asm (assembly files)
# output files are .hack (binary files)
#
# the filename should be supplied as a command line argument (maybe also a .bat file
#       like my work program?)
#
# the four modules (files) that should make up the program are...
#       Parser.py - parses input
#       Code.py - provides binary codes of all assembly mnemonics
#       SymbolTable.py - handles symbols
#       Main.py - driver
#
# each line of binary code is a sequence of 16 "0" and "1" ASCII characters
# "//" are comments and should be omitted (via regular expressions maybe?)
# if the instruction is of format @value it is an A-instruction starting with 0
# if the instruction is of format dest=comp;jump it is a C-instruction starting with 1


class Parser:

    def __init__(self, filename):
        self.file = filename

    def read_data(self):
        file_object = open(self.file, 'r')
        data_list = []
        for line in file_object:
            data_list.append(line)
        return data_list

    def is_a_instruction(self, line):
        if "@" in line:
            return True
        else:
            return False

    def print_data(self):
        data_list = self.read_data()
        for line in data_list:
            print(line, end='')
