import networkx
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, automaton):
        self.__graph = networkx.MultiDiGraph()
        self.__states = automaton.get_section("[State]")
        self.__end_states = automaton.get_end_states()
        self.__adjacency_list = automaton._adjacent_states
        self.__start_state = automaton.get_start_state()
        self.__construct_graph()

    # adds the nodes(states) and the edges to the networkX graph
    def __construct_graph(self):
        edge_label = {}
        for curr_state in self.__states:
            self.__graph.add_node(curr_state)

            # checking whether the current state is origin for some adjacent states
            if curr_state in self.__adjacency_list.keys():
                edge_label[curr_state] = {}

                # creating the edge labels for every 2 adjacent nodes(states)
                for edge in self.__adjacency_list[curr_state]:
                    for next_state in self.__adjacency_list[curr_state][edge]:
                        if next_state not in edge_label[curr_state].keys():
                            edge_label[curr_state][next_state] = edge
                        else:
                            edge_label[curr_state][next_state] += ", " + edge

        # adding the edges with their corresponding
        for curr_state in edge_label.keys():
            for next_state in edge_label[curr_state].keys():
                self.__graph.add_edge(curr_state, next_state, label=edge_label[curr_state][next_state])

    # returns an array of containing the colors of the nodes
    def __color_nodes(self):
        node_colors = {}
        for curr_state in self.__states:
            if curr_state in self.__end_states:
                node_colors[curr_state] = "#6d958a"
            else:
                node_colors[curr_state] = "#9CD5C6"

        return [node_colors[node] for node in self.__graph.nodes()]

    def draw_graph(self):
        node_colors = self.__color_nodes()
        edge_labels = {(u, v): d['label'] for u, v, d in self.__graph.edges(data=True)}

        # creating an invisible node which points to the starting node
        # so there will be an edge named start, pointing to the start node
        invisible_node = ""
        self.__graph.add_node(invisible_node)
        self.__graph.add_edge(invisible_node, self.__start_state, label="Start")
        edge_labels[(invisible_node, self.__start_state)] = "Start"
        node_colors.append("none")

        pos = networkx.planar_layout(self.__graph, scale=1.0)

        # drawing the nodes with their labels
        networkx.draw_networkx_nodes(self.__graph, pos, node_color=node_colors, node_size=800, label=True)
        networkx.draw_networkx_labels(self.__graph, pos)

        # drawing the edges with their labels
        networkx.draw_networkx_edges(self.__graph, pos, width=2.0, connectionstyle='arc3, rad = 0', arrowsize=20)
        networkx.draw_networkx_edge_labels(self.__graph, pos, edge_labels=edge_labels, font_color='black', font_size=11, label_pos=0.3)

        plt.margins(0.1)
        plt.show()

        # removing the invisible node from the graph
        self.__graph.remove_edge(invisible_node, self.__start_state)
        self.__graph.remove_node(invisible_node)
