import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:

    def __init__(self,vertice):
        self.V = vertice
        self.grafo = []

    def addEdge(self, u,v,w):
      self.grafo.append([u,v,w])

      
    def PrimMst(self, raiz):
        # Total de vértices no grafo
        n = self.V

        # Total de arestas no grafo
        m = len(self.grafo)

        # Fila de prioridade para armazenar as arestas potenciais da árvore geradora mínima
        H = []

        # Lista de adjacência que armazena as arestas do grafo
        n_out = [[] * n for i in range(n)]

        # Preenchendo n_out com base nas arestas do grafo
        for j in range(m):
            a, b, c = self.grafo[j]
            n_out[a].append((b, c))
            n_out[b].append((a, c))

        # Inicializa a fila de prioridade H com arestas saindo do vértice raiz
        for (x, c) in n_out[raiz]:
            heapq.heappush(H, (c, raiz, x))

        # Inicialização de variáveis
        n_edges = 0
        custo_tot = 0
        marcados = [raiz]
        arv_ger_min = []

        # Loop principal para construir a árvore mínima
        while n_edges < n - 1:
            while True:
                # Extrai a aresta de menor peso que leva a um vértice não marcado
                (c, a, b) = heapq.heappop(H)
                if b not in marcados:
                    break

            # Marca o vértice b como visitado
            marcados.append(b)

            # Atualiza o custo total e adiciona a aresta à árvore mínima
            custo_tot += c
            arv_ger_min.append((a, b, c))

            # Incrementa o contador de arestas
            n_edges += 1

            # Adiciona arestas saindo do vértice b para a fila de prioridade
            for (x, c) in n_out[b]:
                if x not in marcados:
                    heapq.heappush(H, (c, b, x))

        # Imprime a árvore geradora mínima
        print(arv_ger_min)


class Grafo_biblioteca_nx:
    def __init__(self):
        self.grafo = nx.Graph()


    def adicionar_aresta(self, u, v, peso):
        self.grafo.add_edge(u, v, weight=peso)

    def algoritmo_prim(self):
        T = nx.minimum_spanning_tree(self.grafo, algorithm='prim')
        return T



if __name__ == '__main__':
    grafo = Grafo(5)

    grafo.addEdge(0,1,15)
    grafo.addEdge(0,2,12)
    grafo.addEdge(0,3,13)
    grafo.addEdge(0,4,20)
    grafo.addEdge(1,2,16)
    grafo.addEdge(1,3,16)
    grafo.addEdge(1,4,5)
    grafo.addEdge(2,3,1)
    grafo.addEdge(2,4,18)
    grafo.addEdge(3,4,17)

    print(grafo.grafo)

    print("Primm")
    grafo.PrimMst(0)
 

    grafo_bio = Grafo_biblioteca_nx()
    
    for u,v,peso in grafo.grafo:
         grafo_bio.adicionar_aresta(u,v,peso)

    arvore_Gerada_Prin_biblioteca = grafo_bio.algoritmo_prim()

    pos = nx.spring_layout(arvore_Gerada_Prin_biblioteca)
    labels = nx.get_edge_attributes(arvore_Gerada_Prin_biblioteca, 'weight')
    nx.draw_networkx_nodes(arvore_Gerada_Prin_biblioteca, pos)
    nx.draw_networkx_edges(arvore_Gerada_Prin_biblioteca, pos)
    nx.draw_networkx_edge_labels(arvore_Gerada_Prin_biblioteca, pos, edge_labels=labels)
    nx.draw_networkx_labels(arvore_Gerada_Prin_biblioteca, pos)
    plt.title("arvore minima spanning")
    plt.show()
