from pyspark.ml.classification import LogisticRegression

# Извлекаем сводку из возвращенного экземпляра LogisticRegressionModel, обученного
# в предыдущем примере
modelSummary = lrModel.summary

# Выведем информацию по каждой итерации
modelHistory = modelSummary.objectiveHistory
print("objectiveHistory:")
for objective in modelHistory:
    print(objective)

# Выведем метрики
modelSummary.roc.show()
print("areaUnderROC: " + str(modelSummary.areaUnderROC))

# Зададим вручную порог для классификации, чтобы максимизировать F-Measure
fMeasure = modelSummary.fMeasureByThreshold
maxFMeasure = fMeasure.groupBy().max('F-Measure').select('max(F-Measure)').head()
bestThreshold = fMeasure.where(fMeasure['F-Measure'] == maxFMeasure['max(F-Measure)']) \
    .select('threshold').head()['threshold']

lr.setThreshold(bestThreshold)
