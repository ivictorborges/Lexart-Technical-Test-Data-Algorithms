def create_cyclotron_matrix(size):
    return [[1 for _ in range(size)] for _ in range(size)]


def cyclotron(particle, size):
    if particle == "e":
        matrix = create_cyclotron_matrix(size)
        for i in range(1, size):
            matrix[i][i] = "e"
        return matrix

    elif particle == "p":
        matrix = create_cyclotron_matrix(size)
        for i in range(1, size):
            for j in range(1, size):
                if i == j:
                    matrix[i][j] = "p"
                elif i == size - 1 or j == size - 1:
                    matrix[i][j] = "p"
        return matrix

    elif particle == "n":
        matrix = create_cyclotron_matrix(size)
        for i in range(1, size):
            matrix[i][i] = "n"
        return matrix

    else:
        raise ValueError("Invalid particle type. Please use 'e', 'p', or 'n'.")
