"""Smooth a synthetic image and measure the segmented region."""
import json
import numpy as np
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label, regionprops

y,x=np.mgrid[:64,:64]
image=np.exp(-((x-32)**2+(y-32)**2)/120)
smoothed=gaussian(image,sigma=1)
regions=regionprops(label(smoothed>threshold_otsu(smoothed)))
print(json.dumps({"regions":len(regions), "area_pixels":[float(r.area) for r in regions]}))
