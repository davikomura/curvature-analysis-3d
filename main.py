import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import numpy as np
from geometry.surfaces import (
    sphere, torus, helicoid,
    hyperbolic_paraboloid, elliptic_paraboloid, enneper
)
from geometry.differential_geometry import (
    first_fundamental_form, second_fundamental_form,
    curvatures, partials, normals
)
from visualization.plot_surface_with_curvature import plot_surface_with_curvature

SURFACES = {
    "sphere": sphere.parametrize_sphere,
    "torus": torus.parametrize_torus,
    "helicoid": helicoid.parametrize_helicoid,
    "hyperbolic_paraboloid": hyperbolic_paraboloid.parametrize_hyperbolic_paraboloid,
    "elliptic_paraboloid": elliptic_paraboloid.parametrize_elliptic_paraboloid,
    "enneper": enneper.parametrize_enneper
}

CURVATURES = {
    "gaussian": curvatures.compute_gaussian_curvature,
    "mean": curvatures.compute_mean_curvature,
    "k1": lambda E, F, G, L, M, N: curvatures.compute_principal_curvatures(
        curvatures.compute_mean_curvature(E, F, G, L, M, N),
        curvatures.compute_gaussian_curvature(E, F, G, L, M, N)
    )[0],
    "k2": lambda E, F, G, L, M, N: curvatures.compute_principal_curvatures(
        curvatures.compute_mean_curvature(E, F, G, L, M, N),
        curvatures.compute_gaussian_curvature(E, F, G, L, M, N)
    )[1],
    "kn": curvatures.compute_normal_curvature
}

def choose_option(options, prompt):
    print(f"\n{prompt}")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return list(options.values())[choice]

def main():
    print("=== Curvature Analysis on 3D Surfaces ===")

    surface_func = choose_option(SURFACES, "Choose a surface:")
    curvature_func = choose_option(CURVATURES, "Choose a curvature:")
    plot_title = input("\nEnter the plot title: ")

    def surface():
        return surface_func()

    def curvature():
        x, y, z, u, v = surface_func()
        Xu, Xv = partials.compute_partials(x, y, z, u, v)
        n = normals.compute_normals(Xu, Xv)
        E, F, G = first_fundamental_form.compute_first_fundamental_form(Xu, Xv)
        L, M, N = second_fundamental_form.compute_second_fundamental_form(x, y, z, u, v, n)
        return curvature_func(E, F, G, L, M, N)

    plot_surface_with_curvature(surface, curvature, resolution=150, plot_title=plot_title)

if __name__ == "__main__":
    main()
