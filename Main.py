from Parser import Parser
import argparse


def main():

    input_file = 'Add.asm'

    # initiate parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--data", help="print input data", action="store_true")
    arg_parser.add_argument("-c", "--clean", help="clear input data", action="store_true")
    arg_parser.add_argument("-n", "--normal", help="normalize input data", action="store_true")

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


if __name__ == "__main__":
    # execute only if run as a script
    main()
