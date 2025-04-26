import numpy as np

def compute_partials(x, y, z, u, v):
    
    x_u, x_v = np.gradient(x, u, v, edge_order=2)
    y_u, y_v = np.gradient(y, u, v, edge_order=2)
    z_u, z_v = np.gradient(z, u, v, edge_order=2)

    Xu = np.stack((x_u, y_u, z_u), axis=-1)
    Xv = np.stack((x_v, y_v, z_v), axis=-1)

    return Xu, Xv
