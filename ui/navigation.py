import bpy

# ------------------------------------------------------------------------
# Navigation Panel Properties
# ------------------------------------------------------------------------

def find_objects_by_key(key="blp"):
    override_objects = [obj for obj in bpy.data.objects if obj.override_library]
    return [o for o in override_objects if o.get(key)]

class NAV_PT_Panel(bpy.types.Panel):
    bl_label = "PTP Lighting Navigation"
    bl_idname = "NAV_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PTP_Lighting'
    bl_description = "Navigation panel for PTP Lighting Properties"

    def draw(self, context):
        layout = self.layout
        s = context.scene

        row = layout.row(align=True)
        # row.prop(s, "prop_key_filter", text="Key")
        row.operator("view3d.refresh_custom_prop_list", text="", icon="FILE_REFRESH")
        eevee = context.scene.eevee
        row.prop(eevee, "gtao_distance", text="AO Distance")

        key = s.prop_key_filter or "blp"
        objs = sorted(find_objects_by_key(key), key=lambda o: o.name.lower())

        layout.label(text=f"Found: {len(objs)}")
        col = layout.column(align=True)
        if not objs:
            col.label(text="No objects with that key.", icon='INFO')
        else:
            for o in objs:
                box = layout.box()
                box.label(text=f"{o.name}", icon='OBJECT_DATA')

                # If it's a light, show its energy slider
                if o.type == 'LIGHT':
                    box.prop(o.data, "color", text="Color")
                    box.prop(o.data, "energy", text="Energy")
                    box.prop(o.data, "exposure", text="Exposure")
                    box.prop(o.data, "shadow_jitter_overblur", text="Shadow Jitter")
                else:
                    box.label(text="Not a Light object.", icon='ERROR')
                    box.label(text="Energy control is only available for lights.")
# ------------------------------------------------------------------------
# Register
# ------------------------------------------------------------------------
def register():
    bpy.utils.register_class(NAV_PT_Panel)

def unregister():
    bpy.utils.unregister_class(NAV_PT_Panel)