from pyspark.ml.classification import LogisticRegression

# Загружаем данные
training = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

# Обучаем модель
lrModel = lr.fit(training)

# Выведем коэффициенты и intercept для логистической регрессии
print("Coefficients: " + str(lrModel.coefficients))
print("Intercept: " + str(lrModel.intercept))

# Мы также можем использовать полиномиальное семейство для бинарной классификации.
mlr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8, family="multinomial")

# Обучаем
mlrModel = mlr.fit(training)

# Выведем коэффициенты и intercept для полиномиальной логистической регрессии 
print("Multinomial coefficients: " + str(mlrModel.coefficientMatrix))
print("Multinomial intercepts: " + str(mlrModel.interceptVector))
