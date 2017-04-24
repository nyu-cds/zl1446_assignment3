'''
Assignment 11
Author: Zewei Liu zl1446
The unitest for my program
'''
import numpy as np
import unittest
from parallel_sorter import mpi_sort_data
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

class TestSort(unittest.TestCase):


	def test_mpi_sort_data(self): 
	# This test case comes from Assignment 11
		dataset = np.array([3,5,7,4,6,7,11,9,2,8,3,2])
		self.assertEqual(sorted_list,np.array([2,2,3,3,4,5,6,7,7,8,9,11]))

if __name__ == '__main__':
	unittest.main()