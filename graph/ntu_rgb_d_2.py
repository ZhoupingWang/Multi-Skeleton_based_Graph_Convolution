import sys
sys.path.insert(0, '')
sys.path.extend(['../'])

import numpy as np

from graph import tools

num_node = 25
self_link = [(i, i) for i in range(num_node)]
inward_ori_index = [(11, 9), (9, 15), (23, 15), (8, 23), (16, 15), (24, 16), (20, 24),
                    (17, 20), (4, 15), (2, 4), (21, 2), (1, 21), (5, 11),
                    (18, 5), (12, 18), (22, 12), (19, 11), (7, 19), (13, 7),
                    (3, 13), (25, 10), (10, 17), (6, 14), (14, 1)]
inward = [(i - 1, j - 1) for (i, j) in inward_ori_index]
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward


class AdjMatrixGraph:
    def __init__(self, *args, **kwargs):
        self.edges = neighbor
        self.num_nodes = num_node
        self.self_loops = [(i, i) for i in range(self.num_nodes)]
        self.A_binary = tools.get_adjacency_matrix(self.edges, self.num_nodes)
        self.A_binary_with_I = tools.get_adjacency_matrix(self.edges + self.self_loops, self.num_nodes)
        self.A = tools.normalize_adjacency_matrix(self.A_binary)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    graph = AdjMatrixGraph()
    A, A_binary, A_binary_with_I = graph.A, graph.A_binary, graph.A_binary_with_I
    f, ax = plt.subplots(1, 3)
    ax[0].imshow(A_binary_with_I, cmap='gray')
    ax[1].imshow(A_binary, cmap='gray')
    ax[2].imshow(A, cmap='gray')
    plt.show()
    print(A_binary_with_I.shape, A_binary.shape, A.shape)
