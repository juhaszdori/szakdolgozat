import math

# visszaadja a közösségeket egy listában és a számukat
def get_communities(file, communities):
    nodes = list()
    with open(file, "r") as community_file:
        for line in community_file:
            node_community = line.split()  # 1 sor egy lista, 0. eleme a csúcs, 1. eleme a közösség
            node = int(node_community[0])
            community = int(node_community[1])

            nodes.append(node)

            if community-1 not in communities:
                communities[community-1] = set()
            communities[community-1].add(node)

        n = len(nodes)
    return communities, n

# kiszámítja az nmi értékét
def get_nmi_value(A, B):
    szamlalo = 0
    nevezo1 = 0
    nevezo2 = 0
    n = 0

    communities_A = dict()
    communities_B = dict()

    # a dat fájl a csúcsok listáját tartalmazza, minden csúcs mellett a közössége szerepel
    cA, nA = get_communities(A, communities_A)
    cB, nB = get_communities(B, communities_B)

    # meg kell egyeznie, mert azonos a hálózat
    if nA == nB:
        n = nA

    for i in cA:
        for j in cB:
            nij = len(communities_A[i] & communities_B[j])
            ni = len(communities_A[i])
            nj = len(communities_B[j])
            if nij > 0:
                szamlalo += nij * math.log((nij * n) / (ni * nj))

    for i in cA:
        ni = len(communities_A[i])
        nevezo1 += ni * math.log(ni / n)

    for j in cB:
        nj = len(communities_B[j])
        nevezo2 += nj * math.log(nj / n)

    return -2 * szamlalo / (nevezo1 + nevezo2)