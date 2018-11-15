import argparse
from pathlib import Path

from Parser import Parser
from Assembler import Assembler


def main():

    input_file = 'Add.asm'

    # initiate parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--data", help="print sample data", action="store_true")
    arg_parser.add_argument("-c", "--clean", help="clear sample data", action="store_true")
    arg_parser.add_argument("-n", "--normal", help="normalize sample data", action="store_true")
    arg_parser.add_argument("-a", "--assemble", help="assemble sample data", action="store_true")
    arg_parser.add_argument("-f", "--file", help="assemble from file", type=str, required=False)
    arg_parser.add_argument("-b", "--write_bat_file", help="write drag and drop .bat", action="store_true")

    # read arguments from the command line
    args = arg_parser.parse_args()

    # check for --data or -d
    if args.data:
        asm_parser = Parser(input_file)
        asm_parser.print_data("d")

    # check for --clean or -c
    if args.clean:
        asm_parser = Parser(input_file)
        asm_parser.print_data("c")

    # check for --normal or -n
    if args.normal:
        asm_parser = Parser(input_file)
        asm_parser.print_data("n")

    # check for --assemble or -a
    if args.assemble:
        asm_parser = Parser(input_file)
        assembler = Assembler()
        assembler.print_assembler_data("a", asm_parser.normalize_data())

    # check for --file or -f
    if args.file:
        asm_parser = Parser(args.file)
        assembler = Assembler()
        assembler.write_to_file(args.file, asm_parser.normalize_data())
        return

    # check for --write_bat_file or -k
    if args.write_bat_file:
        if Path("Assembler.bat").is_file():
            print("File already exists")
            input()
        else:
            file_object = open("Assembler.bat", "w")
            file_object.write("python \"%~dp0/Main.py\" -f %1\n\nrem cmd /k")


if __name__ == "__main__":
    # execute only if run as a script
    main()
