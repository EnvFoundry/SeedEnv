"""Normal-incidence power reflection/transmission of a lossless film."""
import json
from tmm import coh_tmm

result=coh_tmm("s",[1.,1.38,1.52],[float("inf"),100.,float("inf")],0.,550.)
print(json.dumps({"wavelength_nm":550., "R":float(result["R"]), "T":float(result["T"]),
                  "R_plus_T":float(result["R"]+result["T"])}))
