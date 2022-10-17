import bpy

from bpy.types import (Operator,
                       Menu,
                       Panel,
                       PropertyGroup,
                       UIList,
                       AddonPreferences)
from bpy.props import (BoolProperty,
                       EnumProperty,
                       FloatProperty,
                       IntProperty,
                       PointerProperty,
                       CollectionProperty,
                       StringProperty)


class BTM_AddonPreferences(AddonPreferences):
    bl_idname = __package__
    
    def draw(self, context):
        layout = self.layout
        # layout.label(text='sssssssssss')

        scn = context.scene
        layout.prop(scn.my_tool, 'SubstancePath', text='SubstancePainter')

