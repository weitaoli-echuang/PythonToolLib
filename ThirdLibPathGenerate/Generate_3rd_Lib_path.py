__author__ = 'VDTConstructor'

import os
import shutil


def generate_directorys(lib_name):
	"""generate the relative path for a specical lib
	lib_name
		lib
		include
			lib_name
		bin
			Win32
				Debug
				Release
			x64
				Debug
				Release"""

	path_list = []
	lib_path = os.path.abspath(lib_name)
	rel_lib = os.path.join(lib_path, 'lib')
	rel_include = os.path.join(lib_path, os.path.join('include', lib_name))

	path_list.append(lib_path)
	path_list.append(rel_lib)
	path_list.append(rel_include)

	platform = ['x64', 'Win32']
	runtime = ['Debug', 'Release']

	rel_bin = os.path.join(lib_path, 'bin')
	for plat in platform:
		for run_time in runtime:
			tmp_path = os.path.join(plat, run_time)
			path_list.append(os.path.join(rel_bin, tmp_path))

	if os.path.isdir(lib_path):
		shutil.rmtree(lib_path)

	for path in path_list:
		os.makedirs(path)


if __name__ == '__main__':
	lib_name = 'freeglut'
	generate_directorys(lib_name)

