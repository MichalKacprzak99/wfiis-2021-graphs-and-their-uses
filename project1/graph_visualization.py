import graph_generation
import math
import random as rand
import numpy as np
from vpython import *


def visualize_graph(graph):
    scene = canvas(width=500, height=500)

    print(graph)

    (verticeNumber, verticeNumber) = graph.shape

    rfactor = 5
    radius = verticeNumber/2
    vertices = []
    r = rfactor * verticeNumber
    x0 = 0
    y0 = 0

    thetaFactor = 360 / verticeNumber
    theta = 0
    for i in range(verticeNumber):
        theta = i * radius * thetaFactor
        positionVector = vector(x0 + r * math.cos(theta),
                                y0 + r * math.sin(theta), 0)
        label(pos=positionVector, text=str(i+1), opacity=0, box=False)
        vertices.append(sphere(pos=positionVector, radius=radius,
                               color=vec(rand.random(), rand.random(), rand.random())))

    result = np.where(graph == 1)
    lista_sasiedztwa = np.sort(list(zip(result[0], result[1])))

    z = [tuple(i) for i in np.unique(lista_sasiedztwa, axis=0)]

    for (first, second) in z:
        curve(vertices[first].pos, vertices[second].pos, color=color.cyan)


visualize_graph(graph_generation.generate_N_L_graph(10, 10))
