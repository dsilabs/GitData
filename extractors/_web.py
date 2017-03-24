""" web extractor
"""

from .. import Extractor, Source
import requests
from StringIO import StringIO

class WebExtractor(Extractor):

    name = 'web'
    reads = 'url'

    def _views(self, source):
        r = requests.get(source.data.url)
        if r.status_code == 200:
            print 'web success: ', source.data.url
            return [
                Source('blob', StringIO(r.content))
            ]

    def extract(self, source):
        r = requests.get(source.url)
        if r.status_code == 200:
            print 'web success: ', source.url
            return [Source('blob', StringIO(r.content))]

    # legacy
    def collect(self, target):
        r = requests.get(target.url)
        if r.status_code == 200:
            return StringIO(r.content)

