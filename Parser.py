import re


class Parser:

    def __init__(self, filename):
        """Initialize parser with path of file to parse."""
        self.file = filename

    def read_data(self):
        """Return data from input as list."""
        file_object = open(self.file, 'r')
        data_list = []
        for line in file_object:
            data_list.append(line)
        return data_list

    def clean_data(self):
        """Return list of data with whitespace and comments removed."""
        input_data = self.read_data()
        clean_data = []
        for line in input_data:
            if not re.match(r'[/\n]', line[0]):
                stripped_line = line.strip()
                clean_data.append(stripped_line.split(' ', 1)[0])
        return clean_data

    def normalize_data(self):
        """Return list of normalized data ready for assembly."""
        clean_data = self.clean_data()
        normalized_data = []
        for line in clean_data:
            if not re.match(r'[@|(]', line[0]):
                if "=" not in line:
                    line = "null=" + line
                if ";" not in line:
                    line = line + ";null"
            normalized_data.append(line)
        return normalized_data

    def print_data(self, flag):
        """Print parser data."""
        print_list = []
        if flag == "d":
            print_list = self.read_data()
        if flag == "c":
            print_list = self.clean_data()
        if flag == "n":
            print_list = self.normalize_data()
        for line in print_list:
            print(line)
