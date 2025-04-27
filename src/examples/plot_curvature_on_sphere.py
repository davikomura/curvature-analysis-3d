import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from geometry.surfaces.sphere import parametrize_sphere
from geometry.differential_geometry.first_fundamental_form import compute_first_fundamental_form
from geometry.differential_geometry.second_fundamental_form import compute_second_fundamental_form
from geometry.differential_geometry.curvatures import compute_gaussian_curvature
from visualization.plot_surface_with_curvature import plot_surface_with_curvature
from geometry.differential_geometry.partials import compute_partials
from geometry.differential_geometry.normals import compute_normals

def surface_func():
    return parametrize_sphere()

def curvature_func():
    x, y, z, u, v = parametrize_sphere()
    
    Xu, Xv = compute_partials(x, y, z, u, v)

    normals = compute_normals(Xu, Xv)
    
    E, F, G = compute_first_fundamental_form(Xu, Xv)
    L, M, N = compute_second_fundamental_form(x, y, z, u, v, normals)

    K = compute_gaussian_curvature(E, F, G, L, M, N)
    
    return K

if __name__ == "__main__":
    
    plot_surface_with_curvature(
        surface_func,
        curvature_func,
        resolution=100,
        plot_title="Gaussian Curvature on Sphere",
    )
