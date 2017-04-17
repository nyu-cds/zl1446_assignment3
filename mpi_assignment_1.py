"""
MPI program, pring hello when rank is even, goodbye otherwise.
"""
from mpi4py import MPI
#get the communicator
comm = MPI.COMM_WORLD
#print comm
#get the rank of the process
rank = comm.Get_rank()
# print rank

# size = comm.Get_size()
# print size
if rank % 2 == 0:
    print("Hello from process %d" % (rank))
else:
    print("Goodbye from process %d" % (rank))