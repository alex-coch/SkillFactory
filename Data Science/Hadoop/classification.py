from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

(trainingData, testData) = output.randomSplit([0.7, 0.3])

rf = RandomForestClassifier(labelCol="labelIndex", featuresCol="full_features", numTrees=10)
model = rf.fit(trainingData)
predictions = model.transform(testData)

predictions.select("rawPrediction", "labelIndex", "full_features").show(5)

evaluator = BinaryClassificationEvaluator()

evaluator = BinaryClassificationEvaluator()
evaluator.setRawPredictionCol("rawPrediction")
evaluator.setLabelCol("labelIndex")

print(evaluator.evaluate(predictions))
evaluator.getMetricName()
