"""A coordinate transform with explicit angular units."""
import json
from astropy.coordinates import SkyCoord
import astropy.units as u

coordinate=SkyCoord(ra=10*u.deg,dec=20*u.deg,frame="icrs").galactic
print(json.dumps({"frame":"galactic", "longitude_deg":coordinate.l.deg, "latitude_deg":coordinate.b.deg}))
