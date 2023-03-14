import classes.NFA as NFA
import classes.DFA as DFA
import classes.visualizer as GUI

def main():
    my_automata = NFA.Automaton("config.in")
    my_automata.check_string("011")
    # my_automata.draw_graph()

    my_gui = GUI.Visualizer(my_automata)
    my_gui.draw_graph()

main()
