"""Compose supplied coordinate transforms. No robot or calibration is assumed."""
import json
import numpy as np
from pytransform3d.transform_manager import TransformManager
from pytransform3d.transformations import transform_from, transform

frames = TransformManager()
frames.add_transform('sample', 'tool', transform_from(np.eye(3), [0.01, 0.02, 0.03]))
frames.add_transform('tool', 'base', transform_from(np.eye(3), [0.1, 0.2, 0.3]))
sample_origin = np.array([0., 0., 0., 1.])
in_base = transform(frames.get_transform('sample', 'base'), sample_origin)
returned = transform(frames.get_transform('base', 'sample'), in_base)
np.testing.assert_allclose(in_base[:3], [.11, .22, .33])
np.testing.assert_allclose(returned, sample_origin, atol=1e-12)
print(json.dumps({'mode': 'supplied_transforms', 'sample_origin_in_base_m': in_base[:3].tolist()}))
