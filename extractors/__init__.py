
from _web import WebExtractor as web
from _csv import CsvExtractor as csv
from _json import JsonExtractor as json
from _html import HtmlExtractor as html
from _zipfile import ZipExtractor as zipfile
from _kml import KmlExtractor as kml
from _xml import XmlExtractor as xml

extractors = [
        # APIs
        #twitter(),

        # connectors
        web(),
        #ftp(),
        #sftp(),

        # parsers
        csv(),
        zipfile(),
        json(),
        kml(),
        html(),
        xml(),

        # databases
        #mysql(),
        #oracle(),
        ]

