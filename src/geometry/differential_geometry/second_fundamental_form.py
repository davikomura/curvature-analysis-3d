import numpy as np

def compute_second_fundamental_form(x, y, z, u, v, normals):
    
    x_u, x_v = np.gradient(x, u, v, edge_order=2)
    y_u, y_v = np.gradient(y, u, v, edge_order=2)
    z_u, z_v = np.gradient(z, u, v, edge_order=2)

    x_uu, x_uv = np.gradient(x_u, u, v, edge_order=2)
    y_uu, y_uv = np.gradient(y_u, u, v, edge_order=2)
    z_uu, z_uv = np.gradient(z_u, u, v, edge_order=2)

    x_vu, x_vv = np.gradient(x_v, u, v, edge_order=2)
    y_vu, y_vv = np.gradient(y_v, u, v, edge_order=2)
    z_vu, z_vv = np.gradient(z_v, u, v, edge_order=2)

    Xuu = np.stack((x_uu, y_uu, z_uu), axis=-1)
    Xuv = np.stack((x_uv, y_uv, z_uv), axis=-1)
    Xvv = np.stack((x_vv, y_vv, z_vv), axis=-1)

    L = np.einsum('ijk,ijk->ij', normals, Xuu)
    M = np.einsum('ijk,ijk->ij', normals, Xuv)
    N = np.einsum('ijk,ijk->ij', normals, Xvv)

    return L, M, N
