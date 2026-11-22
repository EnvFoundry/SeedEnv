"""H2 restricted Hartree-Fock in a minimal basis; illustrative, not chemical accuracy."""
import json
from pyscf import gto, scf, lib

lib.num_threads(1)
mol = gto.M(atom='H 0 0 0; H 0 0 0.74', unit='Angstrom', basis='sto-3g', spin=0, charge=0, verbose=0)
solver = scf.RHF(mol)
energy = solver.kernel()
print(json.dumps({'method':'RHF/STO-3G', 'bond_angstrom':0.74,
                  'energy_hartree':energy, 'converged':bool(solver.converged)}))
assert solver.converged and -1.2 < energy < -1.0
