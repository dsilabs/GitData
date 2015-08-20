""" geojson extractor
"""

from .. import Extractor
import geojson

class GeoJsonExtractor(Extractor):

    def can_extract(self, target, raw_data):
        return target['lpath'].endswith('json')

    def extract(self, target, data):
        t = data.read()
        try:
            data = geojson.loads(t)
        except:
            # possibly malformed json?
            start = min(t.find('{'), t.find('['))
            data = geojson.loads(t[start:])
        result = geojson.is_valid(data)
        if result['valid'] == 'yes':
            return [('geojson', data)]

