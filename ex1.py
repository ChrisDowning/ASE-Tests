from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.build import fcc111, add_adsorbate

h = 6.00
b = 1.50

slab = fcc111('Au', size=(10, 10, 6), vacuum=20.0)

slab.set_calculator(EMT())
e_slab = slab.get_potential_energy()

molecule = Atoms('Pt7', positions=[(0., 0., 0.), (0., 0., b), (0., 0., -b), (b, 0., 0.), (-b, 0., 0.), (0., b, 0.), (0., -b, 0.)])
molecule.set_calculator(EMT())
e_Pt = molecule.get_potential_energy()

add_adsorbate(slab, molecule, h, 'ontop')
constraint = FixAtoms(mask=[a.symbol != 'Pt' for a in slab])
slab.set_constraint(constraint)
dyn = QuasiNewton(slab, trajectory='PtAu.traj')
dyn.run(fmax=0.05)

print('Adsorption energy:', e_slab + e_Pt - slab.get_potential_energy())
