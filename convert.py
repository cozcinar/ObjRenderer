import bpy, os, glob
def convert_one_glb(glb, path_to_obj):
    
    glb_prefix = glb.split('/')[1]
    glb_path = glb.split('/')[0]
    # glb_prefix = path_to_glb.split(os.sep)[-1][:-4]
    target_obj = glb_path + '/' + glb_prefix + '/geometry_result/' + glb_prefix + ".obj"
    path_to_glb = glb_path + '/' + glb_prefix + '/geometry_result/' + glb_prefix + ".glb"

    bpy.ops.import_scene.gltf(filepath=path_to_glb)
    for collection in bpy.data.collections:
       for obj in collection.all_objects:
          if obj.name == 'Cube' or obj.name == 'Light' or obj.name == 'Camera' or 'plane' in obj.name or 'light' in obj.name:
              obj.select_set(True)
    bpy.ops.object.delete()
    bpy.ops.export_scene.obj(filepath=target_obj)
    for collection in bpy.data.collections:
       for obj in collection.all_objects:
           obj.select_set(True)
    bpy.ops.object.delete()

glb_folder = "models/*/"
path_to_glbs = glob.glob(glb_folder)
for glb in path_to_glbs:
    convert_one_glb(glb, glb_folder)