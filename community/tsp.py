import networkx as nx
import numpy as np
import math
import statistics

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

# kiszámítja a távolság mátrixot
def PRD_matrix(G, t):
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

# küszöbérték kiszámítása, meddig daraboljuk az utat
def calculate_threshold(PRD, tour):
    tour_length = len(tour)
    D = list()

    for i in range(tour_length - 1):
        D.append(PRD[tour[i], tour[i + 1]])
    D.append(PRD[tour[tour_length - 1], tour[0]])

    mu = statistics.mean(D)
    szigma = statistics.stdev(D, mu)
    delta = mu + szigma

    return delta

# a kapott útvonalat darabolja fel közösségekre
def split_path(PRD, tour):
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
    print(membership)
    print(tour)

    return membership, len(cutting_pos)