""" json extractor
"""

from .. import Extractor
import json

class JsonExtractor(Extractor):

    def can_extract(self, target, raw_data):
        return target['lpath'].endswith('json')

    def extract(self, target, data):
        t = data.read()
        try:
            return [('json', json.loads(t))]
        except:
            # possibly malformed json?
            start = min(t.find('{'), t.find('['))
            return [('json', json.loads(t[start:]))]

