# ASE Tests

## Summary

Testing the capabilities of ASE
Requires an installation of the Anaconda Python distribution

## Examples

### Initial Setup
Create the conda environment and install dependencies:
```
conda create -n ase -f conda-requirements.txt
conda activate ase
pip install -r pip-requirements.txt
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
