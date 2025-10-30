from solver.problem_solver import load_problems_csv, read_and_preprocess_csv, create_solutions_csv, construct_connection
from solver.costFunctions import solve_cost_function, dijkstra_path_expanded_graph
from solver.graph_builder import build_graph, expand_graph
import networkx as nx
import pickle

def main():

    problems_file = "problems/example-problems.csv"
    #mini_schedule_file = "data/mini-schedule.csv"
    schedule_file = "data/schedule.csv"         # File containing schedule data

    # Load and preprocess the problem
    problems_df = load_problems_csv(problems_file)
    #mini_schedule_df = read_and_preprocess_csv(mini_schedule_file)
    schedule_df = read_and_preprocess_csv(schedule_file)

    # build Graph from data
    #graph = build_graph(schedule_df)
    #mini_graph = build_graph(mini_schedule_df)
    #expanded_mini_graph = expand_graph(mini_graph)
    #expanded_graph = expand_graph(graph)
    expanded_graph = pickle.load(open('tmp/expanded_graph.txt', 'rb'))
    #pickle.dump(expanded_graph, open('tmp/expanded_graph.txt', 'wb'))
    #nx.write_gexf(expanded_graph, "expanded_schedule.gexf")
    #for node in expanded_graph:
    #    print(type(node[2]))
    #    return 0
    connection, cost = solve_cost_funtion(expanded_graph, 'RTA', 'JONR', schedule_df, 'traveltime')
    #total_time = 0
    print(connection)
    print(cost)
    #connection = construct_connection(schedule_df, *decode_expanded_path(node_sequence))
    #print(connection, cost)
    
        
if __name__ == "__main__":
    main()