### Usage
- install required packages with pipenv command --dev
```
pipenv install --dev
```
- run main function with pipenv command run start
```
pipenv run start
```

## Installation of autosklearn
- upgrade pip to the latest version
```
pip install upgrade pip
```
- install swig that is required for auto-sklearn
```
apt-get install swig
```
- install auto-sklearn
```
pip install auto-sklearn
```

## auto-sklearn example

You will find [resources][resource] in the official site.
```
import autosklearn.classification
cls = autosklearn.classification.AutoSklearnClassifier()
cls.fit(X_train, y_train)
predictions = cls.predict(X_test)
```

[resource]: https://automl.github.io/auto-sklearn/master/ "auto-sklearn official"

