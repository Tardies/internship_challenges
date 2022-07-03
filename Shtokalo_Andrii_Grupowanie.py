import bpy

def create_cube():
    verts = [(0, 0, 0),
             (3, 0, 0),
             (3, 3, 0),
             (0, 3, 0),
             (0, 0, 3),
             (3, 0, 3),
             (3, 3, 3),
             (0, 3, 3)]
        
    faces = [(0, 1, 2, 3),
             (7, 6, 5, 4),
             (0, 4, 5, 1),
             (1, 5, 6, 2),
             (2, 6, 7, 3),
             (3, 7, 4, 0)]
             
    mesh = bpy.data.meshes.new("Cube")
    object = bpy.data.objects.new("Cube", mesh)
    
    bpy.context.collection.objects.link(object)
    
    mesh.from_pydata(verts, [], faces)
    mesh.update(calc_edges = True)
    
def create_sphere():
    bpy.ops.mesh.primitive_uv_sphere_add(radius=2, 
                                         enter_editmode=False, align='WORLD', 
                                         location=(5, 2, 2), 
                                         scale=(1, 1, 1))

def create_cone():
    bpy.ops.mesh.primitive_cone_add(radius1=2, 
                                    radius2=0,
                                    depth=4,
                                    enter_editmode=False,
                                    align='WORLD',
                                    location=(9, 2, 2),
                                    scale=(1, 1, 1))

def create_cylinder():
    bpy.ops.mesh.primitive_cylinder_add(radius=2,
                                        depth=4,
                                        enter_editmode=False,
                                        align='WORLD',
                                        location=(13, 2, 2),
                                        scale=(1, 1, 1))

def main():
    CONTENTS = bpy.data.collections.new('CONTENTS')
    #create_cube()
    #create_sphere()
    #create_cone()
    #create_cylinder()
    #bpy.ops.object.move_to_collection(collection_index=0)
    
    bpy.ops.mesh.primitive_cube_add()
    # our created cube is the active one
    obj = bpy.context.active_object
    # Remove object from all collections not used in a scene
    bpy.ops.collection.objects_remove_all()
    # add it to our specific collection
    bpy.data.collections['CONTENTS'].objects.link(obj)
    bpy.context.scene.collection.children.link(CONTENTS)

    
    


if __name__ == "__main__":
    main()