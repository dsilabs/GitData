""" json extractor
"""

from .. import Extractor, Source
import json

class JsonExtractor(Extractor):

    name = 'json'
    reads = 'blob'

    def extract(self, source):
        t = source.read()
        try:
            print 'json success'
            return [Source('json', json.loads(t))]
        except:
            # possibly malformed json?
            print 'json success (malformed)'
            start = min(t.find('{'), t.find('['))
            return [Source('json', json.loads(t[start:]))]

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

    def _views(self, source):
        t = source.data.read()
        try:
            print 'json success'
            return [Source('json', json.loads(t))]
        except:
            # possibly malformed json?
            print 'json success (malformed)'
            start = min(t.find('{'), t.find('['))
            return [Source('json', json.loads(t[start:]))]
