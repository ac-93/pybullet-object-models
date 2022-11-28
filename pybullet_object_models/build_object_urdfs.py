import os
import shutil
from object2urdf import ObjectUrdfBuilder
from pybullet_object_models.cleanup_tools import move_urdfs_to_subdirs, rename_urdfs
from pybullet_object_models.cleanup_tools import get_immediate_subdirectories

# Build entire libraries of URDFs
# Can take a while

# object_folder = "google_scanned_objects"
# object_folder = "ycb_objects"
# object_folder = "gibson_feelies"
# object_folder = "gibson_glavens"
# object_folder = "gibson_bellpeppers"
# object_folder = "egad/egad_eval_set"
# object_folder = "egad/egad_train_set"

# builder = ObjectUrdfBuilder(object_folder)
# builder.build_library(force_overwrite=True,
#                       decompose_concave=True,
#                       force_decompose=False,
#                       center='mass')
#
# tidy up
# move_urdfs_to_subdirs(object_folder)
# rename_urdfs(object_folder)

# shapenet_folder = "test_folder/shapenet_core"
shapenet_folder = "shapenet/ShapeNetCoreV2"
subdirs = get_immediate_subdirectories(shapenet_folder)

for subdir in subdirs:
    object_folder = os.path.join(shapenet_folder, subdir)

    # copy prototype.urdf to subdir
    src_proto = os.path.join(shapenet_folder, '_prototype.urdf')
    dst_proto = os.path.join(object_folder, '_prototype.urdf')
    shutil.copy2(src_proto, dst_proto)

    # build urdfs
    builder = ObjectUrdfBuilder(object_folder)
    builder.build_library(force_overwrite=True,
                          decompose_concave=False,
                          force_decompose=False,
                          center='mass')

    # tidy up
    move_urdfs_to_subdirs(object_folder)
    rename_urdfs(object_folder)
