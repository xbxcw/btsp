import re
import sys
import json
import base64
import subprocess


if sys.version_info >= (3, 0):
    import http.client as http
else:
    import httplib as http


class RemotePainter():
    def __init__(self, port=60041, host='localhost'):
        self._host = host
        self._port = port

        # Json server connection
        self._PAINTER_ROUTE = '/run.json'
        self._HEADERS = {'Content-type': 'application/json',
                         'Accept': 'application/json'}

    # Execute a HTTP POST request to the Substance Painter server and send/receive JSON data
    def _jsonPostRequest(self, route, body, type):
        connection = http.HTTPConnection(self._host, self._port, timeout=3600)
        connection.request('POST', route, body, self._HEADERS)
        response = connection.getresponse()

        data = response.read()
        connection.close()

        if type == "js":
            data = json.loads(data.decode('utf-8'))

            if 'error' in data:
                OutJson = json.loads(body.decode())
                print(base64.b64decode(OutJson["js"]))
                raise ExecuteScriptError(data['error'])
        else:
            # Python can return nothing, so decoding can fail
            try:
                data = data.decode('utf-8').rstrip()
            except:
                pass

        return data

    def checkConnection(self):
        connection = http.HTTPConnection(self._host, self._port)
        connection.connect()

    # Execute a command
    def execScript(self, script, type='python'):
        Command = base64.b64encode(script.encode('utf-8'))

        if type == "js":
            Command = '{{"js":"{0}"}}'.format(Command.decode('utf-8'))
        else:
            Command = '{{"python":"{0}"}}'.format(Command.decode('utf-8'))

        Command = Command.encode("utf-8")

        return self._jsonPostRequest(self._PAINTER_ROUTE, Command, type)


class PainterError(Exception):
    def __init__(self, message):
        super(PainterError, self).__init__(message)


class ExecuteScriptError(PainterError):
    def __init__(self, data):
        super(PainterError, self).__init__(
            'An error occured when executing script: {0}'.format(data))

# fbxname = r'D:\BaiduNetdiskDownload\xiamen\blend\sp\fbx\temp.fbx'

# sp = r"C:\Program Files\Adobe\Adobe Substance 3D Painter\Adobe Substance 3D Painter.exe" + \
#     ' --enable-remote-scripting'


# # subprocess.Popen(sp)


# def executeFbx(fbxname):
#     a = bpy.ops.export_scene.fbx(filepath=fbxname, check_existing=True, filter_glob='*.fbx', use_selection=True, use_active_collection=False, global_scale=1.0, apply_unit_scale=True, apply_scale_options='FBX_SCALE_NONE', use_space_transform=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'}, use_mesh_modifiers=True, use_mesh_modifiers_render=True, mesh_smooth_type='OFF', use_subsurf=False, use_mesh_edges=False, use_tspace=False,
#                                  use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=False, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True, axis_forward='-Z', axis_up='Y')
#     print('a')
#     return {"FINISHED"}


# command = 'import substance_painter.project\n' + 'mySettings = substance_painter.project.Settings(normal_map_format=substance_painter.project.NormalMapFormat.OpenGL)\n' + "fbxname = %s \n" % fbxname + 'substance_painter.project.create(mesh_file_path=meshFile, settings=mySettings)' 

# executeFbx(fbxname)
# remote = RemotePainter()
# remote.execScript(command)


def register():
    pass


def unregister():
    pass