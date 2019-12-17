import os

from pkg_resources import resource_filename


class LazyImage():
    def __init__(self, relname):
        self.relname = relname

    @property
    def _internal_name(self):
        return os.path.join('data', self.relname)

    @property
    def filename(self):
        return resource_filename('image_examples', self._internal_name)
