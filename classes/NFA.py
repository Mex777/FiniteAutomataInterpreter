import networkx
import matplotlib.pyplot as plt


class Automaton:
    _section = {}
    __end_state = []
    __file = []
    __start_state = -1
    _adjacent_states = {}

    def __init__(self, file_name=""):
        if file_name != "":
            self.parse_file(file_name)

    def parse_file(self, file_name):
        file = open(file_name, "r")
        file = file.readlines()
        for line in file:
            line = line.replace("\n", "")
            line.strip()
            if line != "" and line[0] != '#':
                self.__file.append(line)

        self._load_sections()

    # goes through the parsed file and adds each section into the section dictionary
    def _load_sections(self):
        curr_section = ""
        for line in self.__file:
            if line[0] == '[':
                curr_section = line
            else:
                if curr_section not in self._section.keys():
                    self._section[curr_section] = set()
                self._section[curr_section].add(line)

        self._validate_states()
        self._validate_delta()

    def _validate_states(self):
        states = self.get_section("[State]")
        new_states_section = set()
        for line in states:
            tokens = line.split(', ')
            tokens = [token.replace("\n", "") for token in tokens]
            new_states_section.add(tokens[0])
            for state_type in range(1, len(tokens)):
                if tokens[state_type] == "0":
                    if self.__start_state != -1:
                        raise Exception("There is already a start state")
                    else:
                        self.__start_state = tokens[0]
                if tokens[state_type] == "2":
                    self.__end_state.append(tokens[0])

        self._section["[State]"] = new_states_section

    # checks the delta function from the file
    # creates the graph of the Automata
    def _validate_delta(self):
        for steps in self._section["[Delta]"]:
            tokens = steps.split(', ')
            tokens = [token.replace("\n", "") for token in tokens]

            origin_state = tokens[0]
            edge_letter = tokens[1]
            destination_state = tokens[2]
            if origin_state not in self._section["[State]"]:
                raise Exception(f"{origin_state} not in States")
            if destination_state not in self._section["[State]"]:
                raise Exception(f"{destination_state} not in States")
            if edge_letter not in self._section["[Sigma]"]:
                raise Exception(f"{edge_letter} not in Sigma")

            if origin_state not in self._adjacent_states.keys():
                self._adjacent_states[origin_state] = {}

            if edge_letter not in self._adjacent_states[origin_state].keys():
                self._adjacent_states[origin_state][edge_letter] = []

            self._adjacent_states[origin_state][edge_letter].append(destination_state)

    def print_sections(self):
        print(self._section)
        print(f"Start state: {self.__start_state}\nEnd state: {self.__end_state}")

    def get_section(self, section_name):
        if section_name in self._section.keys():
            return self._section[section_name]
        else:
            raise Exception(f"There is no {section_name}")

    def get_end_states(self):
        return self.__end_state

    def get_start_state(self):
        return self.__start_state

    # checks if there's a path in the automata that accepts the input_string
    def __exists_path(self, input_string, curr_letter_index, curr_state):
        if curr_letter_index == len(input_string) - 1:
            # checking whether the string ended in an ending state
            return curr_state in self.__end_state

        next_letter = input_string[curr_letter_index + 1]
        is_path = False

        if curr_state not in self._adjacent_states.keys():
            return False
        if next_letter not in self._adjacent_states[curr_state].keys():
            return False

        for next_state in self._adjacent_states[curr_state][next_letter]:
            is_path |= self.__exists_path(input_string, curr_letter_index + 1, next_state)

        return is_path

    # checks the validity of the string and verifies whether the string is accepted by the automata
    # returns True if the string is accepted and False otherwise
    def check_string(self, input_string):
        path = self.__exists_path(input_string, -1, self.__start_state)
        alphabet = self.get_section("[Sigma]")
        for curr_char in input_string:
            if curr_char not in alphabet:
                raise Exception(f"Invalid string\n{curr_char} -> not in Sigma")

        if path is True:
            print(f"The string {input_string} is accepted\n")
        else:
            print(f"The string {input_string} is not accepted\n")
        return path
