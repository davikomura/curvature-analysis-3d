# 3D Surface Curvature Analysis

## 📌 Overview

This project focuses on computing and visualizing the curvature properties of various 3D surfaces using Python. Leveraging libraries such as NumPy for numerical computations and Matplotlib for visualizations, the project delves into differential geometry concepts, including Gaussian curvature, mean curvature, and principal curvatures. The analysis encompasses a diverse set of surfaces to explore different curvature behaviors.

## 🧠 Objectives

- Implement mathematical representations of selected 3D surfaces.
- Calculate differential geometric properties: first and second fundamental forms, Gaussian curvature (K), mean curvature (H), and principal curvatures (k₁, k₂).
- Visualize surfaces with curvature-based color mappings.
- Analyze curvature distributions across different surface types.
- Ensure modularity and reusability of code components.

## 📁 Project Structure

```
3D-Curvature-Analysis/
├── data/                   # Auxiliary data (meshes, samples)
├── docs/                   # Project documentation
├── results/                # Generated outputs (images, graphs, files)
├── src/                    # Source code
│   ├── geometry/           # Mathematical functions (curvatures, parametrizations)
│   ├── utils/              # Auxiliary utilities (exports, transformations)
│   └── visualization/      # Graph and figure generation
├── tests/                  # Test scripts for implemented functions
├── main.py                 # Main execution script
├── requirements.txt        # Project dependencies
└── README.md               # Project description
```

## 🔍 Selected Surfaces

The project analyzes the following surfaces, chosen to represent a wide range of curvature characteristics:

1. **Sphere**: Constant positive Gaussian curvature.
2. **Cylinder**: Zero Gaussian curvature; non-zero mean curvature.
3. **Elliptic Paraboloid**: Positive Gaussian curvature varying across the surface.
4. **Hyperbolic Paraboloid**: Negative Gaussian curvature throughout.
5. **Torus**: Regions with positive, negative, and zero Gaussian curvature.
6. **Catenoid**: Minimal surface with zero mean curvature.
7. **Helicoid**: Another minimal surface with zero mean curvature.
8. **Ellipsoid**: Varying positive Gaussian curvature depending on direction.
9. **Hyperboloid of One Sheet**: Negative Gaussian curvature; ruled surface.

## 🧮 Mathematical Foundations

For each surface, the following computations are performed:

- **First Fundamental Form**: Coefficients E, F, G derived from partial derivatives of the parametrization.
- **Second Fundamental Form**: Coefficients e, f, g obtained using the surface normal and second-order partial derivatives.
- **Gaussian Curvature (K)**: Calculated as \( K = \frac{eg - f^2}{EG - F^2} \).
- **Mean Curvature (H)**: Calculated as \( H = \frac{1}{2} \cdot \frac{eG - 2fF + gE}{EG - F^2} \).
- **Principal Curvatures (k₁, k₂)**: Eigenvalues of the shape operator derived from the fundamental forms.

## 📊 Visualization

Utilizing Matplotlib's 3D plotting capabilities, the project visualizes:

- Surfaces colored based on Gaussian curvature values.
- Surfaces colored based on mean curvature values.
- Vector fields representing surface normals.
- Optional: Principal curvature directions and magnitudes.

## 🧪 Testing

The `tests/` directory contains scripts to validate:

- Accuracy of curvature computations against known analytical results.
- Consistency of normal vector calculations.
- Correctness of fundamental form implementations.

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/3D-Curvature-Analysis.git
   cd 3D-Curvature-Analysis
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the main script to perform curvature analysis:

```bash
python main.py
```

This will generate visualizations and save them in the `results/` directory.

## 📚 References

- do Carmo, M. P. (1976). *Differential Geometry of Curves and Surfaces*. Prentice-Hall.
- Pressley, A. (2010). *Elementary Differential Geometry*. Springer.
- O'Neill, B. (2006). *Elementary Differential Geometry*. Academic Press.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. 