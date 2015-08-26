""" kml extractor
"""

import tempfile, StringIO
from osgeo import ogr
from .. import Extractor
import json
import ogr2ogr
import geojson

def kmltogeojson(data):
    out = StringIO.StringIO()

    temp = tempfile.NamedTemporaryFile()
    temp.write(data.read())
    temp.flush()

    outname = temp.name + '.geojson'

    result = ogr2ogr.main(["", "-f", "GeoJSON", outname, temp.name])
    if result == True:
        return open(outname).read()


class KmlExtractor(Extractor):

    def can_extract(self, target, raw_data):
        path = str(target['path']).lower()
        return path.endswith('.kml') or path.endswith('.kmz')

    def extract(self, target, data):
        s = kmltogeojson(data)
        if s:
            data = geojson.loads(s)
            result = geojson.is_valid(data)
            if result['valid'] == 'yes':
                return [('geojson', data)]
