"""Symmetry-reduced displacements for an illustrative silicon structure."""
import json
import numpy as np
from phonopy import Phonopy
from phonopy.structure.atoms import PhonopyAtoms

unitcell = PhonopyAtoms(symbols=['Si', 'Si'], scaled_positions=[[0, 0, 0], [0.25, 0.25, 0.25]],
                       cell=np.array([[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]]) * 5.43)
phonon = Phonopy(unitcell, supercell_matrix=np.diag([2, 2, 2]))
phonon.generate_displacements(distance=0.01)
cells = phonon.supercells_with_displacements
print(json.dumps({'structure':'illustrative silicon', 'supercell_atoms':len(phonon.supercell),
                  'displaced_supercells':len(cells), 'displacement_angstrom':0.01,
                  'next':'Evaluate forces for these supercells before constructing force constants.'}))
assert len(phonon.supercell) == 16 and len(cells) > 0
