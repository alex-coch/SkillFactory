from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression

# Подготавливаем обучающие данные из списка кортежей (метка, признаки).
trainingDf = spark.createDataFrame([
    (1.0, Vectors.dense([5.0, 1.4, 1.1])),
    (0.0, Vectors.dense([3.0, 1.3, 2.2])),
    (1.0, Vectors.dense([1.0, 1.2, 3.0]))], ["label", "features"])

# Создаем экземпляр LogisticRegression. Этот экземпляр является оценщиком (Estimator).
lr = LogisticRegression(maxIter=10, regParam=0.01)

# Обучаем модель логистической регрессии. При этом используются параметры по умолчанию.
model1 = lr.fit(trainingDf)

# В качестве альтернативы мы можем указать параметры, используя словарь Python в качестве paramMap. 
paramMap = {lr.maxIter: 20}
paramMap.update({lr.regParam: 0.1, lr.threshold: 0.55})  

#lr.probabilityCol - параметр, который отвечает за название столбца с предсказанными вероятностями

# Теперь обучим новую модель, используя параметры paramMap.
model2 = lr.fit(trainingDf, paramMap)

# Подготовим тестовый датасет
test = spark.createDataFrame([
    (1.0, Vectors.dense([-1.0, 1.5, 1.3])),
    (0.0, Vectors.dense([3.0, 2.0, -0.1])),
    (1.0, Vectors.dense([0.0, 2.2, -1.5]))], ["label", "features"])

# Сделаем предсказание для тестовой выборки, используя метод Transformer.transform().
# LogisticRegression.transform будет использовать только вектор-столбец 'features'.
prediction = model2.transform(test)
result = prediction.select("features", "label", "probability", "prediction") \
    .collect()
