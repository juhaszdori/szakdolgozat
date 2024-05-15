import networkx as nx
import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search, solve_tsp_lin_kernighan
import tsp
import nmi
import convert
from timeit import default_timer as timer

def main():
    np.set_printoptions(threshold=np.inf)

    # Zachary's karate club
    # IP data
    karate = nx.read_gml("karate.gml", label='id', destringizer=int)
    convert.create_edgelist(karate, "karate_edge_list.dat")
    convert.get_degree_sequence(karate, "karate_degree_sequence.dat")

    # alapigazság kozosseg karate_club()

    # IP test
    convert.get_ip_communities("karate_x.dat", "karate_ip_communities.dat")

    # tsp tests
    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(karate, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print(end - start)
    convert.print_community_file(membership, cuts, "karate_tsp_communities.dat")

    # nmi values
    print("nmi")
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_ip_communities.dat"))
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_tsp_communities.dat"))


if __name__ == '__main__':
    main()
