'''
Author: Zewei Liu
'''
from pyspark import SparkContext
import re

def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
	#create spark context
    sc = SparkContext("local", "num_distinct_word")
    text = sc.textFile('pg2701.txt')
    words = text.flatMap(splitter)
    words_mapped = words.map(lambda x: (x,1))
    sorted_map = words_mapped.sortByKey()
    #we use the distinct and count method to get the number of different words
    num_distinct_words = sorted_map.distinct().count()
    print(num_distinct_words)