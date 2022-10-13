# Greeting

A sample Greeting class with greeting function to generate Hello World to learn basic unit testing
and mocking to help me learn about unit test and mocking

## Running test via unittest

To run test via unit test there are various way to run, below are a few:

```
python -m unittest discover -v

# or
python -m unittest discover -v <folder>

# or
python -m unittest discover -v <folder>.<filename>

# or
python -m unittest -v <folder>.<filename>.<TestClass>

# or
python -m unittest -v <folder>.<filename>.<TestClass>.<test_function>

```

## Running test via pytest

Unit test can also be run via pytest as show below

```
pytest -v
```

In order to run pytest, you should install the following packages:

```
pip install pytest
pip install coverage    #optional if you want to use test coverage
pip install pytest-cov  #optional if you want to use test coverage
```

## Generating the test coverage via pytest

```
pytest -v --cov=. --cov-report html
```


## Generating coverage report via unittest

```
coverage run -m unittest discover
coverage html
```
