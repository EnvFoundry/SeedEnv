"""Exchange a silicon structure between ASE and pymatgen."""
import json
from ase.build import bulk
from pymatgen.io.ase import AseAtomsAdaptor

atoms=bulk("Si", "diamond", a=5.43)
structure=AseAtomsAdaptor.get_structure(atoms)
print(json.dumps({"formula":structure.formula, "sites":len(structure), "volume_angstrom3":structure.volume}))
