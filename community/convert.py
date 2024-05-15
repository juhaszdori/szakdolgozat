import networkx as nx

# visszaadja a gráf szomszédsági mátrixát
def get_adjacency_matrix(G):
    A = nx.adjacency_matrix(G, None, None, None)
    A = A.toarray()
    return A

# kiírja egy data fájlba a gráf éllistáját
def create_edgelist(G, data_file):
    nx.set_edge_attributes(G, values=1, name='weight')
    nx.write_weighted_edgelist(G, data_file)

# kiírja egy data fájlba a gráf fokszámsorozatát
def get_degree_sequence(G, degree_sequence):
    A = get_adjacency_matrix(G)
    with open(degree_sequence, "w") as f:
        for i in range(0, len(A)):
            f.write(str(i+1) + "\t" + str(sum(A[i])) + "\n")

# visszaad egy gráfot a generált hálózat éllistájából
def create_graph_from_generated_edgelist(edgelist_file):
    edgelist = []
    with open(edgelist_file, "r") as f:
        for line in f:
            edge = line.split()
            if edge[0] < edge[1]:
                edgetuple = (edge[0], edge[1])
                edgelist.append = (edgetuple)

    G = nx.from_edgelist(edgelist)
    return G

# kiírja egy data fájlba a valós világbeli teszt hálózatok közösségszerkezetét a gráf value attribútumából
def get_communities_from_gml_value(G, communities):
    community = nx.get_node_attributes(G, "value")
    with open(communities, "w") as f:
        for i in range(0, len(community)):
            f.write(str(i) + "\t" + str(community[i]) + "\n")

# karate klub optimális közösségszerkezetét írja ki
def karate_club():
    G = nx.karate_club_graph()
    for i in G.nodes():
        print(f"{i + 1} {G.nodes[i]['club']}")

# kiírja egy data fájlba a tsp által visszaadott közösségszerkezetet
def print_community_file(membership, cuts, file):
    with open(file, "w") as f:
        for n, c in membership.items():
            if c > cuts:
                f.write(str(n) + "\t" + "1" + "\n")
            else:
                f.write(str(n) + "\t" + str(c) + "\n")
    print("közösségek száma: " + str(cuts))

# kiírja egy data fájlba az ip által visszaadott közösségszerkezetet
def get_ip_communities(matrix, communities):
    list = []
    with open(matrix, "r") as f:
        f.readline()
        c = 1
        nodes = f.readline()
        leftover_numbers = nodes.split()
        for i in leftover_numbers:
            if i == ':' or i == ':=':
                leftover_numbers.remove(i)
        leftover = [eval(i) for i in leftover_numbers]
        list.append((1, c))
        for line in f:
            xij = line.split()
            if int(xij[0]) not in leftover:
                continue
            list.append((int(xij[0]), c))
            for j in range(1, len(xij)):
                if xij[j] == '.':
                    continue
                node = j+1
                x = int(xij[j])
                if node in leftover:
                    if x == 0:
                        tuple = (node,c)
                        list.append(tuple)
                        if node in leftover:
                            leftover.remove(node)
            c = c+1

    with open(communities, "w") as f:
        list = sorted(list)
        for i in list:
            pair = i
            f.write(str(pair[0]) + "\t" + str(pair[1]) + "\n")
    print("közösségek száma: " + str(c-1))


