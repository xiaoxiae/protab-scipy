#!/usr/bin/env python3
# Konverze seznamu zastávek z Otevřených dat hl. m. Prahy:
# https://www.geoportalpraha.cz/cs/data/otevrena-data/seznam

import csv
import json
from pyproj import CRS, Transformer
import sys


with open('DOP_PID_ZAST_POPIS_B.json') as f:
    js = json.load(f)

wgs84 = CRS('WGS 84')
utm = CRS('WGS 84 / UTM zone 33N')
xfrm = Transformer.from_crs(wgs84, utm)

csv_out = csv.writer(sys.stdout, delimiter=';')

for feat in js['features']:
    lat, lon = feat['geometry']['coordinates']
    prop = feat['properties']
    east, north = xfrm.transform(lon, lat)
    csv_out.writerow([
        prop['ZAST_NAZEV'],
        prop['ZAST_OBEC'],
        prop['ZAST_PASMO'],
        east,
        north,
    ])
