from solver.problem_solver import read_and_preprocess_csv
from solver.graph_builder import build_graph, expand_graph
import networkx as nx

def main():


    mini_schedule_file = "data/mini-schedule.csv"

    mini_schedule_df = read_and_preprocess_csv(mini_schedule_file)
    mini_graph = build_graph(mini_schedule_df)
    expanded_mini_graph = expand_graph(mini_graph)
    
    nx.write_gexf(mini_graph, "gephi-graphs/mini-graph.gexf")
    nx.write_gexf(expanded_mini_graph, "gephi-graphs/expanded-mini-graph.gexf")
    

if __name__ == "__main__":
    main()