# Quantum Tracking Demo

A micro demo for the CERN-HSF GSoC 2025 project "Sustainable Quantum Computing Algorithms for Particle Physics Reconstruction."

## Files
- `load_trackml.py`: Loads and visualizes a TrackML event.
- `qml_pipeline.py`: Implements a dummy PennyLane circuit with an Ising-like mapper.
- `benchmark.py`: Benchmarks time and energy usage for QML vs. classical loops.



1. Install dependencies: `pip install pandas numpy matplotlib trackml pennylane torch torch-geometric qiskit qiskit-aer`
2. Download TrackML data from [Kaggle](https://www.kaggle.com/competitions/trackml-particle-identification/data?select=train_sample.zip) and place in `data/`.
3. Run the scripts: `python load_trackml.py`, `python qml_pipeline.py`, `python benchmark.py`.

## Demo Results

### 3D Particle Hit Visualization
The `load_trackml.py` script visualizes 100 particle hits from a TrackML event in 3D:
![TrackML Event Visualization](screenshot.png)
## Setup<img width="961" alt="screenshot" src="https://github.com/user-attachments/assets/dd5d0253-1bff-41ab-98fd-72de79b4d387" />

### QML Circuit Output
The `qml_pipeline.py` script runs a dummy QML circuit:
- Example Output: `QML Circuit Output (Expectation Value): 0.560327712581222` (value varies due to random parameters)

### Benchmark Results
The `benchmark.py` script compares classical and QML loops:
- Classical Time: 0.0275 seconds
- QML Time: 0.0610 seconds
- Classical Energy (proxy): 11.151ms CPU time (via PyTorch Profiler)
- QML Energy (proxy): 0.0061 arbitrary units (scaled from time)

## Note
This is a simplified demo to showcase feasibility for GSoC. Energy benchmarking is a proxy due to limited hardware access.
