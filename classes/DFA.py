from classes import NFA


class Automaton(NFA.Automaton):
    def __init__(self, file_name=""):
        super().__init__(file_name)
        self.__check_deterministic()

    def __check_deterministic(self):
        sigma = super().get_section("[Sigma]")
        if "epsilon" in sigma:
            raise Exception("Epsilon can't be in deterministic automata")

        states = super().get_section("[State]")
        adjacent_states = super().get_adjacency_list()
        for curr_state in states:
            if curr_state in adjacent_states.keys():
                for letters in adjacent_states[curr_state].keys():
                    if len(adjacent_states[curr_state][letters]) > 1:
                        raise Exception("You can't use the same character to go from a state to more states")

        delta = super().get_section("[Delta]")
        for line in delta:
            tokens = line.split(", ")
            symbol = tokens[1]

            if symbol == "epsilon":
                raise Exception("Epsilon can't be in deterministic automata")
