from pyspark import SparkConf, SparkContext
from pyspark import files

class Auto():
    def autocount(self):
        conf = SparkConf().setMaster("local").setAppName("pysparkapp").setMaster("local")
        sparkcontext = SparkContext(conf = conf)
        autoRDD=sparkcontext.textFile("/home/sfa/Music/pyspark/data/Auto.csv")
        print(autoRDD.first())
        print(autoRDD.take(5))
        print(autoRDD.count())
a=Auto()
a.autocount()
