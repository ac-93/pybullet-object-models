import os
import time
import random
import pybullet as p
import pybullet_data
import sys
import numpy as np

from pybullet_object_models.layouts import ycb_graspa_layouts

# connect to pybullet and load a plane
p.connect(p.GUI)
p.setGravity(0,0,-10)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

plane_id = p.loadURDF("plane.urdf")

data_path = ycb_graspa_layouts.getDataPath()
layout_list = ycb_graspa_layouts.getLayoutList()

draw_com = False

# load random object
def reset(layout_id):

    # remove if already exists
    if layout_id is not None:
        p.removeBody(layout_id)

    # select rand file
    rand_layout = random.choice(layout_list)

    # load layout
    # print(rand_layout)
    # layout_id = p.loadSDF(rand_layout)
    layout_id = p.loadSDF('/home/alex/Documents/pybullet-object-models/pybullet_object_models/layouts/ycb_graspa_layouts/layout_2.sdf')

    return layout_id

layout_id = reset(None)

# set camera position
cam_dist = 1.0
cam_yaw = 0
cam_pitch = -20
cam_pos = [0, 0, 0]
p.resetDebugVisualizerCamera(cam_dist, cam_yaw, cam_pitch, cam_pos)

# infinite loop of sim
while True:
    p.stepSimulation()
    time.sleep(1./240.)

    if draw_com:
        for obj_id in layout_id:
            p.addUserDebugLine([0, 0, 0], [0.1, 0, 0], [1, 0, 0], parentObjectUniqueId=obj_id, lifeTime=0.1)
            p.addUserDebugLine([0, 0, 0], [0, 0.1, 0], [0, 1, 0], parentObjectUniqueId=obj_id, lifeTime=0.1)
            p.addUserDebugLine([0, 0, 0], [0, 0, 0.1], [0, 0, 1], parentObjectUniqueId=obj_id, lifeTime=0.1)


    # press q to break
    q_key = ord('q')
    r_key = ord('r')
    keys = p.getKeyboardEvents()
    if q_key in keys and keys[q_key] & p.KEY_WAS_TRIGGERED:
        exit()
    elif r_key in keys and keys[r_key] & p.KEY_WAS_TRIGGERED:
        layout_id = reset(layout_id)

p.disconnect()
