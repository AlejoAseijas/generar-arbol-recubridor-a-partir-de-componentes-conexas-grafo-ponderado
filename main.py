import networkx as nx
from dibujarGrafo import dibujar_grafo
from MatrixPesos import MatrixPesos;

# Crear el grafo a partir de la matriz de pesos
GrafoPonderado = nx.from_numpy_array(MatrixPesos)

# Graficamos el grafo completo
dibujar_grafo(GrafoPonderado, 'GrafoPonderado')

# Obtengo las componentes conexas del grafo ponderado
componentesConexas = list(nx.connected_components(GrafoPonderado))

# Graficar cada componente conexa y su árbol recubridor mínimo
arboles_recubridores_minimal = []

for i, componenteConexa in enumerate(componentesConexas):
    # Crear un subgrafo para la componente actual
    subgrafo = GrafoPonderado.subgraph(componenteConexa)
    
    # Calcular el árbol recubridor mínimo
    arbol_recubridor = nx.minimum_spanning_tree(subgrafo, algorithm='kruskal')
    
    # Almacenar el árbol recubridor mínimo
    arboles_recubridores_minimal.append(arbol_recubridor)
    
    # Graficar el árbol recubridor mínimo
    dibujar_grafo(arbol_recubridor, f'Árbol Recubridor Mínimo Componente {i}')

# Imprimir los árboles recubridores mínimos
for i, arbol in enumerate(arboles_recubridores_minimal):
    print(f"Árbol recubridor mínimo para la componente conexa {i}:")
    print(arbol.edges(data=True))

# Calcular el peso total de cada árbol recubridor mínimo
pesos_arboles = []

for i, arbol in enumerate(arboles_recubridores_minimal):
    peso_total = sum(weight for _, _, weight in arbol.edges(data='weight'))
    pesos_arboles.append(peso_total)
    print(f"Peso total del árbol recubridor mínimo para la componente conexa {i}: {peso_total}")
