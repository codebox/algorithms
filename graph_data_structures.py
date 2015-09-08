class DirectedAdjacencyMatrix:
    def __init__(self, n):
        self.n = n
        self.data = [[0] * n for i in range(n)]

    def connect(self, i_from, i_to):
        self.data[i_from][i_to] += 1

    def disconnect(self, i_from, i_to):
        self.data[i_from][i_to] = max(0, self.data[i_from][i_to] - 1)

    def are_connected(self, n1, n2):
        return self.data[n1][n2] > 0 or self.data[n2][n1] > 0

    def get_outgoing(self, i_from):
        return [i for i in range(self.n) if self.data[i_from][i]]

    def get_incoming(self, i_to):
        return [i for i in range(self.n) if self.data[i][i_to]]
