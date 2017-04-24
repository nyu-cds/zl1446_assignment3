
'''
Assignment 11
Author: Zewei Liu zl1446
This file could sort a large dataset using MPI.
'''

from mpi4py import MPI
import numpy as np


#get the communicator
comm = MPI.COMM_WORLD
#get the rank of the process
rank = comm.Get_rank()
#get the size
size = comm.Get_size()

def generate_data():
    return np.random.randint(10000, size=10000)

def mpi_sort_data(input_dataset): 
    if rank == 0:
        bin_length = (np.max(input_dataset) - np.min(input_dataset)) / float(size - 1)
        data2process = list()
        for i in range(-1, size-1):
            every_process_data_list = list()
            for x in input_dataset:
                if (np.min(input_dataset) + bin_length * i) < x <= (np.min(input_dataset) + bin_length * (i + 1)):
                    every_process_data_list.append(x)
            data2process.append(every_process_data_list)
    else:
        data2process = None
    # scatter each part of the data to each rank process
    data_scattered = comm.scatter(data2process, root=0)
    #sort each part of the data in every process seperately
    data2gather = np.sort(data_scattered)
    print rank
    print data2gather
    #in the root process, gather the data from each process
    sorted_data = comm.gather(data2gather, root=0)
    if rank == 0:
        sorted_data = np.concatenate(sorted_data)
        print("final result is \n")
        print(sorted_data)
    return sorted_data

if __name__ =='__main__':
    #generate dataset
    # input_dataset = np.array([3,5,7,4,6,7,11,9,2,8,3,2])
    input_dataset = generate_data()
    mpi_sort_data(input_dataset)