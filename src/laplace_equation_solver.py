import numpy as np

from src.fields import ScalarField

def matrice_aug(A):
    s = A.shape
    col = [[0]]*s[0]
    ligne = [0]*(s[1]+2)
    hor = np.hstack([col, A, col])
    ver = np.vstack([ligne, hor, ligne])
    return ver
class LaplaceEquationSolver:
    """
    A Laplace equation solver used to compute the resultant potential field P in 2D-space generated by a constant
    voltage field V (for example due to wires).
    """

    def __init__(self, nb_iterations: int = 10000):
        """
        Laplace solver constructor. Used to define the number of iterations for the relaxation method.

        Parameters
        ----------
        nb_iterations : int
            Number of iterations performed to obtain the potential by the relaxation method (default = 1000).
        """
        self.nb_iterations = nb_iterations

    def solve(self, constant_voltage: ScalarField) -> ScalarField:
        """
        Solve the Laplace equation to compute the potential field given a constant voltage field.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (x, y) → V(x, y), where V(x, y) is the wires' voltage at a given point (x, y)
            in space.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (x, y) → P(x, y), where P(x, y) is the electric potential at a given point
            (x, y) in space. The difference between P and V is that P gives the potential in the whole world, i.e in
            the wires and in the empty space between the wires, while the field V always gives V(x, y) = 0 if (x, y)
            is not a point belonging to an electric wire.
        """

        # Le code est ici 
        potential=np.zeros_like(constant_voltage)
        
        for _ in range (self.nb_iterations):
            new_potential = np.copy(potential)
    
            potential[1:-1,1:-1] = 1/4*(new_potential[:-2,1:-1] + potential[2 :, 1 : -1] + new_potential[1 : -1, : -2] + potential[ 1: -1, 2:])
            
            potential = np.where(constant_voltage != 0, constant_voltage, potential)
            
            M = potential
        return ScalarField(M)
