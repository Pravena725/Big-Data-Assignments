from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql import SQLContext
import sys

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

country,path = sys.argv[1] ,sys.argv[2]

df = sqlContext.read.load(path.strip(), 
                      format='com.databricks.spark.csv', 
                      header='true', 
                      inferSchema='true')

df=df.filter(df.Country==country.strip())

df.na.drop(subset=["City","AverageTemperature"])

x = df.groupBy('City').mean('AverageTemperature')
x=x.withColumnRenamed('avg(AverageTemperature)','avgTemp')
x=x.withColumnRenamed('City','c')

#df.filter(df.City==x.city & df.AverageTemperature )

y=df.join(x, df.City == x.c,"inner")
o=y.filter(y.AverageTemperature>y.avgTemp).groupBy('City').count().select('City','count').sort('City').collect()

for i in o:
    print(i['City'],'\t',i['count'])

