import math

def get_communities(community, node_list):
    with open(community, "r") as community_file:
        for line in community_file:
            line = community_file.readline()
            node_community = line.split()
            # 1 sor egy lista, 0. eleme a csúcs, 1. eleme a közösség
            node = node_community[0]
            community = node_community[1]

            node_list[node] = node

            if community not in node_list:
                node_list[community] = set()
            node_list[community].add(node)

            c = len(node_list)
            n = len(node_list)
    return c, n

def get_nmi_value(A, B):
    szamlalo = 0
    nevezo1 = 0
    nevezo2 = 0
    n = 0
    #nA = 0
    #nB = 0
    #cA = 0
    #cB = 0

    community_list_A = list()
    community_list_B = list()
    node_list_A = list()
    node_list_B = list()

    # a dat fájl a csúcsok listáját tartalmazza, minden csúcs mellett a közössége szerepel
    cA, nA = get_communities(A, node_list_A)
    cB, nB = get_communities(B, node_list_B)

    #get_communities("community.dat", node_list_A, cA, nA)
    #get_communities("tsp.dat", node_list_B, cB, nB)

    # meg kell egyeznie, mert azonos a hálózat
    if nA == nB:
        n = nA

    for i in range(1, cA + 1):
        for j in range(1, cB + 1):
            nij = len(community_list_A[i] & community_list_B[j])
            ni = len(community_list_A[i])
            nj = len(community_list_B[j])
            if nij > 0:
                szamlalo += nij * math.log((nij * n) / (ni * nj))

    for i in range(1, cA + 1):
        ni = len(community_list_A[i])
        nevezo1 += ni * math.log(ni / n)

    for j in range(1, cB + 1):
        nj = len(community_list_B[j])
        nevezo2 += nj * math.log(nj / n)

    return -2 * szamlalo / (nevezo1 + nevezo2)