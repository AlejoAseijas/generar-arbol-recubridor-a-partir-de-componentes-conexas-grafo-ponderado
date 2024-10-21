# Proyecto de Grafo Ponderado

Este proyecto utiliza la biblioteca `NetworkX` para crear y visualizar un grafo ponderado a partir de una matriz de pesos. Además, se calcula el árbol recubridor mínimo para cada componente conexa del grafo y se visualiza.

## Requisitos

- Python 3.x
- Biblioteca `networkx`
- Biblioteca `numpy`
- Biblioteca `matplotlib`

## Instalación

### 1. Clonar el Repositorio

Asegúrate de tener [Git](https://git-scm.com/) instalado en tu sistema. Luego, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
```

### 2.  Instalar Dependencias

Asegúrate de tener [Python 3](https://www.python.org/downloads/release/python-3130/) instalado en tu sistema. Luego, instala las bibliotecas necesarias utilizando pip:

```bash
pip install networkx numpy matplotlib
```

## Estructura del Proyecto

```bash
nombre-del-repositorio/
├── dibujarGrafo.py       # Contiene la función dibujar_grafo para graficar el grafo.
├── MatrixPesos.py        # Archivo donde se define la matriz de pesos del grafo.
├── main.py               # Script principal que crea y visualiza el grafo.
└── imgs/                 # Carpeta donde se guardan las imágenes generadas. Se genera automaticamente
```

## Uso
### Ejecutar el Script Principal

### 1. Definir la Matriz de Pesos

Abre el archivo MatrixPesos.py y define la matriz de pesos que representa el grafo. La matriz debe ser de forma cuadrada, donde los elementos representan los pesos de las aristas entre los nodos. Un valor de 0 indica que no hay conexión entre los nodos. 

### 2. Ejecutar el Script

Ejecuta el script principal para crear el grafo, calcular los árboles recubridores mínimos y generar las visualizaciones:

```bash
python main.py
```

### 3. Visualizar Resultados

Las imágenes generadas se guardarán en la carpeta ./imgs/. Puedes abrirlas para ver el grafo completo y los árboles recubridores mínimos para cada componente conexa.
