'''
Assignment 11
Author: Zewei Liu zl1446
The unitest for my program
'''
import numpy as np
import unittest
from parallel_sorter import generate_data2process
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

class Test_generate_data2process(unittest.TestCase):


	def test_mpi_sort_data(self): 
	# This test case comes from Assignment 11
		dataset = np.array([3,5,7,4,6,7,11,9,2,8,3,2])
		self.assertTrue(generate_data2process(dataset).tolist(), np.array([[2,2], [3,5,4,3], [7,6,7,8], [9, 11]]).tolist() )

if __name__ == '__main__':
	unittest.main()