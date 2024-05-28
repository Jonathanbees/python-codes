import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    """
    This is an implementation of the pseudo-code provided in the Wikipedia article.
    Arguments:
        A: nxn numpy matrix.
        b: n dimensional numpy vector.
        omega: relaxation factor.
        initial_guess: An initial solution guess for the solver to start with.
        convergence_criteria: The maximum discrepancy acceptable to regard the current solution as fitting.
    Returns:
        phi: solution vector of dimension n.
    """
    phi = initial_guess[:]
    residual = np.linalg.norm(np.matmul(A, phi) - b) #Initial residual
    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
        print('Residual: {0:10.6g}'.format(residual))
    return phi

# An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-8
omega = 0.5 #Relaxation factor

A = np.matrix([[4, -1, -6, 0],
              [-5, -4, 10, 8],
              [0, 9, 4, -2],
              [1, 0, -7, 5]])

b = np.matrix([2, 21, -12, -6])

initial_guess = np.zeros(4)

phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print(phi)