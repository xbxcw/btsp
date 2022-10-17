# from func import judgeprocess
from lib_remote import *

remote = RemotePainter()

remote.execScript('import substance_painter')
# a = remote.execScript('print(substance_painter.project.is_open())')
# a = judgeprocess('Adobe Substance 3D Painter.exe')

command = 'mesh_reloading_settings = substance_painter.project.MeshReloadingSettings(import_cameras=True,preserve_strokes=True)'
remote.execScript(command)



command = 'def on_mesh_reload(status=substance_painter.project.ReloadMeshStatus):\n    import substance_painter.project\n    if status == substance_painter.project.ReloadMeshStatus.SUCCESS:\n        print("The mesh was reloaded successfully.")\n    else:\n        print("The mesh couldn`t be reloaded.")'

remote.execScript(command)

command = 'substance_painter.project.reload_mesh("D:/BaiduNetdiskDownload/xiamen/blend/sp/fbx/Mona_house_01.fbx",mesh_reloading_settings,on_mesh_reload)'

# command = 'on_mesh_reload()'

b = remote.execScript(command)

print(b)