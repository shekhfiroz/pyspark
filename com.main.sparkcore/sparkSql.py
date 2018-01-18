from pyspark.sql.session import SparkSession
class Spark_Sql:
    def predict_metrics(self):
        df_session = SparkSession.builder.master('local[6]').appName("Spark").getOrCreate()
        df_Auto_Csv = df_session.read.csv('/home/sfa/Desktop/firoz/DataScience/Churn_Modelling.csv')
       # print(df_Auto_Csv)
        if __name__ == '__main__':
            df_show=df_Auto_Csv.show().take()
            df_count=df_Auto_Csv.count()
            print(df_count)

Spark_Object=Spark_Sql()
Spark_Object.predict_metrics()