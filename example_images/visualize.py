# Load the example pcd 
import open3d as o3d
import numpy as np

def load_example_pcd(np_file):
	d = np.load(np_file, allow_pickle=True, encoding='bytes').item()
	xyz = d['xyz'].reshape(-1, 3)
	print(xyz)
	rgb = d['rgb'].reshape(-1, 3)/255
	pcd = o3d.geometry.PointCloud()
	pcd.points = o3d.utility.Vector3dVector(xyz)
	pcd.colors = o3d.utility.Vector3dVector(rgb)
	o3d.visualization.draw_geometries([pcd])

def load_custom_pcd(pcd_file, rgb_file=None):
	pcd = o3d.io.read_point_cloud(pcd_file)
	pcd_array = np.asarray(pcd.points)
	print(pcd_array)
	pcd_array[:, 1:3] = -pcd_array[:, 1:3]
	pcd.points = o3d.utility.Vector3dVector(pcd_array)
	r = pcd.get_rotation_matrix_from_xyz([0, 0, -np.pi/2])
	pcd.rotate(r)
	print(pcd_array.shape)
	o3d.visualization.draw_geometries([pcd])
	o3d.io.write_point_cloud('custom.pcd', pcd)

if __name__ == '__main__':
	example_pcd = 'OCID_image_0.npy'
	load_example_pcd(example_pcd)

	pcd_file = 'kin_pcd.pcd'
	rgb_file = 'kin_image.png'

	load_custom_pcd(pcd_file)