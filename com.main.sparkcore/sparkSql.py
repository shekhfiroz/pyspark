from pyspark.sql.session import SparkSession
class Spark_Sql:
    def sparkmethods(self):
        df_session = SparkSession.builder.master('local[3]').appName("Spark").getOrCreate()
        df_Auto_Csv = df_session.read.csv('/home/sfa/Desktop/city_of_cicago.json')
        #df_Auto_Csv.printSchema()
        df_Auto_Csv.show()
       # print(df_Auto_Csv)
        #if __name__ == '__main__':
        #df_Auto_Csv.select("purpose").show()
        #df_show=df_Auto_Csv.show().take(5)
        df_count=df_Auto_Csv.count()
        print(df_count)
so=Spark_Sql()
so.sparkmethods()