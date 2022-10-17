from ast import Not, operator
import time
import bpy
import os
import subprocess
from .lib_remote import *
from .func import create_directory
from bpy.types import PropertyGroup, Operator
from bpy.props import StringProperty,BoolProperty,EnumProperty
remote = RemotePainter()

class MyProperties(PropertyGroup):
    items = [('.PSD', '.psd', ''),
            ('.PNG', 'png', ''),
            ('.TGA', 'tga', '')]
    SubstancePath: StringProperty(
        name="",
        description="Path to Directory",
        default="C:\Program Files\Adobe\Adobe Substance 3D Painter\Adobe Substance 3D Painter.exe",
        maxlen=1024,
        subtype='FILE_PATH')
    ImagePath: StringProperty(
        name="",
        description="贴图文件夹",
        default="//marmoset\MT_Output\'",
        maxlen=1024,
        subtype='DIR_PATH')

    SP_Project_Path: StringProperty(
        name="",
        description="sp 项目 路径",
        default='//sp\"',
        maxlen=1024,
        subtype='DIR_PATH')

    Image_format: EnumProperty(name='format',items=items)

    Bol_AO: BoolProperty(name='AO',default=True)
    AO_Suffix: StringProperty(default='_ao')

    Bol_BentNormals: BoolProperty(name='BentNormals')
    BentNormals_Suffix: StringProperty(default='_bentnormal')

    Bol_Curvature: BoolProperty(name='Curvature')
    Curvature_Suffix: StringProperty(default='_curve')

    Bol_Height: BoolProperty(name='Height')
    Height_Suffix: StringProperty(default='_height')

    Bol_ID: BoolProperty(name='ID')
    ID_Suffix: StringProperty(default='_id')

    Bol_Normal: BoolProperty(name='Normal',default=True)
    Normal_Suffix: StringProperty(default='_normal')

    Bol_Opacity: BoolProperty(name='Opacity')
    Opacity_Suffix: StringProperty(default='_opacity')

    Bol_Position: BoolProperty(name='Position')
    Position_Suffix: StringProperty(default='_position')

    Bol_Thickness: BoolProperty(name='Thickness')
    Thickness_Suffix: StringProperty(default='_thickness')

    Bol_WorldSpaceNormal: BoolProperty(name='WorldSpaceNormal')
    WorldSpaceNormal_Suffix: StringProperty(default='_normalobj')





class BtspSend(Operator):

    bl_description = 'send to sp'
    bl_idname = "btsp.send"
    bl_label = 'btsp'

    def execute(self, context):
        scn = context.scene
        substance_path = scn.my_tool.SubstancePath+' --enable-remote-scripting'
        
        file_name = bpy.path.basename(bpy.data.filepath)

        create_directory(bpy.path.abspath(scn.my_tool.ImagePath))
        spp_project = create_directory(bpy.path.abspath(scn.my_tool.SP_Project_Path))
        fbx_dir = create_directory(bpy.path.abspath(scn.my_tool.SP_Project_Path+'fbx'))
        fbxname = os.path.join(fbx_dir,file_name.replace('blend','fbx'))
        
        self.export_fbx(fbxname)
        materials = self.get_selected_materials()
        texture_set, maps = self.create_py(scn,materials)
        self.run_sbp(substance_path)

        spp = os.path.join(spp_project,file_name.replace('.blend','.spp'))
        self.create_sp(fbxname,maps,spp)

        self.create_texture_set(texture_set)

        # print(texture_set)
        return {"FINISHED"}

    def run_sbp(self,substance_path):
        '''
        启动substance painnter
        '''
        b = ''
        try:
            b = remote.execScript('print("hello world")')
            print('bbbbbbbbbbbbb')
        except:
            a = subprocess.Popen(substance_path)
            try:
                b = remote.execScript('print("启动")')
            except:
                while b != 'null':
                    try:
                        b = remote.execScript('print("启动")')
                    except:
                        time.sleep(0.5)

    def create_py(self,scn,materials):
        st = scn.my_tool
        image_path = bpy.path.abspath(st.ImagePath)
        maps = []
        textures_set = {}
        img_path = {}

        for material in materials:
            if st.Bol_AO:
                img_path['AO'] = image_path+material+st.AO_Suffix+st.Image_format
                if os.path.exists(img_path['AO']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['AO'])+' Textures AO non existent')
                    break
                maps.append(img_path['AO'])

            if st.Bol_BentNormals:
                img_path['BentNormals'] = image_path+material+st.BentNormals_Suffix+st.Image_format
                if os.path.exists(img_path['BentNormals']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['BentNormals'])+' Textures AO non existent')
                    break
                maps.append(img_path['BentNormals'])
            
            if st.Bol_Curvature:
                img_path['Curvature'] = image_path+material+st.Curvature_Suffix+st.Image_format
                if os.path.exists(img_path['Curvature']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['Curvature'])+' Textures Curvature non existent')
                    break
                maps.append(img_path['Curvature'])
            
            if st.Bol_Height:
                img_path['Height'] = image_path+material+st.Height_Suffix+st.Image_format
                if os.path.exists(img_path['Height']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['Height'])+'Textures Height non existent')
                    break
                maps.append(img_path['Height'])
            
            if st.Bol_ID:
                img_path['ID'] = image_path+material+st.ID_Suffix+st.Image_format
                if os.path.exists(img_path['ID']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['ID'])+'Textures ID non existent')
                    break
                maps.append(img_path['ID'])
            
            if st.Bol_Normal:
                img_path['Normal'] = image_path+material+st.Normal_Suffix+st.Image_format
                if os.path.exists(img_path['Normal']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['Normal'])+'Textures Normal non existent')
                    break
                maps.append(img_path['Normal'])
            
            if st.Bol_Opacity:
                img_path['Opacity'] = image_path+material+st.Opacity_Suffix+st.Image_format
                if os.path.exists(img_path['Opacity']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['Opacity'])+'Textures Opacity non existent')
                    break
                maps.append(img_path['Opacity'])
            
            if st.Bol_Position:
                img_path['Position'] = image_path+material+st.Position_Suffix+st.Image_format
                if os.path.exists(img_path['Position']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['Position'])+'Textures Position non existent')
                    break
                maps.append(img_path['Position'])
            
            if st.Bol_Thickness:
                img_path['Thickness'] = image_path+material+st.Thickness_Suffix+st.Image_format
                if os.path.exists(img_path['Thickness']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['Thickness'])+'Textures Thickness non existent')
                    break
                maps.append(img_path['Thickness'])
            
            if st.Bol_WorldSpaceNormal:
                img_path['WorldSpaceNormal'] = image_path+material+st.WorldSpaceNormal_Suffix+st.Image_format
                if os.path.exists(img_path['WorldSpaceNormal']) is False:
                    self.report({'ERROR'}, bpy.path.basename(img_path['WorldSpaceNormal'])+'Textures WorldSpaceNormal non existent')
                    break
                maps.append(img_path['WorldSpaceNormal'])
            textures_set[material] = img_path
            img_path = {}
        return textures_set, maps

    def get_selected_materials(self):
        materials = []
        objs = bpy.context.selected_objects
        for obj in objs:
            material_slot = obj.material_slots
            for material in material_slot:
                material_name = material.material.name
                if material_name in materials:
                    pass
                else:
                    materials.append(material_name)
        return materials

    def export_fbx(self,fbxname):

        fbx = bpy.ops.export_scene.fbx(filepath=fbxname, check_existing=True, filter_glob='*.fbx', use_selection=True, use_active_collection=False, global_scale=1.0, apply_unit_scale=True, apply_scale_options='FBX_SCALE_NONE', use_space_transform=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'}, use_mesh_modifiers=True, use_mesh_modifiers_render=True, mesh_smooth_type='OFF', use_subsurf=False, use_mesh_edges=False, use_tspace=False,use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=False, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True, axis_forward='-Z', axis_up='Y')

    def create_sp(self,fbxname,maps,spp):
        remote.execScript('import substance_painter')
        remote.execScript('import time')

        try:
            remote.execScript('substance_painter.project.close()')
        except:
            pass
        remote.execScript('mySettings = substance_painter.project.Settings(normal_map_format=substance_painter.project.NormalMapFormat.OpenGL)')
        remote.execScript('fbxname = r"%s"' %fbxname)
        remote.execScript('maps = %s' %maps)
        remote.execScript('print(fbxname)')
        remote.execScript('')
        remote.execScript('substance_painter.project.create(mesh_file_path=fbxname,mesh_map_file_paths = maps, settings=mySettings)')

        remote.execScript('file_path = r"%s"' %spp)

        a = remote.execScript('substance_painter.project.save_as(file_path)')

        while a != 'null':
                a = remote.execScript('substance_painter.project.save_as(file_path)')
                print(a)
                time.sleep(0.5)

    def create_texture_set(self,texture_set):

        for material in texture_set:
            remote.execScript('material = "%s"' %material)

            remote.execScript('my_texture_set = substance_painter.textureset.TextureSet.from_name(material)')
            
            for img in texture_set[material]:
                
                remote.execScript('%s_map = substance_painter.resource.ResourceID.from_project(name="%s")' %(img, bpy.path.basename(texture_set[material][img]).split('.')[0]))


                remote.execScript('print(%s_map)' %img)

                remote.execScript('my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.%s, %s_map)' %(img,img))


class BtspReImport(Operator):
    bl_description = 'reimport to sp'
    bl_idname = "btsp.reimport"
    bl_label = 'btsp'

    def execute(self, context):

        scn = context.scene
        create_directory(bpy.path.abspath(scn.my_tool.ImagePath))
        spp_project = create_directory(bpy.path.abspath(scn.my_tool.SP_Project_Path))
        fbx_dir = create_directory(bpy.path.abspath(scn.my_tool.SP_Project_Path+'fbx'))
        file_name = bpy.path.basename(bpy.data.filepath)
        fbxname = os.path.join(fbx_dir,file_name.replace('blend','fbx'))
        self.export_fbx(fbxname)

        remote.execScript("import substance_painter.project")
        remote.execScript('mesh_reloading_settings = substance_painter.project.MeshReloadingSettings(import_cameras=True,preserve_strokes=True)')
        remote.execScript('def on_mesh_reload(status=substance_painter.project.ReloadMeshStatus):\n    import substance_painter.project\n    if status == substance_painter.project.ReloadMeshStatus.SUCCESS:\n        print("The mesh was reloaded successfully.")\n    else:\n        print("The mesh couldn`t be reloaded.")')
        a = remote.execScript('substance_painter.project.reload_mesh(r"%s",mesh_reloading_settings,on_mesh_reload)' %fbxname)
        print(a)
        return {"FINISHED"}



    def export_fbx(self,fbxname):

        fbx = bpy.ops.export_scene.fbx(filepath=fbxname, check_existing=True, filter_glob='*.fbx', use_selection=True, use_active_collection=False, global_scale=1.0, apply_unit_scale=True, apply_scale_options='FBX_SCALE_NONE', use_space_transform=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'}, use_mesh_modifiers=True, use_mesh_modifiers_render=True, mesh_smooth_type='OFF', use_subsurf=False, use_mesh_edges=False, use_tspace=False,use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=False, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True, axis_forward='-Z', axis_up='Y')











