class LazyImage():
    def __init__(self, relname):
        self.relname = relname

    @property
    def filename(self):
        return self.relname
