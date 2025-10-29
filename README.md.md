# Binary Population Simulation and Gravitational Wave Merger Modelling

This project models a population of compact binary systems and estimates their gravitational-wave-driven merger times using the Peters (1964) formalism.  
It was developed as an extension of my MSc research at Queen Mary University of London.

## Contents
- `binary_population_simulation.py`: main Python script
- `results/`: figures produced by the simulation
- `docs/`: project report in LaTeX and PDF format

## Physics Summary
The merger time for two point masses is calculated from:
t_merge = (5/256) * c^5 * a^4 / (G^3 * m1 * m2 * (m1 + m2))

The script also computes the chirp mass and produces three plots:
1. Distribution of merger times
2. Chirp mass versus merger time
3. Component masses

## Requirements
Python 3.10 or newer, with:
- NumPy
- Matplotlib
- SciPy

Install with:

