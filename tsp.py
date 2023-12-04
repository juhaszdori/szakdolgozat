import networkx as nx
import numpy as np
import math
import statistics
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search #, solve_tsp_lin_kernighan
#from python_tsp.heuristics import solve_tsp_record_to_record

def PRF_matrix(G, t):
    A = nx.adjacency_matrix(G, None, None, None)
    A = A.toarray()

    degrees = dict(nx.degree(G)).values()
    deegreelist = list()
    for d in degrees:
        deegreelist.append(1 / d)

    D = np.diag(deegreelist)
    S = np.matmul(D, A)

    PRF = S
    for i in range(2, t+1):
        PRF = np.matmul(S, PRF)
    return PRF

def PRD_matrix(G, t):   # kiszámítja a távolság mátrixot
    n = nx.number_of_nodes(G)
    PRF = PRF_matrix(G, t)
    PRD = np.zeros((n, n))

    pp = np.empty(n, int)
    for i in range(0, n):
        p = np.array(PRF[i,:])
        max_rwf = np.max(p)
        for j in range(0, n):
            if PRF[i,j] == max_rwf:
                pp[i] = j
    pp = np.unique(pp)

    for i in range(0, n):
        for j in range(0, n):
            summ = 0
            for k in pp:
                diff = (PRF[i,k] - PRF[j,k]) * (PRF[i,k] - PRF[j,k])
                summ = summ + diff
            PRD[i,j] = math.sqrt(summ)
    return PRD

def main():
    np.set_printoptions(threshold=np.inf)
    #G = nx.karate_club_graph()
    G = nx.les_miserables_graph()

    distance_matrix = PRD_matrix(G, 6)

    permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
    print(permutation, distance)

    permutation2, distance2 = solve_tsp_local_search(distance_matrix)
    print(permutation2, distance2)

    #permutation3, distance3 = solve_tsp_lin_kernighan(distance_matrix)
    #print(permutation3, distance3)

if __name__ == '__main__':
    main()