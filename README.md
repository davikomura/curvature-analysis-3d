# 3D Surface Curvature Analysis

## 📌 Overview

This project focuses on computing and visualizing the curvature properties of various 3D surfaces using Python. Leveraging libraries such as NumPy for numerical computations and Matplotlib for visualizations, the project delves into differential geometry concepts, including Gaussian curvature, mean curvature, and principal curvatures. The analysis encompasses a diverse set of surfaces to explore different curvature behaviors.

## 🧠 Objectives

- Implement mathematical representations of selected 3D surfaces.
- Calculate differential geometric properties: first and second fundamental forms, Gaussian curvature $(K)$, mean curvature $(H)$, and principal curvatures $(k_{1}, k_{2})$.
- Visualize surfaces with curvature-based color mappings.
- Analyze curvature distributions across different surface types.
- Ensure modularity and reusability of code components.

## 📁 Project Structure

```
3D-Curvature-Analysis/
├── data/                 
├── docs/                   
├── results/                
├── src/      
│   ├── examples/              
│   ├── geometry/           
│   │   ├── differential_geometry/
│   │   └── surfaces/              
│   └── visualization/      
├── tests/              
├── LICENSE 
├── main.py                
├── README.md       
└── requirements.txt             
```

## 🔍 Selected Surfaces

The project analyzes the following surfaces, chosen to represent a wide range of curvature characteristics:

1. **Sphere**: Constant positive Gaussian curvature.
2. **Elliptic Paraboloid**: Positive Gaussian curvature varying across the surface.
3. **Hyperbolic Paraboloid**: Negative Gaussian curvature throughout.
4. **Torus**: Regions with positive, negative, and zero Gaussian curvature.
5. **Enneper**: A minimal surface with self-intersecting properties, showcasing zero mean curvature and intricate geometry.
6. **Helicoid**: Another minimal surface with zero mean curvature.

## 🧮 Mathematical Foundations

For each surface, the following computations are performed:

- **First Fundamental Form**: The coefficients $ E $, $ F $, and $ G $ are derived from the dot products of the partial derivatives of the surface parametrization.
- **Second Fundamental Form**: The coefficients $ e $, $ f $, and $ g $ are computed using the surface normal vector and the second-order partial derivatives of the parametrization.
- **Normal Curvatures**: Curvatures in the direction of a given tangent vector, derived from the fundamental forms.
- **Gaussian Curvature ($K$)**: Defined as $K = \frac{eg - f^2}{EG - F^2}$, representing the intrinsic curvature of the surface.
- **Mean Curvature ($H$)**: Defined as $H = \frac{1}{2} \cdot \frac{eG - 2fF + gE}{EG - F^2}$, representing the average of the principal curvatures.
- **Principal Curvatures ($k_{1}$, $k_{2}$)**: The eigenvalues of the shape operator, derived from the fundamental forms, representing the maximum and minimum normal curvatures at a point.

## 📊 Visualization

The project employs advanced 3D plotting techniques to visualize curvature properties of surfaces. The visualizations are designed to provide an intuitive understanding of curvature distributions across various surface types.

### Visualization Features

- **Curvature-Based Coloring**: Surfaces are colored according to curvature values, with a customizable colormap to highlight variations effectively.
- **Edge Highlighting**: Surface edges are outlined to enhance visual clarity and structure.
- **Interactive Colorbar**: A colorbar is included to represent the range of curvature values, aiding in quantitative analysis.
- **Axes and Titles**: Each visualization includes labeled axes and descriptive titles for better interpretability.

### Visualization Outputs

The following types of visualizations are generated:

1. **Gaussian Curvature Mapping**: Displays the intrinsic curvature of surfaces, highlighting regions of positive, negative, or zero curvature.
2. **Mean Curvature Mapping**: Illustrates the average curvature, providing insights into surface bending behavior.
3. **Principal Curvature Directions**: Optionally visualizes the directions and magnitudes of principal curvatures for a deeper geometric analysis.

These visualizations serve as a powerful tool for exploring and analyzing the geometric properties of 3D surfaces, making complex curvature concepts more accessible and comprehensible.

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
- Gray, A. (1998). *Modern Differential Geometry of Curves and Surfaces with Mathematica*. CRC Press.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. 