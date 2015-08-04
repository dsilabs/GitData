""" kml extractor
"""

from .. import Extractor

class KmlExtractor(Extractor):

    def can_extract(self, target, raw_data):
        path = str(target['path']).lower()
        return path.endswith('.kml') or path.endswith('.kmz')

    def extract(self, target, data):
        return [('kml', 'here is the data!')]

