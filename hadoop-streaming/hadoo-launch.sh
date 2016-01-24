hadoop jar $HADOOP_HOME/hadoop/hadoop-streaming.jar \
-D mapred.job.name="WordCount Job Via Streaming" \
-files countMap.py, countReduce.py \
-input test.txt \
-output /tmp/wordCount/ \
-mapper countMap.py \
-combiner countReduce.py \
-reduce countReduce.py \
