'''
Author: Zewei Liu
'''
from pyspark import SparkContext
from operator import mul

if __name__ == '__main__':
    sc = SparkContext("local", "result product")
    # Create RDD and Compute the product of numbers in the RDD 
    result_product = sc.parallelize(range(1, 1001)).fold(1,mul)
    print("product of numbers:",result_product)