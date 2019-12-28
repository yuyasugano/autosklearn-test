#!/usr/bin/python
import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
import time

def autosk(X, y):
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=39)
    automl = autosklearn.classification.AutoSklearnClassifier()
    automl.fit(X_train, y_train)
    y_predict = automl.predict(X_test)
    print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_predict))

    return automl

def main():
    X, y = sklearn.datasets.load_iris(return_X_y=True)
    ret = autosk(X, y)
    print(ret)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("Elapsed time: {}".format(elapsed_time) + "[sec]")


