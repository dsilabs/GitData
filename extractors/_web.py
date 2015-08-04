""" web extractor
"""

from .. import Extractor
import requests
from StringIO import StringIO

class WebExtractor(Extractor):

    def collect(self, target):
        r = requests.get(target.url)
        if r.status_code == 200:
            return StringIO(r.content)

