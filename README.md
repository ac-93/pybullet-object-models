# pybullet-object-models


<p align="center">
	<img width="180"  src="figures/primitive_example.gif">
	<img width="180"  src="figures/random_example.gif">
	<img width="180"  src="figures/ycb_example.gif">
	<img width="180"  src="figures/superquadric_example.gif">
	<img width="180"  src="figures/google_example.gif">
</p>


This repository contains a collection of object models for simulation, along with helper scripts for downloading, generating and tidying the required files. In particular, they have been tuned and tested in [pybullet](https://github.com/bulletphysics/bullet3/tree/master/examples/pybullet).

The list of available objects includes:

- [Primitive Objects](#primitive-objects)
- [Random Objects](#random-objects)
- [YCB Objects](#ycb-objects)
- [Superquadric Objects](#superquadric-objects)
- [Google Scanned Objects](#google-scanned-objects)

Each object has the following files:

  - Textured mesh for visualization (`.obj`).

  - Simplified mesh for collision (`.obj`). These meshes can be basic shapes or a V-HACD decomposition of the textured mesh, depending on the complexity of the object shape. These are generally generated using the [obj2urdf](https://github.com/cbteeple/object2urdf) package. 

  - URDF file to load the object into the simulation.
  
  - **TODO: add accurate mass and dynamics values to urdfs where possible.**
  
### Setup ###

The repo requires a **python version >= 3**. It can be installed with pip by doing:

```bash
$ git clone https://github.com/eleramp/pybullet-object-models.git
$ pip3 install -e pybullet-object-models/
```

It has been tested only on Ubuntu 18.04 LTS.
  
### Primitive Objects ###

  - A set of simple objects created in blender.


### Random Objects ###

  - Set of randomly generated objects from the [pybullet repo](https://github.com/bulletphysics/bullet3/tree/master/examples/pybullet/gym/pybullet_data/random_urdfs).


### YCB Objects ###

  - The near full set of YCB objects available for download [here](https://www.ycbbenchmarks.com/object-models/).

  - This is too large to store in this repo (approx 1Gb), a tool for dowloading these objects from [here](https://github.com/sea-bass/ycb-tools).
  
  - The downloaded files can then be copied to the `ycb_objects` directory within this repo. This should contain the downloaded files, along with `__init__.py` and `_prototype.urdf` for generating the urdf files using obj2urdf.

  - Additionally, there are 3 SDF files, each loading some YCB objects arranged according to a specific layout. The layouts reproduce the layouts of the [GRASPA-benchmark](https://github.com/robotology/GRASPA-benchmark). **TODO: fix broken orientations on layouts.**

### Superquadric Objects ###

  - Custom objects with a superquadric (superellipsoid) shape, generated using the [pygalmesh tool](https://github.com/nschloe/pygalmesh). 
  
  - Tools are provided for generating your own Superquadric object models. This requires using the [pygalmesh tool](https://github.com/nschloe/pygalmesh) which can be installed the tools by doing:

```bash
$ conda create -n env_pygalmesh python=3.8
$ conda activate env_pygalmesh
$ conda install -c conda-forge pygalmesh
$ pip install trimesh #this is used to interactively fix a bug in the generated meshes, related to the inverted surface normals
```

Using conda to install the tool is not probably the ideal option for some people but it is the best and easiest way at the moment, as pointed out in its [github repo](https://github.com/nschloe/pygalmesh).

We provide information about how to generate custom objects by using the pygalmesh tool.

1. Navigate to the `superquadric_objects` folder:

```bash
$ cd pybullet-object-models/pybullet_object_models/superquadric_objects/
```

2. Activate the conda pygalmesh environment:

```bash
$ conda activate /path/to/env_pygalmesh
```

3. Run the script to generate the meshes:
```bash
$ python generate_superquadric_mesh.py
```
  The output meshes are saved according to the following tree:
```bash
sq_l1_l2_l3_l4_l5/
└── model.obj
```

4. Run the script to generate the URDF model for each new superquadric object:
```
$ python generate_urdf_model.py
```
They are saved inside each superquadric object folder as follow:
```bash
sq_l1_l2_l3_l4_l5/
├── model.obj
└── model.urdf
```

The output meshes have a superquadric shape defined according to the `inside-outside` function:
```
F = ( (x / λ1) ** (2/λ5) + (y / λ2) ** (2/λ5) ) ** (λ5/λ4) + (z / λ3) ** (2/λ4)
```
By default, the `generate_superquadric_mesh.py` creates 100 superquadric meshes, with `λ4, λ5` varying in the range `(0.1, 1.9, step = 0.2)`

You can of course modify the script to reduce the number of generated superquadric meshes as you like.

### Google Scanned Objects ###

  - Over 1000 "common" household objects that have been 3D scanned for use in robotic simulation and synthetic perception research from [Google Research](https://app.ignitionrobotics.org/GoogleResearch/fuel/collections/Google%20Scanned%20Objects).
  
  - This is too large to store on this repo, the full set of objects can be downloaded using this [repo](https://github.com/tommymchugh/gso_downloader).
  
  - I have limited expierience with Bazel but what worked for me was
  
```bash
git clone https://github.com/tommymchugh/gso_downloader.git
cd gso_downloader/
bazel build ...
./bazel-bin/src/download
```
  - This started downloading all the required files into my home directory. **Warning, this is over 10GB**.
  
  - The downloaded files can then be copied to the `google_scanned_objects` directory within this repo. This should contain the downloaded files (in the numbered directories), along with `__init__.py` and `_prototype.urdf` for generating the urdf files using obj2urdf.
  
  - A script for renaming the directories, moving textures and clearing empty directories is provided in `tidy_google_objects.py`. Be careful when using as this will be removing/renaming a large number of files, I would reccomended commenting out any code that alters files and monitoring beforehand to make sure it is working as intended before use.
  
  - This comes with sdf files that can directly be used in pybullet, however for consistency I find automatically generating urdf files using the [obj2urdf](https://github.com/cbteeple/object2urdf) package. A script to do this is provided in `build_object_urdfs.py`, this will also generate convex decompositions, more details are provided in the linked repo. **Warning, takes a while to run for the full google_scanned_objects set**.

### Usage ###

Example scripts for importing the objects into pybullet are provided in the examples folder. To run these cd into the `examples` directory and run `python demo_load_object.py`. Use the `-object_set=` argument to load from a given object set, currently this can be selected from `primitive`, `random`, `ycb`, `superquadric` or `google` if setup correctly.

We use the convention that the object name is the name of the directory, and the urdf file is titled `model.urdf`. The function `getDataPath()` and `getModelList()` can be used to help load objects. Here is a code snippet for importing objects.

```python
import os
import random

from pybullet_object_models import primitive_objects
from pybullet_object_models import random_objects
from pybullet_object_models import ycb_objects
from pybullet_object_models import superquadric_objects
from pybullet_object_models import google_scanned_objects

## Get the path to the objects inside each package
# data_path = primitive_objects.getDataPath()
# data_path = random_objects.getDataPath()
data_path = ycb_objects.getDataPath()
# data_path = superquadric_objects.getDataPath()
# data_path = google_scanned_objects.getDataPath()

## With this path you can access to the object files, e.g. its URDF model
obj_name = 'banana' 

## or a full list of the available objects can be found with 
# model_list = primitive_objects.getModelList()
# model_list = random_objects.getModelList()
model_list = ycb_objects.getModelList()
# model_list = superquadric_objects.getModelList()
# model_list = google_scanned_objects.getModelList()

## from which an object can be selected
object_name = random.choice(model_list)

## the full path is then
path_to_urdf = os.path.join(data_path, object_name, "model.urdf")

## Check by printing
print(path_to_urdf)
```

Here is a Python example to load the objects inside the pybullet simulation:

```python
import os
import time
import pybullet as p
import pybullet_data
from pybullet_object_models import ycb_objects

## Open GUI and set pybullet_data in the path
p.connect(p.GUI)
p.resetDebugVisualizerCamera(3, 90, -30, [0.0, -0.0, -0.0])
p.setTimeStep(1 / 240.)

## Load plane contained in pybullet_data
planeId = p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"))

## Load the object
obj_id = p.loadURDF(os.path.join(ycb_objects.getDataPath(), 'banana', "model.urdf"), [1., 0.0, 0.8])

## Start pybullet loop
p.setGravity(0, 0, -9.8)
while 1:
    p.stepSimulation()
    time.sleep(1./240)
```
