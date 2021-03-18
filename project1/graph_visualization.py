import graph_generation
import math
import random as rand
import numpy as np
from vpython import *


def visualize_graph(graph_by_matrix):
    scene = canvas(width=1000, height=800)

    (vertexNumber, vertexNumber) = graph_by_matrix.shape

    rfactor = 50
    radius = -(1/4) * vertexNumber + 100
    vertice = []
    r = rfactor * vertexNumber + 100
    x0 = 0
    y0 = 0

    t = np.linspace(0, 2 * math.pi, vertexNumber + 1)
    for i in range(vertexNumber):
        positionVector = vector(x0 + (r+radius) * math.sin(t[i]),
                                y0 + (r+radius) * math.cos(t[i]), 0)
        label(pos=positionVector, text=str(i+1), opacity=0, box=False)
        vertice.append(sphere(pos=positionVector, radius=radius,
                               color=vec(rand.random(), rand.random(), rand.random())))

    result = np.where(graph_by_matrix == 1)
    listaa = np.sort(list(zip(result[0], result[1])))

    z = [tuple(i) for i in np.unique(listaa, axis=0)]

    for (first, second) in z:
        curve(vertice[first].pos, vertice[second].pos, color=vec(rand.random(), rand.random(), rand.random()))
    scene.capture("letnie_dranie_graph")