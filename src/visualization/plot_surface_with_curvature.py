import numpy as np
import matplotlib.pyplot as plt

def plot_surface_with_curvature(surface_func, curvature_func, resolution=100, cmap='coolwarm', plot_title='Surface with Curvature'):
    
    x, y, z, u, v = surface_func()
    curvature = curvature_func()

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    normalized_curvature = (curvature - curvature.min()) / (curvature.max() - curvature.min())

    surf = ax.plot_surface(
        x, y, z,
        rstride=1, cstride=1,
        facecolors=plt.cm.get_cmap(cmap)(normalized_curvature),
        linewidth=0.5,
        antialiased=True,
        shade=True
    )
    
    surf.set_edgecolor('k')

    m = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=curvature.min(), vmax=curvature.max()))
    m.set_array([])
    fig.colorbar(m, ax=ax, shrink=0.5, aspect=10, label='Curved')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(plot_title)
    plt.tight_layout()
    plt.show()
