

class Source(object):

    def __init__(self, kind, data):
        self.kind = kind
        self.data = data

    def __repr__(self):
        return self.kind #'<Source({self.kind!r}, data)>'.format(self=self)
        #return '<Source({self.kind!r}, data)>'.format(self=self)


class Extractor(object):
    reads = None

    def collect(self, target):
        pass

    def can_extract(self, target, data):
        pass

    def extract(self, target, data):
        pass

    def _views(self, source):
        pass

    def views(self, source):
        return (
            source.kind == self.reads and
            self._views(source) or []
        )

