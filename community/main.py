import networkx as nx
import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search
import tsp
import nmi
import convert
from timeit import default_timer as timer

def karate():
    karate = nx.read_gml("karate.gml", label='id', destringizer=int)
    convert.create_edgelist(karate, "karate_edge_list.dat")
    convert.get_degree_sequence(karate, "karate_degree_sequence.dat")
    convert.karate_club("karate.dat")

def polbooks():
    polbooks = nx.read_gml("polbooks.gml", label='id', destringizer=int)
    convert.create_edgelist(polbooks, "polbooks_edge_list_0.dat")
    convert.reindex_edgelist("polbooks_edge_list_0.dat", "polbooks_edge_list.dat")
    convert.get_degree_sequence(polbooks, "polbooks_degree_sequence.dat")
    convert.get_communities_from_gml_value_polbooks(polbooks, "polbooks_ground_truth.dat")

def dolphins():
    dolphins = nx.read_gml("dolphins.gml", label='id', destringizer=int)
    convert.create_edgelist(dolphins, "dolphins_edge_list_0.dat")
    convert.reindex_edgelist("dolphins_edge_list_0.dat", "dolphins_edge_list.dat")
    convert.get_degree_sequence(dolphins, "dolphins_degree_sequence.dat")

def football():
    football = nx.read_gml("football.gml", label='id', destringizer=int)
    convert.create_edgelist(football, "football_edge_list_0.dat")
    convert.reindex_edgelist("football_edge_list_0.dat", "football_edge_list.dat")
    convert.get_degree_sequence(football, "football_degree_sequence.dat")
    convert.get_communities_from_gml_value_football(football, "football_ground_truth.dat")

def lesmis():
    lesmis = nx.read_gml("lesmis.gml", label='id', destringizer=int)
    convert.create_edgelist(lesmis, "lesmis_edge_list_0.dat")
    convert.reindex_edgelist("lesmis_edge_list_0.dat", "lesmis_edge_list.dat")
    convert.get_degree_sequence(lesmis, "lesmis_degree_sequence.dat")

def get_ip_nmi_values_real():
    convert.get_ip_communities("karate_x.dat", "karate_ip_communities.dat")
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_ip_communities.dat"))

    convert.get_ip_communities("dolphins_x.dat", "dolphins_ip_communities.dat")

    convert.get_ip_communities("lesmis_x.dat", "lesmis_ip_communities.dat")

    convert.get_ip_communities("polbooks_x.dat", "polbooks_ip_communities.dat")
    print(nmi.get_nmi_value("polbooks_ground_truth.dat", "polbooks_ip_communities.dat"))

    convert.get_ip_communities("football_x.dat", "football_ip_communities.dat")
    print(nmi.get_nmi_value("football_ground_truth.dat", "football_ip_communities.dat"))

def get_tsp_results_karate():
    karate = nx.read_gml("karate.gml", label='id', destringizer=int)

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(karate, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "karate_tsp_communities_sa.dat")

    print("nmi")
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_tsp_communities_sa.dat"))

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(karate, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "karate_tsp_communities_ls.dat")

    print("nmi")
    print(nmi.get_nmi_value("karate_ground_truth.dat", "karate_tsp_communities_ls.dat"))

def get_tsp_results_polbooks():
    polbooks = nx.read_gml("polbooks.gml", label='id', destringizer=int)

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(polbooks, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "polbooks_tsp_communities_sa.dat")

    print("nmi")
    print(nmi.get_nmi_value("polbooks_ground_truth.dat", "polbooks_tsp_communities_sa.dat"))

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(polbooks, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "polbooks_tsp_communities_ls.dat")

    print("nmi")
    print(nmi.get_nmi_value("polbooks_ground_truth.dat", "polbooks_tsp_communities_ls.dat"))

def get_tsp_results_football():
    football = nx.read_gml("football.gml", label='id', destringizer=int)

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(football, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "football_tsp_communities_sa.dat")

    print("nmi")
    print(nmi.get_nmi_value("football_ground_truth.dat", "football_tsp_communities_sa.dat"))

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(football, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "football_tsp_communities_ls.dat")

    print("nmi")
    print(nmi.get_nmi_value("football_ground_truth.dat", "football_tsp_communities_ls.dat"))

def get_tsp_results_dolphins():
    dolphins = nx.read_gml("dolphins.gml", label='id', destringizer=int)

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(dolphins, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "dolphins_tsp_communities_sa.dat")

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(dolphins, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "dolphins_tsp_communities_ls.dat")

def get_tsp_results_lesmis():
    lesmis = nx.read_gml("lesmis.gml", label='id', destringizer=int)

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(lesmis, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "lesmis_tsp_communities_sa.dat")

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(lesmis, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "lesmis_tsp_communities_ls.dat")

def generated():
    network1 = convert.create_graph_from_generated_edgelist("network1.dat")
    convert.create_edgelist(network1, "network1_edge_list_0.dat")
    convert.reindex_edgelist("network1_edge_list_0.dat", "network1_edge_list.dat")
    convert.get_degree_sequence(network1, "network1_degree_sequence.dat")

    network3 = convert.create_graph_from_generated_edgelist("network3.dat")
    convert.create_edgelist(network3, "network3_edge_list_0.dat")
    convert.reindex_edgelist("network3_edge_list_0.dat", "network3_edge_list.dat")
    convert.get_degree_sequence(network3, "network3_degree_sequence.dat")

    network2 = convert.create_graph_from_generated_edgelist("network2.dat")
    convert.create_edgelist(network2, "network2_edge_list_0.dat")
    convert.reindex_edgelist("network2_edge_list_0.dat", "network2_edge_list.dat")
    convert.get_degree_sequence(network2, "network2_degree_sequence.dat")

    network4 = convert.create_graph_from_generated_edgelist("network4.dat")
    convert.create_edgelist(network4, "network4_edge_list_0.dat")
    convert.reindex_edgelist("network4_edge_list_0.dat", "network4_edge_list.dat")
    convert.get_degree_sequence(network4, "network4_degree_sequence.dat")

def get_tsp_results_network1():
    network1 = convert.create_graph_from_generated_edgelist("network1.dat")

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network1, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network1_tsp_communities_sa.dat")

    print("nmi")
    print(nmi.get_nmi_value("network1_ground_truth.dat", "network1_tsp_communities_sa.dat"))

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network1, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network1_tsp_communities_ls.dat")

    print("nmi")
    print(nmi.get_nmi_value("network1_ground_truth.dat", "network1_tsp_communities_ls.dat"))

def get_tsp_results_network3():
    network3 = convert.create_graph_from_generated_edgelist("network3.dat")

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network3, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network3_tsp_communities_sa.dat")

    print("nmi")
    print(nmi.get_nmi_value("network3_ground_truth.dat", "network3_tsp_communities_sa.dat"))

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network3, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network3_tsp_communities_ls.dat")

    print("nmi")
    print(nmi.get_nmi_value("network3_ground_truth.dat", "network3_tsp_communities_ls.dat"))

def get_tsp_results_network2():
    network2 = convert.create_graph_from_generated_edgelist("network2.dat")

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network2, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network2_tsp_communities_sa.dat")

    print("nmi")
    print(nmi.get_nmi_value("network2_ground_truth.dat", "network2_tsp_communities_sa.dat"))

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network2, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network2_tsp_communities_ls.dat")

    print("nmi")
    print(nmi.get_nmi_value("network2_ground_truth.dat", "network2_tsp_communities_ls.dat"))

def get_tsp_results_network4():
    network4 = convert.create_graph_from_generated_edgelist("network4.dat")

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network4, 6)
    tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network4_tsp_communities_sa.dat")

    print("nmi")
    print(nmi.get_nmi_value("network4_ground_truth.dat", "network4_tsp_communities_sa.dat"))

    print("Lokális kereső")
    start = timer()
    distance_matrix = tsp.PRD_matrix(network4, 6)
    tour, distance = solve_tsp_local_search(distance_matrix)
    membership, cuts = tsp.split_path(distance_matrix, tour)
    end = timer()
    print("idő")
    print(end - start)
    convert.get_tsp_communities(membership, cuts, "network4_tsp_communities_ls.dat")

    print("nmi")
    print(nmi.get_nmi_value("network4_ground_truth.dat", "network4_tsp_communities_ls.dat"))

def get_ip_nmi_values_generated():
    convert.get_ip_communities("network1_x.dat", "network1_ip_communities.dat")
    print(nmi.get_nmi_value("network1_ground_truth.dat", "network1_ip_communities.dat"))

    convert.get_ip_communities("network3_x.dat", "network3_ip_communities.dat")
    print(nmi.get_nmi_value("network3_ground_truth.dat", "network3_ip_communities.dat"))

    convert.get_ip_communities("network2_x.dat", "network2_ip_communities.dat")
    print(nmi.get_nmi_value("network2_ground_truth.dat", "network2_ip_communities.dat"))

    convert.get_ip_communities("network4_x.dat", "network4_ip_communities.dat")
    print(nmi.get_nmi_value("network4_ground_truth.dat", "network4_ip_communities.dat"))


def main():
    np.set_printoptions(threshold=np.inf)

if __name__ == '__main__':
    main()
