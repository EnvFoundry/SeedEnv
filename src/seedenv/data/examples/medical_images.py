"""Keep spatial meaning when constructing an example NIfTI volume."""
import json
import nibabel as nib
import numpy as np

volume=np.zeros((16,16,8),dtype=np.float32)
volume[4:12,4:12,2:6]=1
image=nib.Nifti1Image(volume,np.diag([.8,.8,2.,1.]))
print(json.dumps({"shape":list(image.shape), "voxel_size_mm":list(map(float,image.header.get_zooms())),
                  "axis_codes":list(nib.aff2axcodes(image.affine)), "nonzero_voxels":int(np.count_nonzero(volume))}))
