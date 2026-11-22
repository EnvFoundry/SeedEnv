"""Physical coordinates of a synthetic volume and label-preserving resampling."""
import json
import SimpleITK as sitk

image = sitk.Image([8, 10, 12], sitk.sitkUInt8)
image.SetSpacing((0.5, 1.0, 2.0))
image.SetOrigin((10.0, -5.0, 3.0))
index = (3, 4, 5)
image[index] = 1
point = image.TransformIndexToPhysicalPoint(index)
output = sitk.Resample(image, image, sitk.Transform(3, sitk.sitkIdentity), sitk.sitkNearestNeighbor)
print(json.dumps({'data':'synthetic mask', 'index':index, 'physical_point':point,
                  'resampled_label':int(output[index])}))
assert point == (11.5, -1.0, 13.0) and output[index] == 1
