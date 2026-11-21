"""Solve -Laplacian(u)=1 with zero boundary values on a square."""
import json
from skfem import MeshTri, Basis, ElementTriP1, asm, condense, solve
from skfem.models.poisson import laplace, unit_load

mesh=MeshTri().refined(3)
basis=Basis(mesh,ElementTriP1())
solution=solve(*condense(asm(laplace,basis),asm(unit_load,basis),D=basis.get_dofs()))
print(json.dumps({"dofs":int(basis.N), "maximum_u":float(solution.max()), "boundary_max":float(abs(solution[basis.get_dofs().all()]).max())}))
