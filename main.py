import classes.NFA as NFA
import classes.DFA as DFA
import classes.visualizer as gui


def main():
    my_automata = NFA.Automaton("./tests/NFA/inputs/input1.txt")

    print(my_automata.check_string("0000"))
    # my_gui = gui.Visualizer(my_automata)
    # my_gui.draw_graph()


main()
