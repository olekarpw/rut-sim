# RUT-SIM: Resonant Universe Theory Simulation Suite (v5.3)

Python simulation tools for verifying the geometric framework of the **Resonant Universe Theory (RUT)**.

## Overview
This repository contains reference computational modules for testing phase stability, topological generation limits, and standard model mixing parameters within the 6D phase space model of RUT 5.3.

## Modules Included
* `sci.py`: Calculates the vacuum phase attractor ($\Psi_p \approx 77.638^\circ$), fine-structure constant relations ($\alpha \approx 1/137.036$), and fundamental fermion mass spectra.
* `soliton_3d.py`: 3D topology projections of 6D toroidal solitons, demonstrating topological phase breakdown for generations $n \ge 4$.
* `mixing_matrices.py`: Derivation of Cabibbo angle (CKM) and PMNS neutrino mixing angles from vacuum phase geometry.
* `main.py`: Unified CLI suite manager.

## Quick Start
```bash
# Clone repository
git clone [https://github.com/olekarpw/rut-sim.git](https://github.com/olekarpw/rut-sim.git)
cd rut-sim

# Install dependencies
pip install numpy matplotlib scipy

# Run simulation suite
python3 main.py
