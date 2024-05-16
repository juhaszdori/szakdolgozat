import networkx as nx
import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search, solve_tsp_lin_kernighan
import tsp
import nmi
import convert
from timeit import default_timer as timer

def karate():
    #Zachary's karate club
    # IP data
    karate = nx.read_gml("karate.gml", label='id', destringizer=int)
    convert.create_edgelist(karate, "karate_edge_list.dat")
    convert.get_degree_sequence(karate, "karate_degree_sequence.dat")

    # alapigazság kozosseg
    convert.karate_club("karate.dat")

    # IP test
    convert.get_ip_communities("karate_x.dat", "karate_ip_communities.dat")

    # tsp tests
    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(karate, 6)
    tour, distance = solve_tsp_lin_kernighan(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "karate_tsp_communities.dat")

    # nmi values
    print("nmi")
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_ip_communities.dat"))
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_tsp_communities.dat"))

def polbooks():
    # Books about U.S. politics
    polbooks = nx.read_gml("polbooks.gml", label='id', destringizer=int)
    convert.create_edgelist(polbooks, "polbooks_edge_list_0.dat")
    convert.reindex_edgelist("polbooks_edge_list_0.dat", "polbooks_edge_list.dat")
    convert.get_degree_sequence(polbooks, "polbooks_degree_sequence.dat")
    convert.get_communities_from_gml_value_polbooks(polbooks, "polbooks_ground_truth.dat")

def football():
    # College Football
    football = nx.read_gml("football.gml", label='id', destringizer=int)
    convert.create_edgelist(football, "football_edge_list_0.dat")
    convert.reindex_edgelist("football_edge_list_0.dat", "football_edge_list.dat")
    convert.get_degree_sequence(football, "football_degree_sequence.dat")

def dolphins():
    # Dolphin social network
    dolphins = nx.read_gml("dolphins.gml", label='id', destringizer=int)
    convert.create_edgelist(dolphins, "dolphins_edge_list_0.dat")
    convert.reindex_edgelist("dolphins_edge_list_0.dat", "dolphins_edge_list.dat")
    convert.get_degree_sequence(dolphins, "dolphins_degree_sequence.dat")

def football():
    # College Football
    football = nx.read_gml("football.gml", label='id', destringizer=int)
    convert.create_edgelist(football, "football_edge_list_0.dat")
    convert.reindex_edgelist("football_edge_list_0.dat", "football_edge_list.dat")
    convert.get_degree_sequence(football, "football_degree_sequence.dat")
    convert.get_communities_from_gml_value_football(football, "football_ground_truth.dat")

def lesmis():
    # Les Miserables
    lesmis = nx.read_gml("lesmis.gml", label='id', destringizer=int)
    convert.create_edgelist(lesmis, "lesmis_edge_list_0.dat")
    convert.reindex_edgelist("lesmis_edge_list_0.dat", "lesmis_edge_list.dat")
    convert.get_degree_sequence(lesmis, "lesmis_degree_sequence.dat")

def generated():
    # generált
    network2 = convert.create_graph_from_generated_edgelist("network2.dat")
    convert.create_edgelist(network2, "network2_edge_list.dat")
    convert.get_degree_sequence(network2, "network2_degree_sequence.dat")

    network3 = convert.create_graph_from_generated_edgelist("network3.dat")
    convert.create_edgelist(network3, "network3_edge_list.dat")
    convert.get_degree_sequence(network3, "network3_degree_sequence.dat")

def get_ip_nmi_values():
    network4 = convert.create_graph_from_generated_edgelist("network4.dat")
    convert.create_edgelist(network4, "network4_edge_list.dat")
    convert.get_degree_sequence(network4, "network4_degree_sequence.dat")

    convert.get_ip_communities("karate_x.dat", "karate_ip_communities.dat")
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_ip_communities.dat"))

    convert.get_ip_communities("dolphins_x.dat", "dolphins_ip_communities.dat")

    convert.get_ip_communities("lesmis_x.dat", "lesmis_ip_communities.dat")

    polbooks = nx.read_gml("polbooks.gml", label='id', destringizer=int)
    convert.get_communities_from_gml_value_polbooks(polbooks, "polbooks_ground_truth.dat")
    convert.get_ip_communities("polbooks_x.dat", "polbooks_ip_communities.dat")
    print(nmi.get_nmi_value("polbooks_ground_truth.dat", "polbooks_ip_communities.dat"))

    football = nx.read_gml("football.gml", label='id', destringizer=int)
    convert.get_communities_from_gml_value_polbooks(football, "football_ground_truth.dat")
    convert.get_ip_communities("football_x.dat", "football_ip_communities.dat")
    print(nmi.get_nmi_value("football_ground_truth.dat", "football_ip_communities.dat"))

def get_tsp_results():
    convert.get_tsp_communities(membership, cuts, "karate_tsp_communities.dat")
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_tsp_communities.dat"))

def main():
    np.set_printoptions(threshold=np.inf)















if __name__ == '__main__':
    main()
