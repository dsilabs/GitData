""" xml extractor
"""

from .. import Extractor
import csv

class XmlExtractor(Extractor):

    def can_extract(self, target, raw_data):
        return str(target['path']).lower().endswith('.csv')

    def extract(self, target, data):
        rows = []
        reader = csv.reader(data, delimiter=",", quotechar='"')
        for row in reader:
            rows.append(row)
        return [('rows', rows)]

