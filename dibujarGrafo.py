import matplotlib
matplotlib.use('Agg')
import os
import networkx as nx
import matplotlib.pyplot as plt

if not os.path.exists('./imgs'):
    os.makedirs('./imgs')

def dibujar_grafo(grafo, tituloFoto):
    pos = nx.spring_layout(grafo, k=0.1)  
    plt.figure(figsize=(10, 8))  

    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', 
            node_size=700, font_size=12, font_color='black', 
            edge_color='gray', width=2, alpha=0.8)

    plt.title(tituloFoto, fontsize=16)
    plt.axis('off')  
    plt.savefig(f"./imgs/{tituloFoto}.png", bbox_inches='tight')  
    plt.close() 