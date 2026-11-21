"""Transform coordinates while preserving the coordinate reference system."""
import json
import geopandas as gpd

points=gpd.GeoSeries(gpd.points_from_xy([120.15,120.20],[30.25,30.30]),crs="EPSG:4326")
projected=points.to_crs("EPSG:3857")
print(json.dumps({"crs":str(projected.crs), "xy_m":[[p.x,p.y] for p in projected]}))
