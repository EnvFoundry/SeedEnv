"""Build a parameterized plate and through-hole using the full CAD API."""
import json
import cadquery as cq

shape=cq.Workplane("XY").box(20,10,2).faces(">Z").workplane().hole(3)
print(json.dumps({"volume_mm3":shape.val().Volume(), "solids":shape.solids().size()}))
