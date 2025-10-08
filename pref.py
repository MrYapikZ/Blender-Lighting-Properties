import bpy
# ------------------------------------------------------------------------
# Navigation Properties
# ------------------------------------------------------------------------
class DataSettings(bpy.types.PropertyGroup):
    bpy.types.Scene.prop_key_filter = bpy.props.StringProperty(
        name="Custom Property Key",
        description="List objects that have this custom property key",
        default="blp",
    )

def register():
    bpy.utils.register_class(DataSettings)
    # bpy.types.Scene.pref_props = bpy.props.PointerProperty(type=DataSettings)
def unregister():
    bpy.utils.unregister_class(DataSettings)
    # del bpy.types.Scene.pref_props