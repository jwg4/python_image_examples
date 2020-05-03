import os

from pkg_resources import resource_filename


class LazyImage():
    def __init__(self, relname, alias, comment=None):
        self.relname = relname
        self._alias = alias
        self._comment = comment

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
    def data(self):
        with open(self.filename, 'rb') as f:
            return f.read()
