bl_info = {
    "name": "PTP Lighting Properties",
    "description": "Lighting properties",
    "author": "MrYapikZ",
    "version": (0, 1, 0),
    "blender": (4, 5, 0),
}

import bpy
from . import ui, pref

ADDON_ID = __name__


# ------------------------------------------------------------------------
# Register
# ------------------------------------------------------------------------

modules = [
    pref,
    ui,
]


def register():
    for item in modules:
        item.register()


def unregister():
    for item in modules:
        item.unregister()