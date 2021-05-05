import math
import random as rand
import numpy as np
from vpython import *


def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def visualize_graph(graph_by_matrix: np.ndarray, weighted_graph: bool = False):
    """Method to visualize graph using vPython

        Parameters:
        graph_by_matrix (np.ndarray): graph given by matrix
        weighted_graph (bool): flag to determine if graph is weighted

        Returns:
        None

       """
    canvas(width=1000, height=800)

    (vertexNumber, vertexNumber) = graph_by_matrix.shape

    rfactor = 20
    radius = -(1 / 4) * vertexNumber + 50
    vertices = []
    r = rfactor * vertexNumber + 100
    x0 = 0
    y0 = 0

    t = np.linspace(0, 2 * math.pi, vertexNumber + 1)
    for i in range(vertexNumber):
        positionVector = vector(x0 + (r + radius) * math.sin(t[i]),
                                y0 + (r + radius) * math.cos(t[i]), 0)
        label(pos=positionVector * (1.1 + radius / positionVector.mag), text=str(i + 1), opacity=0, box=False)
        vertices.append(sphere(pos=positionVector, radius=radius,
                               color=vec(rand.random(), rand.random(), rand.random())))

    result = np.where(graph_by_matrix != 0)
    listaa = np.sort(list(zip(result[0], result[1])))
    if len(listaa) > 0:
        z = [tuple(i) for i in np.unique(listaa, axis=0)]

        for (first, second) in z:
            line_axis = (vertices[second].pos - vertices[first].pos)
            line_axis_normalized = line_axis.norm()

            rand_color = vec(rand.random(), rand.random(), rand.random())

            label(pos=vertices[first].pos + line_axis_normalized * line_axis.mag / 2,
                  opacity=1.0,
                  text=str(graph_by_matrix[first][second]),
                  background=rand_color,
                  box=False)
            arrow(pos=vertices[second].pos - 1.9 * radius * line_axis_normalized,
                  axis=line_axis_normalized,
                  length=radius,
                  color=rand_color)

            curve(vertices[first].pos, vertices[second].pos, color=rand_color)
    # window.capture("letnie_dranie_graph")
