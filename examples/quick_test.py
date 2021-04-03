import os
import random

from pybullet_object_models import primitive_objects
from pybullet_object_models import random_objects
from pybullet_object_models import ycb_objects
from pybullet_object_models import superquadric_objects
from pybullet_object_models import google_scanned_objects

# Get the path to the objects inside each package
# data_path = primitive_objects.getDataPath()
# data_path = random_objects.getDataPath()
data_path = ycb_objects.getDataPath()
# data_path = superquadric_objects.getDataPath()
# data_path = google_scanned_objects.getDataPath()

# With this path you can access to the object files, e.g. its URDF model
obj_name = 'banana' # name of the object folder

# or a full list of the available objects can be found with
# model_list = primitive_objects.getModelList()
# model_list = random_objects.getModelList()
model_list = ycb_objects.getModelList()
# model_list = superquadric_objects.getModelList()
# model_list = google_scanned_objects.getModelList()

# from which an object can be selected
rand_object_name = random.choice(model_list)

# the full path is then
path_to_urdf = os.path.join(data_path, rand_object_name, "model.urdf")

print(path_to_urdf)
