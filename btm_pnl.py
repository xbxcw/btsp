from bpy.types import (Panel, AddonPreferences)


class BTSP(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BTSP'
    bl_label = 'send to sbp'
    bl_context = 'objectmode'

    def draw(self, context):
        scn = context.scene
        layout = self.layout

        # 贴图文件夹
        layout.prop(scn.my_tool, 'ImagePath', text='ImagePath')
        layout.prop(scn.my_tool, 'SP_Project_Path', text='SP_Project_Path')

        box = layout.box()
        row = box.row()

        row.operator('btsp.send',text='send')
        row.column().operator('btsp.reimport',text='reimport')

        layout.prop(scn.my_tool,'Image_format')

        box = layout.box()

        row = box.row()
        row.prop(scn.my_tool,'Bol_AO')
        row.column().prop(scn.my_tool,'AO_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_BentNormals')
        row.column().prop(scn.my_tool,'BentNormals_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_Curvature')
        row.column().prop(scn.my_tool,'Curvature_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_Height')
        row.column().prop(scn.my_tool,'Height_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_ID')
        row.column().prop(scn.my_tool,'ID_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_Normal')
        row.column().prop(scn.my_tool,'Normal_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_Opacity')
        row.column().prop(scn.my_tool,'Opacity_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_Position')
        row.column().prop(scn.my_tool,'Position_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_Thickness')
        row.column().prop(scn.my_tool,'Thickness_Suffix')

        row = box.row()
        row.prop(scn.my_tool,'Bol_WorldSpaceNormal')
        row.column().prop(scn.my_tool,'WorldSpaceNormal_Suffix')


















