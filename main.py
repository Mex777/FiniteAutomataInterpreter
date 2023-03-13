import classes.DFA as DFA
import classes.NFA as NFA
import networkx

def main():
    my_automata = NFA.Automaton("config.in")
    my_automata.check_string("010101")
    my_automata.draw_graph()


main()
