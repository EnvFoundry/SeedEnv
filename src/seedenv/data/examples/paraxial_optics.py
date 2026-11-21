"""One-to-one imaging with a thin lens, lengths in millimetres."""
import json
from raytracing import Lens, Space

system = Space(100) * Lens(50) * Space(100)
print(json.dumps({"matrix_ABCD": [[system.A, system.B], [system.C, system.D]],
                  "image_condition_B_mm": system.B, "magnification": system.A}))
