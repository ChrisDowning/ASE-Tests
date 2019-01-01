# ASE Tests

## Summary

Testing the capabilities of ASE
Requires an installation of the Anaconda Python distribution

## Examples

### Setup
Create the conda environment (first run only):
```
conda env create -f environment.yml
```

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
