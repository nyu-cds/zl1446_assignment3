from mpi4py import MPI
import numpy as np

#get the communicator
comm = MPI.COMM_WORLD
#get the rank of the process
rank = comm.Get_rank()
size = comm.Get_size()
#internal value in every step
internal_value = np.zeros(1)


if rank == 0:
    #initial step at rank 0
    while (True):
        print("input an integer less than 100:")
        input_val = raw_input('')
        # check whether it is integer
        try: 
            internal_value[0]=int(input_val)
        except ValueError as error:
            print(error)
            continue
        if internal_value[0]>=100:
            print("input should be less than 100")
        else:
            break
    #final step at rank 0, recieve value
    comm.Send(internal_value, dest=1)
    comm.Recv(internal_value, source=size-1)
    print("our final result is %d"  % (int(internal_value[0])))
elif rank>0 and rank<size-1:
#send internal number to next rank
    comm.Recv(internal_value, source=rank-1)
    internal_value = internal_value*rank
    comm.Send(internal_value, dest=rank+1)
#send back to process 0
elif rank==size-1:
    comm.Recv(internal_value, source=rank-1)
    internal_value = internal_value*rank
    comm.Send(internal_value, dest=0)