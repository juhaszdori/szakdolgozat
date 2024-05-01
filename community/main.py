import networkx as nx
import numpy as np
import scipy as sp
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search, solve_tsp_lin_kernighan
from tsp import PRD_matrix, split_path, print_community_file
import nmi
from amplpy import AMPL

def create_adjacency_from_generated_edgelist(edgelist):
    A = edgelist
    return A

def get_ilp_communities(matrix):
    C = matrix
    return C

def convert_edgelist_for_ilp(input, output):
    input

# elkészíti és kiírja egy data fájlba a valós világbeli teszt hálózatok éllistáját
def create_edgelist_from_gml(gml_file, data_file):
    G = nx.read_gml(gml_file, label='id', destringizer=int)
    nx.set_edge_attributes(G, values=1, name='weight')
    nx.write_weighted_edgelist(G, data_file)

# data fájlok az ampl modellhez
def get_edgelist_for_ilp():
    create_edgelist_from_gml("karate.gml", "karate.dat")
    create_edgelist_from_gml("dolphins.gml", "dolphins.dat")
    create_edgelist_from_gml("lesmis.gml", "lesmis.dat")
    create_edgelist_from_gml("polbooks.gml", "polbooks.dat")
    create_edgelist_from_gml("football.gml", "football.dat")

   # G = nx.read_gml("karate.gml", label='id', destringizer=int)
   # nx.set_edge_attributes(G, values=1, name='weight')
   # nx.write_weighted_edgelist(G, "karate.dat")

# visszaadja a valós világbeli teszt hálózatok szomszédsági mátrixát
# visszatérési értéke a tsp algoritmus bemenete
def get_adjacency_matrix_from_gml(gml_file):
    G = nx.read_gml(gml_file, label='id', destringizer=int)
    A = nx.adjacency_matrix(G, None, None, None)
    A = A.toarray()
    #print(A)
    return A

def karate_club():
    G = nx.karate_club_graph()
    n = nx.number_of_nodes(G)
    np.set_printoptions(threshold=np.inf)

    gt_membership = [G.nodes[v]['club'] for v in G.nodes()]
    for i in G.nodes():
        print(f"{i + 1} {G.nodes[i]['club']}")

    A = nx.adjacency_matrix(G, None, None, None)  # SciPy sparse array
    A = A.toarray()  # A = A.todense()
    #print(A)

    print("Node Degree")
    for v in G:
        print(f"{v:4} {G.degree(v):6}")

    G.nodes[5]["club"]
    'Mr. Hi'
    G.nodes[9]["club"]
    'Officer'


    #gml = nx.read_gml("karate.gml", label='id', destringizer=int)
    #print(gml.edges)
    #gml = gml.split("\n")[1:]
    #G = nx.parse_gml(gml)  # parse gml data

    # print degree for each team - number of games
    #for n, d in G.degree():
        #print(f"{n:20} {d:2}")


    #for i in G.nodes():
        #print(f"{i} {G.nodes[i]}")

def run_ampl():
    ampl = AMPL()

def main():
    np.set_printoptions(threshold=np.inf)

    get_adjacency_matrix_from_gml("karate.gml")
    #get_adjacency_matrix_from_gml("dolphins.gml")
    #get_adjacency_matrix_from_gml("lesmis.gml")
    #get_adjacency_matrix_from_gml("polbooks.gml")
    #get_adjacency_matrix_from_gml("football.gml")

    #get_edgelist_for_ip_model()

    karate_club()

    run_ampl()

    #nmi.get_nmi_value("community.dat", "tsp.dat")
    #nmi.get_nmi_value("community.dat", "ilp.dat")




if __name__ == '__main__':
    main()
