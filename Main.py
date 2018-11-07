from Parser import Parser
import argparse


def main():

    input_file = 'Add.asm'

    # initiate parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-r", "--run", help="run parser", action="store_true")

    # read arguments from the command line
    args = arg_parser.parse_args()

    # check for --run or -r
    if args.run:
        asm_parser = Parser(input_file)
        asm_parser.print_data()


if __name__ == "__main__":
    # execute only if run as a script
    main()
