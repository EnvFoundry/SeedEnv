# Volume processing · 三维医学影像处理

Filter, resample and transform image volumes.

Use origin, spacing and direction cosines, not array shape alone, to interpret geometry. Apply label-preserving interpolation to masks and preserve physical coordinates in exported images.

三维影像的滤波、重采样与坐标变换。

几何含义由原点、间距和方向余弦共同确定。掩模采用保持标签的插值，导出影像保留物理坐标。

Software / 软件：SimpleITK (`python-simpleitk`).

Use `seedenv context volume-processing` for software entries and setup on this host.

- https://simpleitk.readthedocs.io/en/master/gettingStarted.html

Editable starting program / 可编辑起点：`seedenv example volume-processing --output research.py`.
