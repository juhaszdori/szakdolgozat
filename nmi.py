import math

def nmi(A, B):
    teteje =0
    alja1 = 0
    alja2 = 0
    n = 0
    cA = 0
    cB = 0
    
    community_list_A = list()
    community_list_B = list()
    node_list_A = list()
    node_list_B = list()
    #ellenőrizni kell hogy ugyanannyi
    
    # a dat fájl a csúcsok listáját tartalmazza, minden csúcs mellett a közössége szerepel
    
    with open("community.dat", "r") as community_file:
        for line in community_file:
            line = community_file.readline()
            node_community = line.split()
            # 1 sor egy lista, 0. eleme a csúcs, 1. eleme a közösség
            node = node_community[0]
            community = node_community[1]
            
            node_list_A[node] = node
            
            if community not in community_list:
                community_list_A[community] = set()
            community_list_A[community].add(node)
            
            cA = len(community_list_A)
            n = len(node_list_A)

    for i in range(1, cA+1):
        for j in range(1, cB+1):
            nij = len(community_list_A[i] & community_list_B[j])        
            ni = len(community_list_A[i])
            nj = len(community_list_B[j])
            if n_ij > 0:
                teteje += nij * log( (nij*n) / (ni*nj) )
    
    for j in range(1, cA+1):
        ni = len(community_list_A[i])
        alja1 += ni * log( ni/n )
            
    for j in range(1, cB+1):
        nj = len(community_list_B[j])
        alja2 += nj * log( nj/n )
    
    return -2 * teteje/(alja1+alja2)

def get_communities(community):
    with open(community, "r") as communities:
        line = communities.readline()
        
        while line:
            line = communities.readline()
 

def main():

    nmi()

if __name__ == '__main__':
    main()