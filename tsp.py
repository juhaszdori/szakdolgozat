import networkx as nx
import numpy as np
import math
import statistics
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search, solve_tsp_lin_kernighan
from timeit import default_timer as timer

def PRF_matrix(G, t):
    A = nx.adjacency_matrix(G, None, None, None)
    A = A.toarray()

    degrees = dict(nx.degree(G)).values()
    probabilitylist = list()
    for d in degrees:
        probabilitylist.append(1 / d)

    P = np.diag(probabilitylist)
    R = np.matmul(P,A)
    T = np.transpose(R)

    PRF = T
    for i in range(2, t+1):
        PRF = np.matmul(T, PRF)
    return PRF


def PRD_matrix(G, t):   # kiszámítja a távolság mátrixot
    n = nx.number_of_nodes(G)
    PRF = PRF_matrix(G, t)
    PRD = np.zeros((n, n))
    pp = set()

    for i in range(0, n):
        p = np.array(PRF[:,i])
        max_rwf = np.max(p)
        for j in range(0, n):
            if PRF[j,i] == max_rwf:
                pp.add(j)

    for i in range(0, n):
        for j in range(0, n):
            summ = 0
            for k in pp:
                diff = (PRF[k,i] - PRF[k,j]) * (PRF[k,i] - PRF[k,j])
                summ = summ + diff
            PRD[j,i] = math.sqrt(summ)
    return PRD


def calculate_threshold(PRD, tour): # küszöbérték kiszámtása, meddig darabolunk
    tour_length = len(tour)
    D = list()

    for i in range(tour_length - 1):
        D.append(PRD[tour[i], tour[i + 1]])
    D.append(PRD[tour[tour_length - 1], tour[0]])

    mu = statistics.mean(D)
    szigma = statistics.stdev(D, mu)
    delta = mu + szigma

    return delta


def split_path(PRD, tour):   # a kapott útvonalat darabolja fel közösségekre
    tour_length = len(tour)
    cutting_pos = list()
    membership = dict()
    community = 1

    delta = calculate_threshold(PRD, tour)

    for i in range(tour_length-1):
        membership[tour[i]] = community
        if PRD[tour[i],tour[i+1] ] > delta:
            cutting_pos.append(tour[i])
            community = community+1
    if PRD[tour[tour_length-1],tour[0]] > delta:
        cutting_pos.append(tour[tour_length-1])
    membership[tour[tour_length-1]] = community

    return membership, len(cutting_pos)


def print_community_file(membership, cuts, filename):
    with open(filename, "w") as f:
        c = dict(sorted(membership.items()))

        for n, c in c.items():
            if c > cuts:
                f.write(str(n) + "\t" + "1" + "\n")
            else:
                f.write(str(n) + "\t" + str(c) + "\n")

    print("közösségek száma: " + str(cuts))

def main():
    np.set_printoptions(threshold=np.inf)

    G = nx.read_gml("karate.gml", label='id', destringizer=int)
    G = nx.read_gml("dolphins.gml", label='id', destringizer=int)
    G = nx.read_gml("lesmis.gml", label='id', destringizer=int)
    G = nx.read_gml("polbooks.gml", label='id', destringizer=int)
    G = nx.read_gml("football.gml", label='id', destringizer=int)

    print("Szimulált hűtés")
    start = timer()
    distance_matrix = PRD_matrix(G, 6)
    permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
    #print(permutation, distance)
    membership, cuts = split_path(distance_matrix, permutation)
    end = timer()
    print(end - start)
    print_community_file(membership, cuts, "simulated_annealing.dat")


    print("Helyi keresés")
    start = timer()
    distance_matrix = PRD_matrix(G, 6)
    permutation2, distance2 = solve_tsp_local_search(distance_matrix)
    #print(permutation2, distance2)
    membership, cuts = split_path(distance_matrix, permutation2)
    end = timer()
    print(end - start)
    print_community_file(membership, cuts, "local_search.dat")

    #permutation3, distance3 = solve_tsp_lin_kernighan(distance_matrix)
    #print(permutation3, distance3)



if __name__ == '__main__':
    main()