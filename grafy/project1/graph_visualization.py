import math
import random as rand
from typing import Tuple, List, Any

import numpy as np
from vpython import *


def __preparation(graph_by_matrix: np.ndarray, rfactor: float, radius: float) -> Tuple[
    List[Tuple[Any, Any]], List[sphere]]:
    canvas(width=1000, height=800)

    (vertexNumber, vertexNumber) = graph_by_matrix.shape

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
    return list(zip(result[0], result[1])), vertices


def visualize_weighted_graph(graph_by_matrix: np.ndarray, weighted_matrix: np.ndarray, digraph: bool = False) -> None:
    """Method to visualize weighted graph using vPython

        Parameters:
        graph_by_matrix (np.ndarray): graph given by matrix
        weighted_matrix (np.ndarray): weights of graph (in case of 0 weight)
        digraph (bool): flag to determine if graph is directed

        Returns:
        None

       """
    (vertexNumber, vertexNumber) = graph_by_matrix.shape

    rfactor = 40
    radius = -(1 / 4) * vertexNumber + 50

    listaa, vertices = __preparation(graph_by_matrix, rfactor, radius)

    if not digraph:
        listaa = np.sort(listaa)
    for (first, second) in listaa:
        line_axis = (vertices[second].pos - vertices[first].pos)
        line_axis_normalized = line_axis.norm()

        rand_color = vec(rand.random(), rand.random(), rand.random())
        label(pos=vertices[first].pos + line_axis_normalized * line_axis.mag * 2 / 3,
              opacity=1.0,
              text=str(weighted_matrix[first][second]),
              background=rand_color,
              box=False)
        if digraph:
            arrow(pos=vertices[second].pos - 1.9 * radius * line_axis_normalized,
                  axis=line_axis_normalized,
                  shaftwidth=20,
                  headwidth=40,
                  headlength=radius,
                  length=radius,
                  color=rand_color)

        curve(vertices[first].pos, vertices[second].pos, color=rand_color)


def visualize_graph(graph_by_matrix: np.ndarray, digraph: bool = False) -> None:
    """Method to visualize graph using vPython

        Parameters:
        graph_by_matrix (np.ndarray): graph given by matrix
        digraph (bool): flag to determine if graph is directed

        Returns:
        None

       """
    (vertexNumber, vertexNumber) = graph_by_matrix.shape

    rfactor = 40
    radius = -(1 / 4) * vertexNumber + 50

    listaa, vertices = __preparation(graph_by_matrix, rfactor, radius)
    if not digraph:
        listaa = np.sort(listaa)
    for (first, second) in listaa:
        line_axis = (vertices[second].pos - vertices[first].pos)
        line_axis_normalized = line_axis.norm()

        rand_color = vec(rand.random(), rand.random(), rand.random())
        if digraph:
            arrow(pos=vertices[second].pos - 1.9 * radius * line_axis_normalized,
                  axis=line_axis_normalized,
                  shaftwidth=20,
                  headwidth=40,
                  headlength=radius,
                  length=radius,
                  color=rand_color)

        curve(vertices[first].pos, vertices[second].pos, color=rand_color)
    # window.capture("letnie_dranie_graph")
