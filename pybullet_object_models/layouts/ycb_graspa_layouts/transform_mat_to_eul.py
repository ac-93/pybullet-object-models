

def rot2eul(R):
    beta = -np.arcsin(R[2,0])
    alpha = np.arctan2(R[2,1]/np.cos(beta),R[2,2]/np.cos(beta))
    gamma = np.arctan2(R[1,0]/np.cos(beta),R[0,0]/np.cos(beta))
    return np.array((alpha, beta, gamma))

# mustard transform test
trans_mat = np.array([
    [-0.36, -0.932952303175248,  0, -74.79695182],
    [0.932952303175248, -0.36,  0, 161.16925375],
    [0, 0,  1, 8],
    [0, 0,  0, 1]
]) *0.001


rot_mat = trans_mat[:3,:3]
eul = rot2eul(rot_mat)
pos = trans_mat[:3,3]
