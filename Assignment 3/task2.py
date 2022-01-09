from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql import SQLContext
import sys
from pyspark.sql.functions import col

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

city,globe = sys.argv[1] ,sys.argv[2]

dfc = sqlContext.read.load(city.strip(), 
                      format='com.databricks.spark.csv', 
                      header='true', 
                      inferSchema='true')

dfg = sqlContext.read.load(globe.strip(), 
                      format='com.databricks.spark.csv', 
                      header='true', 
                      inferSchema='true')
                      
dfc=dfc.withColumn('AverageTemperature',col("AverageTemperature").cast("float"))
dfg=dfg.withColumn('LandAverageTemperature',col("LandAverageTemperature").cast("float"))

x=dfc.groupBy('dt', 'Country').max('AverageTemperature')
x=x.withColumnRenamed('max(AverageTemperature)','maxTemp')
x=x.withColumnRenamed('dt','d')

y=dfg.join(x, (x.d == dfg.dt) & (x.maxTemp>dfg.LandAverageTemperature),"inner").groupBy('Country').count().sort('Country').collect()

for i in y:
    print(i['Country'],'\t',i['count'])