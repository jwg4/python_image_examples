import sys
import inspect

from .helpers.image import LazyImage


cameraman = LazyImage("hlevkin/cameraman.bmp")
fishing_boat = LazyImage("usc_misc/boat.512.tiff")
mandrill = LazyImage("usc_misc/4.2.03.tiff")
peppers = LazyImage("usc_misc/4.2.07.tiff")
phantom = LazyImage("Shepp_logan.png")

try:
    module = sys.modules[__name__]
    members = inspect.getmembers(module)

    metadata = {
        name: obj.comment
        for name, obj in members
        if isinstance(obj, LazyImage)
    }
except:
    pass