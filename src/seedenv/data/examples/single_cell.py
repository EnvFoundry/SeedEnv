"""A synthetic count matrix; demonstrate data layers, not biological inference."""
import json
import numpy as np
import scanpy as sc
from anndata import AnnData

data = AnnData(np.random.default_rng(12).poisson(3, (40, 30)).astype(float))
data.layers['counts'] = data.X.copy()
sc.pp.normalize_total(data, target_sum=1e4)
sc.pp.log1p(data)
sc.pp.pca(data, n_comps=5)
sc.pp.neighbors(data, n_neighbors=5, n_pcs=5)
print(json.dumps({'data':'synthetic counts', 'cells':data.n_obs, 'genes':data.n_vars,
                  'pca_shape':list(data.obsm['X_pca'].shape),
                  'neighbor_edges':int(data.obsp['connectivities'].nnz)}))
assert data.obsm['X_pca'].shape == (40, 5)
assert np.all(data.layers['counts'] >= 0)
