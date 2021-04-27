from object2urdf import ObjectUrdfBuilder
from pybullet_object_models.cleanup_tools import move_urdfs_to_subdirs, rename_urdfs

# Build entire libraries of URDFs
# Can take a while

# object_folder = "google_scanned_objects"
# object_folder = "ycb_objects"
# object_folder = "gibson_feelies"
object_folder = "gibson_glavens"
object_folder = "gibson_bellpeppers"

builder = ObjectUrdfBuilder(object_folder)
builder.build_library(force_overwrite=True,
                      decompose_concave=True,
                      force_decompose=False,
                      center='mass')

# tidy up
move_urdfs_to_subdirs(object_folder)
rename_urdfs(object_folder)
