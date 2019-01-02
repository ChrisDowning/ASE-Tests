# ASE Tests

## Summary

Testing the capabilities of ASE

Uses a local setup of ASE via pip, in a Conda environment

## Examples

### Initial Setup

Enter the environment:
```
conda activate ase
```

### PtAu Example

Enter the PtAu directory:
```
cd PtAu
```

Run the test case (Pt<sub>7</sub> above an Au slab):
```
python PtAu.py
```

Inspect the trajectory and play with the GUI:
```
ase gui PtAu.traj
```

### Exiting

Leave the conda environment:
```
conda deactivate
```
