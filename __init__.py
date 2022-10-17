# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from .btm_pnl import BTSP
from .btm_op import MyProperties, BtspSend,BtspReImport
from .btm_preferences import BTM_AddonPreferences

import bpy
bl_info = {
    "name": "btsp",
    "author": "hyc",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "Object"
}


fbxname = r'C:\Users\HYC\Documents\maya\btm\btm.fbx'

class btm(bpy.types.Operator):
    bl_idname = "triangle.btm"
    bl_label = 'btm'

    def execute(self, context):
        a = bpy.ops.export_scene.fbx(filepath=fbxname, check_existing=True, filter_glob='*.fbx', use_selection=True, use_active_collection=False, global_scale=1.0, apply_unit_scale=True, apply_scale_options='FBX_SCALE_NONE', use_space_transform=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'}, use_mesh_modifiers=True, use_mesh_modifiers_render=True, mesh_smooth_type='OFF', use_subsurf=False, use_mesh_edges=False, use_tspace=False,
                                     use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=False, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True, axis_forward='-Z', axis_up='Y')
        print(a)
        return {"FINISHED"}


class mtb(bpy.types.Operator):
    bl_idname = "triangle.mtb"
    bl_label = 'mtb'

    def execute(self, context):
        bpy.ops.object.delete(use_global=False)
        a = bpy.ops.import_scene.fbx(filepath=fbxname)
        obj_objects = bpy.context.selected_objects[:]  # 获取导入对象集合
        for i in obj_objects:
            bpy.context.view_layer.objects.active = i  # 设置导入对象为活动对象
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
            bpy.context.object.data.use_auto_smooth = True  # 设置自动法线
            bpy.ops.object.material_slot_remove()  # 移除活动对象材质球
        return {"FINISHED"}


# classes = [mtb, btm, btsp, tests, BTM, MyProperties]
classes = [ mtb,
            btm,
            BTSP,
            BtspReImport,
            BtspSend, 
            MyProperties, 
            BTM_AddonPreferences]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperties)
    print('hello')


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.my_tool
    print('bye')
