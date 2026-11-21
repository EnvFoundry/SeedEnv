"""Lossless dielectric slab: a starting RCWA model with explicit physical scale."""
import json
import grcwa

# Lengths are in micrometres; c=1, so frequency is inverse wavelength.
model = grcwa.obj(nG=11, L1=[0.5, 0], L2=[0, 0.5], freq=1 / 1.55, theta=0, phi=0, verbose=0)
model.Add_LayerUniform(0, 1)
model.Add_LayerUniform(0.2, 2.25)
model.Add_LayerUniform(0, 1)
model.Init_Setup()
model.MakeExcitationPlanewave(p_amp=0, p_phase=0, s_amp=1, s_phase=0, order=0)
reflection, transmission = model.RT_Solve(normalize=1)
print(json.dumps({"R": float(reflection), "T": float(transmission),
                  "R_plus_T": float(reflection + transmission)}))
