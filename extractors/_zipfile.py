""" zipfile extractor
"""

from .. import Extractor
import zipfile
from datetime import datetime

class ZipExtractor(Extractor):

    def can_extract(self, target, raw_data):
        return str(target['path']).lower().endswith('.zip')

    def extract(self, target, data):
        zfp = zipfile.ZipFile(data)
        if target['fragment']:
            return [('file', zfp.read(target.fragment))]
        else:
            zfp = zipfile.ZipFile(data)
            names = [['Filename', 'Size', 'Timestamp']]
            return [('zipfiles', names + [(
                f.filename,
                f.file_size,
                datetime(*f.date_time))
                for f in zfp.infolist()])]
