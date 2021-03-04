import graph_generation
import math
import random as rand
import numpy as np
from vpython import *


def visualize_graph(graph):
    scene = canvas(width=1000, height=800)

    (verticeNumber, verticeNumber) = graph.shape

    rfactor = 50
    radius = -(1/4) * verticeNumber + 100
    vertices = []
    r = rfactor * verticeNumber + 100
    x0 = 0
    y0 = 0

    t = np.linspace(0, 2 * math.pi, verticeNumber + 1 )
    theta = 0
    for i in range(verticeNumber):
        positionVector = vector(x0 + (r+radius) * math.sin(t[i]),
                                y0 + (r+radius) * math.cos(t[i]), 0)
        label(pos=positionVector, text=str(i+1), opacity=0, box=False)
        vertices.append(sphere(pos=positionVector, radius=radius,
                               color=vec(rand.random(), rand.random(), rand.random())))

    result = np.where(graph == 1)
    lista_sasiedztwa = np.sort(list(zip(result[0], result[1])))

    z = [tuple(i) for i in np.unique(lista_sasiedztwa, axis=0)]

    for (first, second) in z:
        curve(vertices[first].pos, vertices[second].pos, color=vec(rand.random(), rand.random(), rand.random()))


visualize_graph(graph_generation.generate_N_L_graph(40, 10))
