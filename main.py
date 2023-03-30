import sys

import classes.NFA as NFA
import classes.DFA as DFA
import classes.visualizer as gui
import time
import random

def gen_string(length):
    strin = ""
    for i in range(length):
        strin += str(random.randint(0, 1))


    return strin




def main():
    sys.setrecursionlimit(50000)
    input_string = gen_string(14000)
    my_automata = NFA.Automaton("config.in")
    start = time.time()
    print(my_automata.check_string(input_string))
    end = time.time()
    print(end - start)


main()
