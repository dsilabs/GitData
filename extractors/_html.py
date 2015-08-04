""" html extractor
"""

from .. import Extractor
from bs4 import BeautifulSoup

class HtmlExtractor(Extractor):

    def can_extract(self, target, raw_data):
        path = str(target['path']).lower()
        return path.endswith('.html') or 'table' in raw_data

    def extract(self, target, stream):
        result = []
        stream.seek(0)
        soup = BeautifulSoup(stream)
        for table in soup.find_all('table'):
            t = []
            for row in table.find_all('tr'):
                r = []
                for cell in row.find_all('th'):
                    r.append(cell.text)
                for cell in row.find_all('td'):
                    r.append(cell.text)
                t.append(r)
            result.append(t)
        return [('tables',result)]
