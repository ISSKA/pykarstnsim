# PyKarstNSim

A Python interface for the [KarstNSim](https://github.com/ring-team/KarstNSim_Public) C++ library, enabling graph-based and geologically-driven simulation of 3D karst networks directly from Python.

## About

PyKarstNSim provides Python bindings to KarstNSim, a powerful tool for simulating realistic karst network geometries. This package is based on a [fork](https://github.com/ISSKA/KarstNSim_Public) of the original [KarstNSim_Public](https://github.com/ring-team/KarstNSim_Public) repository developed by the RING team. Both repositories are kept in sync on a best-effort basis.

### Credits

KarstNSim was originally developed by:

- **Augustin Gouy** (PhD development, 2022-2025)
- **Benoît Thébault** (initial implementation, 2022)
- Supervised by **Pauline Collon** and **Vincent Bailly-Comte**

The methodology adapts the karst synthesis approach from:

> Paris, A., Guérin, E., Peytavie, A., Collon, P., Galin, E., 2021. _Synthesizing Geologically Coherent Cave Networks_. Comput. Graph. Forum 40, 277–287. https://doi.org/10.1111/cgf.14420

### Citation

If you use this package, please cite the original KarstNSim publication:

```bibtex
@article{Gouy2024,
    author = {Gouy, Augustin and Collon, Pauline and Bailly-Comte, Vincent and Galin, Eric and Antoine, Christophe and Thebault, Benoît and Landrein, Philippe},
    doi = {10.1016/j.jhydrol.2024.130878},
    journal = {Journal of Hydrology},
    title = {{KarstNSim: A graph-based method for 3D geologically-driven simulation of karst networks}},
    year = {2024}
}
```

## Installation

### Using [uv](https://docs.astral.sh/uv/) (recommended)

```bash
uv add git+https://github.com/ISSKA/pykarstnsim.git
```

### Using pip

```bash
pip install git+https://github.com/ISSKA/pykarstnsim.git
```

## Usage

See the [pykarstnsim-demo](https://github.com/ISSKA/pykarstnsim-demo) repository for working examples and tutorials.

## Documentation

For detailed information about:

- **Simulation methodology**: See the [2024 publication](https://doi.org/10.1016/j.jhydrol.2024.130878) and [2025 thesis](https://hal.univ-lorraine.fr/tel-05114757v1)
- **Input parameters and configuration**: Refer to the [config reference](https://github.com/ISSKA/KarstNSim_Public/blob/main/config_reference.md) in the C++ repository
- **Algorithm details**: Consult the full [KarstNSim documentation](https://github.com/ring-team/KarstNSim_Public)

## Requirements

- Python >= 3.9
- NumPy >= 2.0.2

## Contributing

Contributions are welcome! To set up a development environment:

### Using uv (recommended)

```bash
git clone https://github.com/ISSKA/pykarstnsim.git
cd pykarstnsim
uv sync
```

### Using pip

```bash
git clone https://github.com/ISSKA/pykarstnsim.git
cd pykarstnsim
pip install -e .
```

## License

See [LICENSE](LICENSE) file for details. License is shared with the original KarstNSim C++ library.

## Contact

For issues specific to the Python bindings, please open an issue on this repository.

For questions about the underlying KarstNSim methodology:

- Augustin Gouy: a.gouy.proaddress@gmail.com
- Pauline Collon: pauline.collon@univ-lorraine.fr
