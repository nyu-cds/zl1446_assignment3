'''
Author: Zewei Liu
'''
from pyspark import SparkContext
from operator import add
from math import sqrt

if __name__ == '__main__':
    sc = SparkContext("local", "average_square_root")
        
    # Create RDD from 1 to 1,000 and Compute the square root of each number in the RDD
    sqrts_result = sc.parallelize(range(1, 1001)).map(sqrt)
    # Compute the average of the square roots #
    average = sqrts.fold(0, add)/sqrts_result.count()
    print("average of square roots required is :",average)