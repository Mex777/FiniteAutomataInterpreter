class Automata:
    section = {}
    end_state = []
    file = []
    start_state = -1
    adjacency_list = {}

    def load_sections(self):
        curr_key = ""
        for line in self.file:
            if line[0] == '[':
                curr_key = line
            else:
                if curr_key not in self.section.keys():
                    self.section[curr_key] = set()

                if curr_key != "[State]":
                    self.section[curr_key].add(line)
                else:
                    tokens = line.split(', ')
                    tokens = [token.replace("\n", "") for token in tokens]
                    self.section[curr_key].add(tokens[0])
                    for state_type in range(1, len(tokens)):
                        if tokens[state_type] == "0":
                            if self.start_state != -1:
                                raise Exception("There is already a start state")
                            else:
                                self.start_state = tokens[0]
                        if tokens[state_type] == "2":
                            self.end_state.append(tokens[0])

        self.__validate_delta()

    def __validate_states(self):
        pass

    def __validate_delta(self):
        for steps in self.section["[Delta]"]:
            tokens = steps.split(', ')
            tokens = [token.replace("\n", "") for token in tokens]
            if tokens[0] not in self.section["[State]"]:
                raise Exception(f"{tokens[0]} not in States")
            if tokens[2] not in self.section["[State]"]:
                raise Exception(f"{tokens[2]} not in States")
            if tokens[1] not in self.section["[Sigma]"]:
                raise Exception(f"{tokens[1]} not in Sigma")

            if tokens[0] not in self.adjacency_list.keys():
                self.adjacency_list[tokens[0]] = {}

            if tokens[1] not in self.adjacency_list[tokens[0]].keys():
                self.adjacency_list[tokens[0]][tokens[1]] = []

            self.adjacency_list[tokens[0]][tokens[1]].append(tokens[2])

        print(self.adjacency_list)

    def parse_file(self, file_name):
        file = open(file_name, "r")
        file = file.readlines()
        # self.file = [line.replace("\n", "") for line in file if line[0] != '#']
        for line in file:
            line = line.replace("\n", "")
            line.strip()
            if line != "" and line[0] != '#':
                self.file.append(line)

    def print_sections(self):
        print(self.section)
        print(f"Start state: {self.start_state}\nEnd state: {self.end_state}")

    def get_section(self, section_name):
        if section_name in self.section.keys():
            return self.section[section_name]
        else:
            raise Exception(f"There is no {section_name}")

    def __exists_path(self, input_string, curr_letter_index, curr_state):
        if curr_letter_index == len(input_string) - 1:
            # checking whether the string ended in an ending state
            return curr_state in self.end_state

        next_letter = input_string[curr_letter_index + 1]
        is_path = False

        if curr_state not in self.adjacency_list.keys():
            return False
        if next_letter not in self.adjacency_list[curr_state].keys():
            return False

        for next_state in self.adjacency_list[curr_state][next_letter]:
            is_path |= self.__exists_path(input_string, curr_letter_index + 1, next_state)

        return is_path

    def check_string(self, input_string):
        path = self.__exists_path(input_string, -1, self.start_state)

        for curr_char in input_string:
            if curr_char not in self.section["[Sigma]"]:
                raise Exception(f"Invalid string\n{curr_char} -> not in Sigma")

        if path is True:
            print(f"The string {input_string} is accepted\n")
        else:
            print(f"The string {input_string} is not accepted\n")
        return path


def main():
    my_automata = Automata()

    my_automata.parse_file("config.in")
    my_automata.load_sections()
    my_automata.print_sections()

    my_automata.check_string("/**/")
    # print(my_automata.get_section("[Sigma]"))


main()


# ce se intampal daca dam un state inexistent in delta


