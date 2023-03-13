import classes.DFA as DFA


def main():
    my_automata = DFA.Automaton("config.in")
    my_automata.check_string("/*ab**/")


main()




