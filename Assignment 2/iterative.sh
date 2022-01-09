#!/bin/sh
CONVERGE=1
ITER=1
rm v v1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /A2/task-* 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/PES2UG19CS448/A2/mapper_t1.py'" \
-reducer "'/home/PES2UG19CS448/A2/reducer_t1.py' '/home/PES2UG19CS448/A2/v'" \
-input /A2/dataset-sample.txt \
-output /A2/task-1-output

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/PES2UG19CS448/A2/mapper_t2.py' '/home/PES2UG19CS448/A2/v' '/home/PES2UG19CS448/A2/node-map-sample.json'" \
	-reducer "'/home/PES2UG19CS448/A2/reducer_t2.py'" \
	-input /A2/task-1-output/part-00000 \
	-output /A2/task-2-output
	touch v1
	hadoop fs -cat /A2/task-2-output/part-00000 > "/home/PES2UG19CS448/A2/v1"
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /A2/task-2-output/
	echo $CONVERGE
done
