'''
Created on 02-Aug-2017

@author: Padmakumar
'''
from pyspark import SparkConf, SparkContext
import collections

# create SparkContext using standalone mode
conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

# create a RDD from text file and transform it to only contains ratings column
linesRDD = sc.textFile("./u.data")
ratingsRDD = linesRDD.map(lambda x: x.split()[2])

# use RDD action countByValue to count how many times each value occurs..
result = ratingsRDD.countByValue()

# print out the results
sortedResults = collections.OrderedDict(sorted(result.items()))
print('\nRating Count')
for key, value in sortedResults.items():
    print("%s %i" % (key, value))