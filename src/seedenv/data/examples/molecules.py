"""Calculate descriptors while retaining the input structure identifier."""
import json
from rdkit import Chem
from rdkit.Chem import Descriptors

smiles="CC(=O)Oc1ccccc1C(=O)O"
molecule=Chem.MolFromSmiles(smiles)
print(json.dumps({"smiles":smiles, "molecular_weight":Descriptors.MolWt(molecule),
                  "hbond_donors":Descriptors.NumHDonors(molecule), "hbond_acceptors":Descriptors.NumHAcceptors(molecule)}))
