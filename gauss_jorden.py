import numpy as np

def gauss_jordan(A, B):
    # Augmenting matrix [A|B]
    augmented_matrix = np.hstack((A, B))

    # Perform Gaussian elimination
    for i in range(len(augmented_matrix)):
        # Partial pivoting
        pivot_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

        # Make diagonal elements non-zero
        pivot = augmented_matrix[i, i]
        if pivot != 0:
            augmented_matrix[i] /= pivot

        # Elimination
        for j in range(len(augmented_matrix)):
            if i != j:
                factor = augmented_matrix[j, i] / augmented_matrix[i, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    # Extracting solution matrix
    X = augmented_matrix[:, len(A):]

    return X

# Example usage:
A = np.array([[2, -1, 1],
              [3, 2, 1],
              [1, 1, 1]])
B = np.array([[2],
              [3],
              [4]])

solution_matrix = gauss_jordan(A, B)
print("Solution matrix:")
print(solution_matrix)
