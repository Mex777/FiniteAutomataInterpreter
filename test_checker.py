import classes.NFA as NFA
import classes.DFA as DFA


def parse_file(file):
    return [line.replace("\n", "") for line in file.readlines() if line[0] != '#']


# test checker for the NFA automata
def check_nfa(test_counter):
    print("NFA:")
    for curr_test in range(test_counter):
        nfa_automaton = NFA.Automaton(f"./tests/NFA/inputs/input{curr_test}.txt")
        queries_file = open(f"./tests/NFA/queries/queries{curr_test}.txt")
        output_file = open(f"./tests/NFA/outputs/output{curr_test}.txt")

        queries = parse_file(queries_file)
        output = parse_file(output_file)
        #
        passed_test = True
        for query in range(0, len(queries)):
            if nfa_automaton.check_string(queries[query]) != bool(int(output[query])):
                passed_test = False
                problem = query

        if passed_test:
            print(f"\tTest {curr_test} passed")
        else:
            print(f"\tTest {curr_test} failed (Query {problem})")
        # print(f"Test {curr_test}: ")
        # for query in range(0, len(queries)):
        #     print(f"\t{queries[query]} -> {nfa_automaton.check_string(queries[query])} - {bool(int(output[query]))}")


# test checker for the DFA automata
def check_dfa(test_counter):
    print("DFA:")
    for curr_test in range(test_counter):
        dfa_automaton = DFA.Automaton(f"./tests/DFA/inputs/input{curr_test}.txt")
        queries_file = open(f"./tests/DFA/queries/queries{curr_test}.txt")
        output_file = open(f"./tests/DFA/outputs/output{curr_test}.txt")

        queries = parse_file(queries_file)
        output = parse_file(output_file)
        #
        passed_test = True
        for query in range(0, len(queries)):
            if dfa_automaton.check_string(queries[query]) != bool(int(output[query])):
                passed_test = False
                problem = query

        if passed_test:
            print(f"\tTest {curr_test} passed")
        else:
            print(f"\tTest {curr_test} failed (Query {problem})")


check_nfa(3)
check_dfa(1)
