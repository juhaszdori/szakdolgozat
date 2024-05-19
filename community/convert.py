import networkx as nx

# visszaadja a gráf szomszédsági mátrixát
def get_adjacency_matrix(G):
    A = nx.adjacency_matrix(G, None, None, None)
    A = A.toarray()
    return A

# kiírja egy data fájlba a gráf éllistáját
def create_edgelist(G, data_file):
    nx.set_edge_attributes(G, values=1, name='weight')
    nx.write_weighted_edgelist(G, data_file, delimiter="\t")

# 1-től kezdi a csúcsok indexelését
def reindex_edgelist(data_file, data_file2):
    edgelist = []
    with open(data_file, "r") as f:
        for line in f:
            edge = line.split()
            edge[0] = str(int(edge[0])+1)
            edge[1] = str(int(edge[1])+1)
            edgetuple = (edge[0], edge[1])
            edgelist.append(edgetuple)
    with open(data_file2, "w") as f:
        for e in edgelist:
            f.write(e[0] + "\t" + e[1] + "\t" + "1" + "\n")

# kiírja egy data fájlba a gráf fokszámsorozatát
def get_degree_sequence(G, degree_sequence):
    A = get_adjacency_matrix(G)
    with open(degree_sequence, "w") as f:
        for i in range(0, len(A)):
            f.write(str(i+1) + "\t" + str(sum(A[i])) + "\n")

# visszaad egy gráfot a generált hálózat éllistájából
def create_graph_from_generated_edgelist(generated_file):
    edgelist = list()
    with open(generated_file, "r") as f:
        for line in f:
            edge = line.split()
            if int(edge[0]) < int(edge[1]):
                edgetuple = (int(edge[0]), int(edge[1]))
                edgelist.append(edgetuple)

    G = nx.empty_graph(100)
    for u in edgelist:
        G.add_edge(u[0]-1, u[1]-1)

    return G

# kiírja egy data fájlba a polbooks hálózat közösségszerkezetét a gráf value attribútumából
def get_communities_from_gml_value_polbooks(G, communities):
    community = nx.get_node_attributes(G, "value")
    with open(communities, "w") as f:
        for n, c in community.items():
            if c == 'c':
                c = 1
            elif c == 'l':
                c = 2
            elif c == 'n':
                c = 3
            f.write(str(n+1) + "\t" + str(c) + "\n")

# kiírja egy data fájlba a football hálózat közösségszerkezetét a gráf value attribútumából
def get_communities_from_gml_value_football(G, communities):
    community = nx.get_node_attributes(G, "value")
    with open(communities, "w") as f:
        for n, c in community.items():
            f.write(str(n+1) + "\t" + str(c+1) + "\n")

# 1-től kezdi a csúcsok indexelését
def create_(data_file, data_file2):
    edgelist = []
    with open(data_file, "r") as f:
        for line in f:
            edge = line.split()
            edge[0] = str(int(edge[0])+1)
            edge[1] = str(int(edge[1])+1)
            edgetuple = (edge[0], edge[1])
            edgelist.append(edgetuple)
    with open(data_file2, "w") as f:
        for e in edgelist:
            f.write(e[0] + "\t" + e[1] + "\n")

# karate klub optimális közösségszerkezetét írja ki egy data fájlba
def karate_club(data_file):
    G = nx.karate_club_graph()
    with open(data_file, "w") as f:
        for i in G.nodes():
            f.write(f"{i + 1} {G.nodes[i]['club']}" + "\n")

# kiírja egy data fájlba a tsp által visszaadott közösségszerkezetet
def get_tsp_communities(membership, cuts, file):
    membership = dict(sorted(membership.items()))
    with open(file, "w") as f:
        for n, c in membership.items():
            f.write(str(n+1) + "\t" + str(c) + "\n")
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
        for line in f:
            xij = line.split()
            if int(int(xij[0])) != 1 and int(xij[0]) not in leftover:
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


