from classes import NFA


class Automaton(NFA.Automaton):
    def __init__(self, file_name=""):
        super().__init__(file_name)
        self.__check_deterministic()

    def __check_deterministic(self):
        section = super()._section
        if "epsilon" in section["[Sigma]"]:
            raise Exception("Epsilon can't be in deterministic automata")

        states = super().get_section("[State]")
        for curr_state in states:
            if curr_state in super()._adjacent_states.keys():
                for letters in super()._adjacent_states[curr_state].keys():
                    if len(super()._adjacent_states[curr_state][letters]) > 1:
                        raise Exception("You can't use the same character to go from a state to more states")


