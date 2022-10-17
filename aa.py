import lib_remote
import time
remote = lib_remote.RemotePainter()

materials = ['MONA_HOUSE_01_01', 'MONA_HOUSE_01_02']
command = 'for material in %s:'%materials +'\n' + \
    '    my_texture_set = substance_painter.textureset.TextureSet.from_name(material)\n' + \
    '    ao_map = substance_painter.resource.ResourceID.from_project(name=material+"_ao")\n' + \
    '    bent_normal_map = substance_painter.resource.ResourceID.from_project(name=material+"_bentnormal")\n' + \
    '    curvature_map = substance_painter.resource.ResourceID.from_project(name=material+"_curve")\n' + \
    '    height_map = substance_painter.resource.ResourceID.from_project(name=material+"_height")\n' + \
    '    id_map = substance_painter.resource.ResourceID.from_project(name=material+"_objid")\n' + \
    '    normal_map = substance_painter.resource.ResourceID.from_project(name=material+"_normal")\n' + \
    '    position_map = substance_painter.resource.ResourceID.from_project(name=material+"_position")\n' + \
    '    thickness_map = substance_painter.resource.ResourceID.from_project(name=material+"_thickness")\n' + \
    '    world_space_normal_map = substance_painter.resource.ResourceID.from_project(name=material+"_normalobj")\n' + \
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.AO, ao_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.BentNormals, bent_normal_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.Curvature, curvature_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.Height, height_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.ID, id_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.Normal, normal_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.Position, position_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.Thickness, thickness_map)\n'+\
    '    my_texture_set.set_mesh_map_resource(substance_painter.textureset.MeshMapUsage.WorldSpaceNormal, world_space_normal_map)\n'






a = remote.execScript(command)
print(a)