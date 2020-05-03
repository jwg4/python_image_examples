import os

from pkg_resources import resource_filename


class LazyImage():
    def __init__(self, relname, alias=None, comment=None):
        self.relname = relname
        self._alias = alias
        self._comment = comment
        self._raw = None

    @property
    def alias(self):
        return self._alias


    @property
    def _internal_name(self):
        return os.path.join('data', self.relname)

    @property
    def filename(self):
        return resource_filename('image_examples', self._internal_name)

    @property
    def comment(self):
        if self._comment:
            return self._comment
        return "File: %s" % (self._internal_name, )

    @property
    def raw(self):
        if self._raw is None:
            with open(self.filename, 'rb') as f:
                self._raw = f.read()
        return self._raw
    
    @property
    def data(self):
        return bytearray(self.raw)
